Feature: Support Wistia embeds when configured

  Scenario: No Wistia script loaded when not configured
    Given Homepage has no Wistia content configured
    When Checking network requests
    Then No Wistia player script is loaded

  Scenario: Wistia player has accessible title and controls
    Given Wistia video is configured and renders
    When Checking accessibility
    Then Video has descriptive title; player controls are keyboard accessible

  Scenario: Video ID required when enabled
    Given Wistia is enabled but missing video ID
    When Page renders
    Then Video does not render; configuration error logged

  Scenario: Reduced motion and autoplay preferences respected
    Given User has prefers-reduced-motion
    When Wistia video configured with autoplay
    Then Autoplay does not occur; user controls playback

  Scenario: Player blocked handled gracefully
    Given Wistia domain blocked
    When Video renders
    Then Fallback or placeholder displays; no blocking error to user

  Scenario: No consent handled
    Given Video requires consent but not granted
    When Video configured
    Then Video does not load until consent provided

  Scenario: Missing video handled
    Given Wistia video ID points to deleted video
    When Player attempts to load
    Then Appropriate error or placeholder shown

  Scenario: Optional play events with consent
    Given User consents to analytics
    When User plays Wistia video
    Then Play event may be tracked per consent
