@issue_0002 @navigation
Feature: Main navigation opens the correct destinations

  Scenario Outline: A main navigation menu opens its intended destination
    Given the Emids homepage and main navigation are available
    When the user opens the "<navigation_item>" menu and selects its "<destination>" destination
    Then the intended "<path>" page opens

    Examples:
      | navigation_item | destination     | path                           |
      | Solutions       | Solutions       | /solutions/                    |
      | Capabilities    | Data Engineering | /capabilities/data-engineering/ |
      | Industries      | Payer           | /segments/payer/               |
      | Insights        | Insights Hub    | /insights/                     |
      | Company         | Our Story       | /about-us/                     |
