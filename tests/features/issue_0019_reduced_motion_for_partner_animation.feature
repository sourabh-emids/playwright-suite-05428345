Feature: Reduced motion for partner animation
  # issue_0019

  Scenario: Prefers-reduced-motion disables continuous motion
    Given User has prefers-reduced-motion enabled in system settings
    When The Partnerships section renders
    Then Continuous motion animations are disabled or meaningfully reduced

  Scenario: Content remains fully visible with reduced motion
    Given User has prefers-reduced-motion enabled
    When The Partnerships section renders
    Then All partner logos remain visible and discoverable without animation

  Scenario: Animation not required to discover partner
    Given User has prefers-reduced-motion enabled
    When The user views the Partnerships section
    Then All partner names and logos are visible in a static state

  Scenario: Preference change handled while page open
    Given The page is currently displayed
    When User changes system reduced motion preference
    Then Animation state updates without requiring page reload
