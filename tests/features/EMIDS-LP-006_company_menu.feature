Feature: Company navigation group implementation

  Scenario: Company menu exposes approved links
    Given The Company menu is opened
    When All menu items are reviewed
    Then Only approved company links and Contact/Connect destinations are present

  Scenario: Company menu works with all input methods
    Given The Company menu is open
    When User interacts via keyboard, pointer, or touch
    Then All links are operable with each input method

  Scenario: Only published pages in Company menu
    Given Company navigation items
    When Checking publication status
    Then Only pages with published status are displayed
