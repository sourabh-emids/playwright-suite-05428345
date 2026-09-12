Feature: Wistia embeds conditional loading

  Scenario: No Wistia script without configuration
    Given No Wistia content configured for homepage
    When Page loads
    Then No unnecessary Wistia player script is loaded

  Scenario: Configured video has accessible controls
    Given Wistia video is configured
    When Video renders
    Then Player has accessible title and controls

  Scenario: Reduced motion and autoplay preferences respected
    Given Wistia video configuration
    When User prefers reduced motion or autoplay is set
    Then Preferences are respected

  Scenario: Video ID required when enabled
    Given Wistia configuration
    When Video is enabled
    Then Video ID is present and valid
