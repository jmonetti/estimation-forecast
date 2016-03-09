# -*- coding: utf-8 -*-
import json

from lettuce import step, before, world
from webtest import TestApp

from forecast.data_access.data_access import DataAccess
from forecast.server import app


@before.all
def before_all():
    world.data_access = DataAccess()
    world.app = TestApp(app)


@step(u'Given the system know about the following projects:')
def given_the_system_know_about_the_following_projects(step):
    world.data_access.add_projects(step.hashes)


@step(u'When the client request GET /projects')
def when_the_client_request_get_projects(step):
    world.response = world.app.get('/projects')


@step(u'The response status should be "([^"]*)"')
def the_response_status_should_be_group1(step, group1):
    assert world.response.status == group1


@step(u'And the json response should be and array with 2 "([^"]*)" elements')
def and_the_json_response_should_be_and_array_with_2_group1_elements(step, group1):
    response_dict = json.loads(world.response.body)
    projects = response_dict['projects']

    assert len(projects) == 2
    for project in projects:
        assert group1 in project
