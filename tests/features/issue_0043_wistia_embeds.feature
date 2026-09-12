"""Feature file for Issue 0043 - Wistia embeds conditional loading."""
Feature: Wistia embeds conditional loading

  Scenario: No unnecessary Wistia script when not configured
    Given Homepage variant has no Wistia content configured
    When Page loads
    Then No unnecessary Wistia player script is loaded

  Scenario: Wistia player accessible with content configured
    Given Wistia content is configured for the variant
    When Player loads
    Then Player has accessible title/controls

  Scenario: Reduced motion/autoplay preferences respected
    Given User has prefers-reduced-motion or autoplay settings configured
    When Wistia video loads
    Then Video respects reduced motion preferences; no autoplay with sound by default

  Scenario: Player blocked handling
    Given Wistia player is blocked
    When Page loads
    Then Core content remains functional

  Scenario: No consent handling
    Given Required consent for media embedding is not granted
    When Page loads
    Then Media does not auto-load; consent-gated loading is enforced
