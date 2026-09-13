Feature: Respect reduced motion for partner animation

  Scenario: Verify reduced motion disables animation
    Given User has prefers-reduced-motion enabled
    When Page loads with partner animation
    Then Non-essential continuous motion is disabled or meaningfully reduced

  Scenario: Verify content remains fully visible
    Given User prefers reduced motion
    When Animation is disabled
    Then All partner content remains fully visible and accessible

  Scenario: Verify animation not required to discover partner
    Given User prefers reduced motion and views partners
    When Animation is disabled
    Then All partners are visible without requiring animation to view content

  Scenario: Verify preference changes while page open
    Given Page is loaded and user changes motion preference mid-session
    When User enables or disables reduced motion
    Then Animation state updates without page reload

  Scenario: Verify animation library failure handled
    Given Animation library fails to load
    When Page renders
    Then Partners render in static fallback layout
