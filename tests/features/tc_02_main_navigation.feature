@TC-02
Feature: Main navigation destinations
  As a website visitor
  I want each main navigation menu to route to its defined destination
  So that I can find the corresponding content

  Scenario Outline: Main navigation opens the corresponding page
    Given the Emids homepage is open in a desktop browser
    When the user opens the "<navigation_item>" menu and selects its defined destination
    Then the corresponding page at "<expected_path>" opens

    Examples:
      | navigation_item | expected_path                              |
      | Solutions       | /solutions/modernization-as-a-service/     |
      | Capabilities    | /capabilities/data-engineering/            |
      | Industries      | /segments/payer/                           |
      | Insights        | /insights/                                 |
      | Company         | /about-us/                                 |
