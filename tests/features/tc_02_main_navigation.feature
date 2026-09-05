@TC-02 @functional @navigation
Feature: Main navigation opens the correct pages
  Each main menu must expose a destination that opens its corresponding page.

  Scenario Outline: Open a destination from every main navigation menu
    Given the Emids homepage is open
    When the user opens the "<menu>" menu and selects "<item>"
    Then the destination path is "<path>"

    Examples:
      | menu         | item             | path                           |
      | Solutions    | Solutions        | /solutions/                    |
      | Capabilities | Data Engineering | /capabilities/data-engineering/ |
      | Industries   | Payer            | /segments/payer/               |
      | Insights     | Insights Hub     | /insights/                     |
      | Company      | Our Story        | /about-us/                     |
