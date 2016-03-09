Feature: Handle storing, retrieving and deleting project data
  Scenario: Retrieve projects details
    Given the system know about the following projects:
    |  name        | sprints|
    | Lion Project | 12     |
    | Ads Project  | 22     |
    When the client request GET /projects
    The response status should be "200 OK"
    And the json response should be and array with 2 "name" elements