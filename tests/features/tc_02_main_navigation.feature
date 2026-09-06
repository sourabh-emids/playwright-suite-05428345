@TC-02
Feature: Main navigation opens the correct pages
  Each desktop main navigation menu should open a matching destination.

  Scenario Outline: Open a destination from each main navigation menu
    Given the Emids desktop main navigation is available
    When I open the "<destination>" destination from the "<menu>" main navigation menu
    Then the "<heading>" destination page for "<destination>" is displayed

    Examples:
      | menu         | destination         | heading                          |
      | Solutions    | Solutions           | Solutions                        |
      | Capabilities | Digital Engineering | Digital Engineering              |
      | Industries   | Payer               | Transforming Payer Operations    |
      | Insights     | Insights Hub        | The intelligence behind the outcomes. |
      | Company      | Our Story           | About Us                         |
