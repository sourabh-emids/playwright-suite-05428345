Feature: Main navigation opens the correct pages
  As a visitor
  I want each main navigation category to expose its destination
  So that I can reach the corresponding content

  Scenario Outline: A main navigation category opens its expected page
    Given the homepage is loaded for navigation
    When the visitor opens the "<menu>" menu and selects "<item>"
    Then the expected "<path>" page is open

    Examples:
      | menu         | item             | path                                      |
      | Solutions    | Modernization    | /solutions/modernization-as-a-service/   |
      | Capabilities | Data Engineering | /capabilities/data-engineering/          |
      | Industries   | Payer            | /segments/payer/                         |
      | Insights     | Insights Hub     | /insights/                               |
      | Company      | Our Story        | /about-us/                               |
