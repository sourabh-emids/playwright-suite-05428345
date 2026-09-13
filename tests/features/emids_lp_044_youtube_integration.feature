Feature: Support YouTube embeds only when configured

  Scenario: Verify no player resources when not configured
    Given Homepage has no YouTube embed configured
    When Page loads
    Then No YouTube player resources are loaded

  Scenario: Verify configured media keyboard accessible
    Given YouTube embed is configured
    When User navigates via keyboard
    Then Player is keyboard accessible with proper focus management

  Scenario: Verify configured media titled
    Given YouTube embed is configured
    When Player renders
    Then Player has accessible title attribute

  Scenario: Verify valid video ID required
    Given YouTube embed is configured
    When Page renders
    Then Valid video ID is used; invalid ID shows appropriate error

  Scenario: Verify no autoplay with sound by default
    Given YouTube embed is configured
    When Player initializes
    Then Video does not autoplay with sound by default

  Scenario: Verify video removed handled
    Given YouTube video is deleted or made private
    When Player attempts to load
    Then Graceful error displayed; no page break

  Scenario: Verify regional restriction handled
    Given YouTube video is region-restricted
    When User attempts to play
    Then Appropriate message displayed

  Scenario: Verify cookies blocked handled
    Given User blocks third-party cookies
    When YouTube player loads
    Then Player loads in privacy-enhanced mode or shows appropriate message
