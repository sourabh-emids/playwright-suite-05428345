@tc_02
Feature: TC-02 Main navigation

  Scenario Outline: Main navigation opens the correct page
    Given the Emids homepage and main navigation are available
    When the user opens "<menu>" and selects "<destination>"
    Then "<path>" is displayed with the heading "<heading>"

    Examples:
      | menu         | destination     | path                            | heading                                  |
      | Solutions    | Solutions       | /solutions/                     | Solutions                                |
      | Capabilities | Data Engineering| /capabilities/data-engineering/ | Data Engineering                         |
      | Industries   | Payer           | /segments/payer/                | Transforming Payer Operations            |
      | Insights     | Insights Hub    | /insights/                      | The intelligence behind the outcomes.    |
      | Company      | Our Story       | /about-us/                      | About Us                                 |
