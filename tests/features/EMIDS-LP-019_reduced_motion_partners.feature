Feature: Reduced motion for partner animation

  Scenario: Reduced motion disables continuous motion
    Given User has prefers-reduced-motion enabled
    When Partner logo animation would run
    Then Non-essential continuous motion is disabled or meaningfully reduced

  Scenario: Content remains fully visible
    Given Reduced motion preference is active
    When Partner section renders
    Then All partner logos remain fully visible and discoverable

  Scenario: Animation not required to discover partner
    Given Static view of partner logos
    When All partners are inspected without animation
    Then All partners are discoverable without requiring animation

  Scenario: Preference changes while page open
    Given User changes reduced motion preference while page is open
    When Preference change is detected
    Then Animation state updates appropriately
