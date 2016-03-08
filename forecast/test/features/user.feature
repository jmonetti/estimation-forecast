Feature: Handle storing, retrieving and deleting project data
  Scenario: Retrieve projects details
    Given the system know about the following projects:
    |  name        | sprints|
    | Lion Project | 12     |
    | Ads Project  | 22     |
    When the client request GET /projects
    The the response status should be "200"
    And the json response should be and array with 2 "name" elements
    And the response should be JSON:
    """
    [
      {
        "name": "Lion Project",
        "sprints": 12
      },
      {
        "name": "Ads Project",
        "sprints": 22
      }
    ]
    """

