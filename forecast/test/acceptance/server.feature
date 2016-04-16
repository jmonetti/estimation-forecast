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
    Given I access to the resource url "/projects"
    And the system has no projects stored
    And I provide data for a project:
    """
    {
      "name": "New project",
      "sprints": 10
    }
    """
    When I store the data
    Then the status should be "201 CREATED"
    And the json response should be:
    """
    {
      "name": "New project",
      "sprints": 10
    }
    """
    
  @Put @Positive
  Scenario: Update project
    Given I access to the resource url "/projects"
    And the system knows about a set of projects
      | id |    name        | sprints|
      | 1  | Lion Project   | 12     |
    And I provide a valid project id
    And I provide data for a project:
    """
    {
      "name": "update",
      "sprints": 10
    }
    """
    When I update the project with id 1
    Then the response status should be "201 OK"
    And the json response should be:
    """
    {
      "name": "Updated project",
      "sprints": 10
    }
    """
