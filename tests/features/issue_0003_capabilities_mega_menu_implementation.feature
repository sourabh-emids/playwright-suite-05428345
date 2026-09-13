Feature: Capabilities mega-menu implementation
  # issue_0003

  Scenario: Capabilities menu opens predictably
    Given A user focuses on the Capabilities navigation item
    When The user activates the trigger
    Then The menu opens displaying AI, Engineering, and Platforms capability groups with their child destinations

  Scenario: All capability links are keyboard operable
    Given The Capabilities menu is open
    When The user navigates using Tab and Arrow keys
    Then All capability links within all groups are keyboard accessible

  Scenario: Capability labels match approved taxonomy
    Given The Capabilities menu displays group headings
    When Automated testing verifies labels against CMS taxonomy
    Then Labels (AI, Engineering, Platforms) match the approved site taxonomy exactly

  Scenario: Labels are unique within menu
    Given The Capabilities menu is rendered
    When Automated testing checks for duplicate labels
    Then All capability labels are unique within the menu structure

  Scenario: Mobile Capabilities uses accessible disclosure
    Given A user is on a mobile viewport
    When The user expands the Capabilities menu
    Then An accessible disclosure pattern provides equivalent access to all capability groups
