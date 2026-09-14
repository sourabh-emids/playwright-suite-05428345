"""Feature: Company Navigation Group."""
Feature: Company Navigation Group

  @issue_0006
  Scenario: company_menu_exposes_approved_links
    Given Company menu is open
    When User views navigation items
    Then Menu exposes only approved company links

  @issue_0006
  Scenario: company_menu_keyboard_pointer_touch
    Given Company menu is rendered
    When User interacts via keyboard, pointer, or touch
    Then Menu works with all interaction methods

  @issue_0006
  Scenario: company_contact_connect_destinations
    Given Company menu is open
    When User navigates to contact-related destinations
    Then Contact/Connect destinations route correctly

  @issue_0006
  Scenario: company_no_unpublished_pages
    Given Company navigation is configured
    When Menu renders
    Then Only published pages appear in the menu

  @issue_0006
  Scenario: company_focus_trap_handling
    Given Company menu is open
    When User navigates via keyboard
    Then Focus does not trap unexpectedly within menu
