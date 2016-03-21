import json

from behave import given, when, then
from webtest import TestApp

from forecast.data_access.data_access import DataAccess
from forecast.app import app


@given(u'I access to the resource url "{resource_url}"')
def step_impl(context, resource_url):
    context.resource_url = resource_url


@given(u'the system knows about a set of projects')
def step_impl(context):
    projects = []
    for row in context.table:
        projects.append(
            {
                'name': row['name'],
                'sprints': row['sprints']
            }
        )
    DataAccess().add_projects(projects)


@when(u'I retrieve the results')
def step_impl(context):
    context.app = TestApp(app)
    context.response = context.app.get(context.resource_url)


@when(u'I store the data')
def step_impl(context):
    context.app = TestApp(app)
    context.response = context.app.post(
        context.resource_url,
        context.project
    )


@then(u'the status should be "{status_code}"')
def step_impl(context, status_code):
    assert context.response.status == status_code


@then(u'the json response should be and array with 2 "{attribute_name}" elements')
def step_impl(context, attribute_name):
    response_dict = json.loads(context.response.body)
    projects = response_dict['projects']

    assert len(projects) == 2
    for project in projects:
        assert attribute_name in project


@given(u'the system has no projects stored')
def step_impl(context):
    DataAccess().reset_projects()


@given(u'I provide data for a project')
def step_impl(context):
    assert context.text is not None, "REQUIRE: text"
    context.project = context.text


@then(u'the json response should be')
def step_impl(context):
    assert json.loads(context.text) == json.loads(context.response.body)

