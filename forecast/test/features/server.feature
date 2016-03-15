Feature: Handle storing, retrieving and deleting project data
  @Get @Positive
  Scenario: Retrieve projects details
    Given I access to the resource url "/projects"
    And the system knows about a set of projects
    |  name        | sprints|
    | Lion Project | 12     |
    | Ads Project  | 22     |
    When I retrieve the results
    Then the status should be "200 OK"
    And the json response should be and array with 2 "name" elements

  @Post @Positive
  Scenario: Add project
    Given I access to the resource url "/projects/"
    And the system has no projects stored
    And I provide details for a project:
    |  name        | sprints|
    | New Project  | 10     |
    When I retrieve the results
    Then the response status should be "201 OK"
    And the json response should be:
    """
    {
      "name": "New project",
      "sprints": 10
    }
    """

    @Put @Positive
    Scenario: Update project
      Given I access to the resource url "/projects/"
      And the system knows about a set of projects
      |  name        | sprints|
      | Lion Project | 12     |
      And I provide a valid project id
      And I provide details for a project:
      |  name            | sprints|
      | Updated Project  | 10     |
      When I retrieve the results
      Then the response status should be "201 OK"
      And the json response should be:
      """
      {
        "name": "Updated project",
        "sprints": 10
      }
      """
