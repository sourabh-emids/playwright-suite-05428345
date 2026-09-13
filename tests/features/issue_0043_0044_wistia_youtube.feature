Feature: Wistia and YouTube embeds when configured

  Scenario: No player script without Wistia content
    Given No Wistia content is configured
    When Page loads
    Then No Wistia player script is loaded unnecessarily

  Scenario: Player accessible when configured
    Given Wistia video is configured
    When Page renders
    Then Player has accessible title and controls

  Scenario: Reduced motion respected for video
    Given User prefers reduced motion
    When Video plays
    Then Motion preferences are respected

  Scenario: No player without YouTube embed
    Given No YouTube embed is configured
    When Page loads
    Then No YouTube player resources are required

  Scenario: No autoplay with sound by default
    Given YouTube embed is configured
    When Video attempts to autoplay
    Then Autoplay does not occur with sound by default

  Scenario: Consent and privacy behavior for video
    Given YouTube embed is configured
    When User loads page
    Then Appropriate consent/privacy behavior is implemented
