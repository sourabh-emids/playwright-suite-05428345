"""Feature file for Issue 0006 - Company navigation group implementation."""
Feature: Company navigation group implementation

  Scenario: Company menu exposes approved links
    Given A user has the Company menu open
    When The user examines the menu content
    Then Only published company information and contact-related destinations are displayed

  Scenario: Company menu works across input methods
    Given A user is viewing the Company menu
    When The user interacts via keyboard, pointer, and touch
    Then The menu functions correctly with all interaction methods

  Scenario: Unpublished page not in Company menu
    Given A company page has been unpublished
    When A user views the Company menu
    Then The unpublished page is not visible in the menu

  Scenario: Company menu no focus trap
    Given A user has the Company menu open
    When The user tabs through the menu
    Then Focus does not become trapped within the menu
