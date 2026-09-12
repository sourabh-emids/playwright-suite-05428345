Feature: Capabilities mega-menu implementation

  Scenario: Capabilities menu opens and closes predictably
    Given A user interacts with the Capabilities navigation item
    When The menu trigger is activated
    Then Menu opens displaying AI, Engineering, and Platforms capability groups with their child destinations

  Scenario: All capability links are keyboard operable
    Given The Capabilities menu is open
    When The user navigates via keyboard
    Then All capability links are reachable via Tab key and activate on Enter

  Scenario: Capability labels match approved taxonomy
    Given The Capabilities menu content
    When Labels are compared against approved site taxonomy
    Then AI, Engineering, and Platforms labels are consistent with content management

  Scenario: No duplicate labels within menu
    Given The Capabilities menu structure
    When Labels are inspected for uniqueness
    Then All labels within the menu are unique

  Scenario: Mobile disclosure pattern for Capabilities
    Given A user on a mobile device
    When The Capabilities menu is opened
    Then An accessible disclosure pattern is used instead of mega-menu
