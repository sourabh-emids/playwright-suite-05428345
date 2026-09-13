Feature: Respect reduced motion for partner animation

    @emids_lp_019
    Scenario: verify_reduced_motion_disables_animation
        Given User has prefers_reduced_motion enabled
        When Page renders with animated partner logos
        Then Non-essential continuous motion is disabled or meaningfully reduced

    @emids_lp_019
    Scenario: verify_content_fully_visible
        Given Reduced motion is active
        When Partner logos render
        Then All partner content remains fully visible (not hidden by stopping animation)

    @emids_lp_019
    Scenario: verify_animation_not_required_to_discover
        Given Animation is running or stopped
        When User views partners
        Then Partner content does not require animation to be discovered

    @emids_lp_019
    Scenario: verify_preference_changes_while_page_open
        Given Page is loaded and user changes motion preference
        When System preference changes
        Then Animation adjusts accordingly without page reload

    @emids_lp_019
    Scenario: verify_animation_library_failure
        Given Animation library fails to load
        When Partner section renders
        Then Static fallback is shown; content remains accessible
