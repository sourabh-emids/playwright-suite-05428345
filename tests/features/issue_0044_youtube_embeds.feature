Feature: Support YouTube embeds when configured

  Scenario: No YouTube player when not configured
    Given Homepage has no YouTube content
    When Checking for YouTube resources
    Then No YouTube iframe or player script loaded

  Scenario: Configured media keyboard accessible and titled
    Given YouTube video is configured
    When Checking accessibility
    Then Video iframe has title attribute; keyboard navigation works

  Scenario: Valid video ID required
    Given YouTube is configured
    When Checking configuration
    Then Valid video ID present; invalid ID not causing errors

  Scenario: No autoplay with sound by default
    Given YouTube video configured
    When Page loads
    Then Video does not autoplay with sound; uses proper privacy-enhanced embed

  Scenario: Video removed handled
    Given YouTube video is deleted or private
    When Player loads
    Then Appropriate unavailable message or error shown

  Scenario: Regional restriction handled
    Given Video is regionally restricted
    When User attempts playback
    Then User sees appropriate restriction message

  Scenario: Cookies blocked handled
    Given User blocks third-party cookies
    When YouTube embed loads
    Then Embed uses privacy-enhanced mode; continues without blocking page

  Scenario: Optional play events under consent
    Given User consents to statistics
    When User plays YouTube video
    Then Play event tracked if permitted by consent
