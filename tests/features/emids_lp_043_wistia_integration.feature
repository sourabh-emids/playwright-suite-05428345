Feature: Support Wistia embeds only when configured

  Scenario: Verify no unnecessary script when Wistia not configured
    Given Homepage has no Wistia content configured
    When Page loads
    Then No Wistia player script is loaded

  Scenario: Verify player has accessible title/controls when configured
    Given Wistia content is configured with video ID and title
    When Player renders
    Then Player has accessible title and controls

  Scenario: Verify video ID required when enabled
    Given Wistia embed is enabled
    When Page renders
    Then Valid video ID is provided; invalid ID handled gracefully

  Scenario: Verify reduced motion/autoplay preferences respected
    Given User prefers reduced motion or has autoplay disabled
    When Wistia player loads
    Then Player respects user preferences; no unwanted autoplay

  Scenario: Verify player blocked handled
    Given Wistia player script is blocked
    When Page renders with Wistia content
    Then Fallback displayed; no page break

  Scenario: Verify no consent handling for Wistia
    Given Wistia embed is configured but consent not granted for media
    When Page renders
    Then Player loads only when applicable consent rules are satisfied

  Scenario: Verify missing video handled
    Given Wistia video ID does not exist or is removed
    When Player attempts to load
    Then Graceful error or placeholder displayed
