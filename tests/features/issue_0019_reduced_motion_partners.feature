Feature: Reduced motion for partner animation

  Scenario: Prefers-reduced-motion disables non-essential motion
    Given User has prefers-reduced-motion enabled
    When Partner logo animation is active
    Then Non-essential continuous motion is disabled or meaningfully reduced

  Scenario: Content remains fully visible
    Given User has prefers-reduced-motion enabled
    When Partner logos animate
    Then All partner logos remain fully visible

  Scenario: Animation not required to discover partner
    Given Animation is disabled via reduced motion
    When User views partner logos
    Then All partners can be discovered without animation

  Scenario: Preference changes while page open
    Given Page is open and user changes motion preference
    When Preference change is detected
    Then Animation behavior updates accordingly

  Scenario: Animation library failure fallback
    Given Animation library fails
    When Page renders
    Then Static partner list remains visible
