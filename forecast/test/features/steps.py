# -*- coding: utf-8 -*-
from data_access.data_access import DataAccess
from lettuce import step, before, world


@before.all
def before_all():
    world.data_access = DataAccess()


@step(u'Given the system know about the following projects:')
def given_the_system_know_about_the_following_projects(step):
    world.data_access.add_projects(step.hashes)


@step(u'When the client request GET /projects')
def when_the_client_request_get_projects(step):
    assert False, 'This step must be implemented'

@step(u'The the response status should be "([^"]*)"')
def the_the_response_status_should_be_group1(step, group1):
    assert False, 'This step must be implemented'


@step(u'And the json response should be and array with 2 "([^"]*)" elements')
def and_the_json_response_should_be_and_array_with_2_group1_elements(step, group1):
    assert False, 'This step must be implemented'


@step(u'And the response should be JSON:')
def and_the_response_should_be_json(step):
    assert False, 'This step must be implemented'