import json

from behave import given, when, then
from webtest import TestApp

from forecast.data_access.data_access import DataAccess
from forecast.server import app


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


@when(u'the client request GET /projects')
def step_impl(context):
    context.app = TestApp(app)
    context.response = context.app.get('/projects')


@then(u'the response status should be "{text}"')
def step_impl(context, text):
    assert context.response.status == text


@then(u'the json response should be and array with 2 "{text}" elements')
def step_impl(context, text):
    response_dict = json.loads(context.response.body)
    projects = response_dict['projects']

    assert len(projects) == 2
    for project in projects:
        assert text in project