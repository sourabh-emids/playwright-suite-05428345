Feature: Respect reduced motion for partner animation

  Scenario: Reduced motion disables continuous motion
    Given User has prefers-reduced-motion: reduce enabled
    When Partner logos would animate continuously
    Then Animation is disabled or significantly reduced

  Scenario: Content remains fully visible with reduced motion
    Given Reduced motion is active
    When User views partner section
    Then All partner logos are visible in static display

  Scenario: Partner discoverable without animation
    Given User cannot see animation due to reduced motion
    When User attempts to view all partners
    Then All partners are visible in static view; animation not required to discover partner

  Scenario: Preference change during page visit handled
    Given User changes system reduced motion preference while page is open
    When System preference updates
    Then Page responds to preference change without reload

  Scenario: Animation library failure fallback
    Given Animation library fails to load or execute
    When Page renders
    Then Static partner logos display; page remains functional
