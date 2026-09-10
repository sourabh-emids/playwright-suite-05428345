Feature: Main navigation destinations

  Scenario Outline: Main navigation opens the correct destinations
    Given the Emids homepage is open for navigation
    When the user opens the "<menu>" main navigation menu
    And the user selects the "<destination>" destination for "<path>"
    Then the browser opens the navigation path "<path>"

    Examples:
      | menu         | destination     | path                            |
      | Solutions    | Solutions       | /solutions/                     |
      | Capabilities | Data Engineering| /capabilities/data-engineering/ |
      | Industries   | Payer           | /segments/payer/                |
      | Insights     | Insights Hub    | /insights/                      |
      | Company      | Our Story       | /about-us/                      |
