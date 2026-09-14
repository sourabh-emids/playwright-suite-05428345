"""Feature: Reduced Motion for Partner Animation."""
Feature: Reduced Motion for Partner Animation

  @issue_0019
  Scenario: reduced_motion_disables_continuous_motion
    Given User has prefers-reduced-motion: reduce enabled
    When Page renders with animated partner logos
    Then Continuous motion is disabled or meaningfully reduced

  @issue_0019
  Scenario: content_visible_when_motion_disabled
    Given Animation is disabled via reduced motion preference
    When Partner logos render
    Then All content remains fully visible

  @issue_0019
  Scenario: animation_not_required_for_discovery
    Given Animation is required for loop display
    When User views partner logos
    Then All partners can be discovered without animation

  @issue_0019
  Scenario: preference_change_while_page_open
    Given Page is open and user changes motion preference mid-session
    When Preference change is detected
    Then Animation state updates appropriately

  @issue_0019
  Scenario: animation_library_failure
    Given Animation library fails to load
    When Partner section renders
    Then Static fallback renders without errors
