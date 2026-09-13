Feature: Support YouTube embeds when configured

    @emids_lp_044
    Scenario: verify_no_player_without_config
        Given Homepage has no YouTube embed configured
        When Page renders
        Then No YouTube player resources are required

    @emids_lp_044
    Scenario: verify_configured_media_keyboard_accessible
        Given YouTube embed is configured
        When Player renders
        Then Media is keyboard accessible with title

    @emids_lp_044
    Scenario: verify_valid_video_id
        Given YouTube embed has video ID
        When Automated check validates ID
        Then Video ID is valid format

    @emids_lp_044
    Scenario: verify_no_autoplay_with_sound
        Given YouTube video is configured
        When Page loads
        Then No autoplay with sound by default

    @emids_lp_044
    Scenario: verify_consent_privacy_behavior
        Given YouTube embed is configured
        When User interacts with embed
        Then Appropriate consent/privacy behavior is followed

    @emids_lp_044
    Scenario: verify_video_removed_handling
        Given YouTube video has been removed
        When Embed attempts to load
        Then Appropriate error or placeholder shown

    @emids_lp_044
    Scenario: verify_regional_restriction_handling
        Given YouTube video is regionally restricted
        When Embed attempts to load
        Then User sees appropriate message rather than broken player

    @emids_lp_044
    Scenario: verify_cookies_blocked_handling
        Given User has cookies blocked
        When YouTube embed loads
        Then Embed handles privacy-enhanced mode or shows fallback
