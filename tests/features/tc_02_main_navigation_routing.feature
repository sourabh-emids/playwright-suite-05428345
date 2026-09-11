Feature: TC-02 Main navigation routing
  Verify that each desktop main-navigation category exposes and reaches its intended destination.

  Scenario Outline: A main navigation category reaches its destination
    Given the TC-02 user is on the Emids homepage
    When the TC-02 user selects the "<menu_name>" main navigation category
    Then the TC-02 "<menu_name>" destination "<expected_path>" loads without an error

    Examples:
      | menu_name    | expected_path                                  |
      | Solutions    | /solutions/modernization-as-a-service/         |
      | Capabilities | /capabilities/data-engineering/                |
      | Industries   | /segments/payer/                               |
      | Insights     | /insights/                                     |
      | Company      | /about-us/                                     |
