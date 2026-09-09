@issue_0002
Feature: Main navigation destinations

  Scenario Outline: A main navigation menu opens its intended destination
    Given the homepage main navigation is available
    When the user opens the "<menu>" menu and selects "<destination>"
    Then the destination path is "<path>" with heading "<heading>"

    Examples:
      | menu         | destination      | path                            | heading                               |
      | Solutions    | Solutions        | /solutions/                     | Solutions                             |
      | Capabilities | Data Engineering | /capabilities/data-engineering/ | Data Engineering                      |
      | Industries   | Payer            | /segments/payer/                | Transforming Payer Operations         |
      | Insights     | Insights Hub     | /insights/                      | The intelligence behind the outcomes. |
      | Company      | Our Story        | /about-us/                      | About Us                              |

  Scenario: Connect opens the contact page
    Given the homepage main navigation is available
    When the user selects Connect from the header
    Then the destination path is "/contact/" with heading "Let's Connect"
