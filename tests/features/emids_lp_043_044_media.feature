"""Feature: Media embeds conditional (emids_lp_043-044)."""
Feature: Media embeds conditional

    @emids_lp_043 @media
    Scenario: No Wistia script when not configured
        Given No Wistia content configured
        When Page loads
        Then No Wistia player script loaded
        And No unnecessary resources

    @emids_lp_043 @media @accessibility
    Scenario: Configured Wistia player accessible
        Given Wistia video is configured
        When Player loads
        Then Player has accessible title
        And Controls are keyboard accessible

    @emids_lp_043 @media @reduced-motion
    Scenario: Reduced motion and autoplay preferences respected
        Given User has prefers-reduced-motion or autoplay preference
        When Wistia video configured
        Then Autoplay behavior respects user preferences

    @emids_lp_044 @media
    Scenario: No YouTube when not configured
        Given No YouTube embed configured
        When Page loads
        Then No YouTube player resources required
        And Minimal page load

    @emids_lp_044 @media @accessibility
    Scenario: Configured media keyboard accessible
        Given YouTube video is configured
        When Player loads
        Then Player is keyboard accessible
        And Has meaningful title

    @emids_lp_044 @media
    Scenario: No autoplay with sound by default
        Given YouTube embed configured
        When Page loads
        Then Video does not autoplay with sound
        And Appropriate poster or start behavior
