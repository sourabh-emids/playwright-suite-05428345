"""Feature: Respect reduced motion for partner animation (emids_lp_019)."""
Feature: Respect reduced motion for partner animation

    @emids_lp_019 @partnerships @reduced-motion
    Scenario: Reduced motion disables non-essential motion
        Given User has prefers-reduced-motion: reduce
        When Page loads partner section
        Then Continuous motion animation is disabled or meaningfully reduced

    @emids_lp_019 @partnerships @reduced-motion
    Scenario: Content fully visible with motion disabled
        Given Animation is reduced or disabled
        When User views partner section
        Then All partner logos remain fully visible
        And Content is not lost

    @emids_lp_019 @partnerships
    Scenario: Animation not required for content discovery
        Given Animation fails or is disabled
        When User views partner section
        Then All partners are visible without animation
        And Animation is not required

    @emids_lp_019 @partnerships @reduced-motion
    Scenario: Preference changes while page open
        Given Page is loaded and animation is running
        When User toggles prefers-reduced-motion preference
        Then Animation adjusts in real-time to new preference

    @emids_lp_019 @partnerships
    Scenario: Animation library failure fallback
        Given Animation library fails to load
        When Page renders partner section
        Then Partners display in static fallback
        And No broken state
