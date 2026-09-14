Feature: Implement Capabilities mega-menu

  Scenario: Capabilities menu opens predictably
    Given User is on desktop with header visible
    When User activates the Capabilities navigation item
    Then Capabilities menu opens with AI, Engineering, and Platforms groups visible

  Scenario: All capability links are keyboard operable
    Given Capabilities menu is open
    When User navigates using Tab and Arrow keys
    Then All capability links are reachable and activatable via keyboard

  Scenario: Capability labels match approved taxonomy
    Given Capabilities menu is open
    When User compares menu labels to approved site taxonomy
    Then Labels match the content-managed taxonomy exactly

  Scenario: Capability group labels are unique within menu
    Given Capabilities menu is open
    When User checks for duplicate labels
    Then AI, Engineering, and Platforms labels are each unique within the menu

  Scenario: Mobile capabilities uses accessible disclosure
    Given User is on mobile device
    When User expands Capabilities section
    Then Accessible disclosure pattern is used matching other mobile menus

  Scenario: Capability links resolve to valid URLs
    Given Capabilities menu is open
    When User clicks child capability links
    Then Each link resolves to a valid destination URL

  Scenario: Menu handles overflow on smaller screens
    Given User has reduced viewport height
    When Capabilities menu opens
    Then Menu content is accessible via scrolling if needed without breaking layout
