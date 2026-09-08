@TC-02
Feature: Emids main navigation
  As a website visitor
  I want each main navigation menu to open its intended destination
  So that I can reach the site's primary content areas

  Scenario Outline: Main navigation opens the correct pages
    Given the Emids homepage and main navigation are available
    When I select the "<menu>" menu and its destination at "<path>"
    Then the navigation destination "<path>" loads without a visible page error

    Examples:
      | menu         | path                               |
      | Solutions    | /solutions/                        |
      | Capabilities | /capabilities/digital-engineering/ |
      | Industries   | /segments/payer/                   |
      | Insights     | /insights/                         |
      | Company      | /about-us/                         |
