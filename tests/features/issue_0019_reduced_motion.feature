"""Feature file for Issue 0019 - Reduced motion for partner animation."""
Feature: Reduced motion for partner animation

  Scenario: Reduced motion disables continuous motion
    Given A user has prefers-reduced-motion enabled
    When The user views the partner logo marquee
    Then Non-essential continuous motion is disabled or meaningfully reduced

  Scenario: Content remains fully visible
    Given A user has prefers-reduced-motion enabled
    When The user views the partner section
    Then All partner logos remain fully visible and discoverable

  Scenario: Animation not required to discover partner
    Given A user views the partner section without motion
    When The user examines all partners
    Then All partners are discoverable without requiring animation

  Scenario: Preference changes while page open
    Given A user changes prefers-reduced-motion setting while page is open
    When The preference change is detected
    Then Animation state updates to match new preference
