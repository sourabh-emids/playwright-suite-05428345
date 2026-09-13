Feature: Support Wistia embeds when configured

    @emids_lp_043
    Scenario: verify_no_unnecessary_wistia_script
        Given Homepage has no Wistia content configured
        When Page renders
        Then No Wistia player script is loaded unnecessarily

    @emids_lp_043
    Scenario: verify_wistia_player_accessible_title
        Given Wistia content is configured with video ID
        When Player renders
        Then Player has accessible title and controls

    @emids_lp_043
    Scenario: verify_video_id_required_when_enabled
        Given Wistia embed is configured
        When Automated check validates config
        Then Video ID is required when Wistia is enabled

    @emids_lp_043
    Scenario: verify_reduced_motion_autoplay_preferences
        Given User prefers reduced motion or has autoplay disabled
        When Wistia video attempts autoplay
        Then Autoplay preferences are respected

    @emids_lp_043
    Scenario: verify_player_blocked_handling
        Given Wistia player is blocked
        When Page renders
        Then Fallback or message shown; no critical errors

    @emids_lp_043
    Scenario: verify_no_consent_wistia_handling
        Given Consent is required for Wistia
        When Consent not given
        Then Wistia player does not load

    @emids_lp_043
    Scenario: verify_missing_video_handling
        Given Wistia video ID points to missing video
        When Player attempts to load
        Then Appropriate error handling or fallback
