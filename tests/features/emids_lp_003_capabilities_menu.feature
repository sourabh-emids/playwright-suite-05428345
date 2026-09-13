Feature: Implement Capabilities mega-menu

  Scenario: Verify Capabilities menu opens and closes predictably
    Given The user is on the homepage
    When The user activates the Capabilities navigation control
    Then The menu opens and displays AI, Engineering, and Platforms capability groups with child destinations

  Scenario: Verify all capability links are keyboard operable
    Given The Capabilities menu is open
    When The user navigates using keyboard alone
    Then All capability links including AI, Engineering, Platforms, and child links are operable via keyboard

  Scenario: Verify labels match approved site taxonomy
    Given The Capabilities menu is open
    When The user compares menu labels to approved taxonomy
    Then Labels for AI, Engineering, and Platforms match content-managed terminology exactly

  Scenario: Verify labels are unique within menu
    Given The Capabilities menu is open
    When The user checks for duplicate labels
    Then All capability labels are unique within the menu

  Scenario: Verify URLs resolve correctly
    Given The Capabilities menu is open
    When The user clicks each capability link
    Then All capability destination URLs resolve successfully without 404 errors

  Scenario: Verify menu overflow handled gracefully
    Given The user is on a viewport with limited height
    When The Capabilities menu opens
    Then Menu content scrolls or repositions without clipping critical content
