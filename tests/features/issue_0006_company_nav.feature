Feature: Implement Company navigation group

  Scenario: Company menu exposes approved links
    Given User activates the Company navigation item
    When Menu opens
    Then Only published and approved company links are displayed

  Scenario: Company menu works with keyboard, pointer, and touch
    Given User is testing accessibility
    When User navigates Company menu using keyboard, mouse, and touch
    Then Menu functions correctly with all input methods

  Scenario: Company menu consistent behavior with other header groups
    Given User compares Company menu to Solutions or Capabilities menu
    When Testing interaction patterns
    Then Company menu opens, navigates, and closes with the same behavior as other primary navigation groups

  Scenario: No focus trap in Company menu
    Given Company menu is open
    When User presses Tab repeatedly
    Then User can exit menu; focus does not get trapped within menu

  Scenario: Company menu handles redirect loop gracefully
    Given A company link destination has redirect loop
    When User clicks that link
    Then Page either loads with warning or link is not rendered to prevent infinite loop
