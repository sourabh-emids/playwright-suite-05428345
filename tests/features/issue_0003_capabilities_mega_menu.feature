"""Feature: Capabilities Mega-Menu Implementation."""
Feature: Capabilities Mega-Menu Implementation

  @issue_0003
  Scenario: capabilities_menu_opens_closes_predictably
    Given User is on page with header visible
    When User activates the Capabilities menu trigger
    Then Capabilities menu opens predictably; second activation closes it

  @issue_0003
  Scenario: capability_links_keyboard_operable
    Given Capabilities menu is open
    When User navigates via keyboard (Tab/Arrow)
    Then All capability links are keyboard operable

  @issue_0003
  Scenario: capability_labels_match_taxonomy
    Given Capabilities menu is rendered
    When Group labels are compared against approved taxonomy
    Then Labels show AI, Engineering, and Platforms matching approved taxonomy

  @issue_0003
  Scenario: unique_labels_within_menu
    Given Capabilities menu has multiple items
    When Labels are checked for uniqueness
    Then All labels are unique within the menu

  @issue_0003
  Scenario: capability_urls_resolve
    Given Capabilities menu shows links
    When User clicks any capability link
    Then All URLs resolve to valid destination pages

  @issue_0003
  Scenario: large_screen_mega_menu_layout
    Given Page is at desktop viewport
    When Capabilities menu opens
    Then Menu uses grouped mega-menu layout

  @issue_0003
  Scenario: small_screen_accessible_disclosure
    Given Page is at mobile viewport
    When Capabilities menu opens
    Then Menu uses accessible disclosure pattern

  @issue_0003
  Scenario: menu_overflow_handling
    Given Capability menu is open at narrow desktop width
    When Menu content exceeds container bounds
    Then Menu overflow is handled without breaking layout
