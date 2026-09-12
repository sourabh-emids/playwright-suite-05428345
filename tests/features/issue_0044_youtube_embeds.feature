"""Feature file for Issue 0044 - YouTube embeds conditional loading."""
Feature: YouTube embeds conditional loading

  Scenario: No player resources when not configured
    Given Homepage variant has no YouTube embed configured
    When Page loads
    Then No YouTube player resources are required

  Scenario: Configured media keyboard accessible and titled
    Given YouTube embed is configured
    When User views the video
    Then Video is keyboard accessible and has appropriate title/aria-label

  Scenario: No autoplay with sound by default
    Given YouTube embed is configured
    When Page loads
    Then Video does not autoplay with sound

  Scenario: Video removed handling
    Given YouTube video has been removed
    When User attempts to view the video
    Then Appropriate error handling or fallback is displayed

  Scenario: Regional restriction handling
    Given YouTube video is regionally restricted
    When User attempts to view the video
    Then Appropriate handling occurs without breaking page
