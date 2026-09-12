Feature: YouTube embeds conditional loading

  Scenario: No player resources without embed
    Given No YouTube embed configured
    When Page loads
    Then No YouTube player resources are required

  Scenario: Configured media keyboard accessible and titled
    Given YouTube embed is configured
    When Video renders
    Then Media is keyboard accessible and has title

  Scenario: Valid video ID
    Given YouTube configuration
    When Video ID is verified
    Then Video ID is valid

  Scenario: No autoplay with sound by default
    Given YouTube embed configuration
    When Autoplay is set
    Then Video does not autoplay with sound
