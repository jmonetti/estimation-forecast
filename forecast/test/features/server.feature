Feature: Handle storing, retrieving and deleting project data
  Scenario: Retrieve projects details
    Given the client uses the forecast API
    And the system knows about a set of projects
    |  name        | sprints|
    | Lion Project | 12     |
    | Ads Project  | 22     |
    When the client request GET /projects
    Then the response status should be "200 OK"
    And the json response should be and array with 2 "name" elements

  Scenario: Add project
    Given the client use the forecast API
    When the client request POST projects/ with the following JSON:
    """
    {
      "name": "New project",
      "sprints": 10
    }
    """
    Then the response status should be "200 OK"
    And the json response should be and array with 1 "name" elements
    