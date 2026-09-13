Feature: Company navigation group
  # issue_0006

  Scenario: Company menu works with all input methods
    Given A user navigates to the Company menu
    When The user activates the menu using keyboard, pointer, or touch
    Then The menu opens and displays approved company links and contact destinations

  Scenario: Only published pages appear in Company menu
    Given The Company menu is rendered
    When Automated testing validates destination URLs
    Then All links point to currently published pages with valid HTTP status
