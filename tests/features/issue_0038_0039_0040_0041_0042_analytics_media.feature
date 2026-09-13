Feature: Analytics and media conditional loading

  Scenario: Analytics follows consent
    Given User is on Emids homepage
    When Analytics configuration initializes
    Then Analytics initialization follows consent state

  Scenario: Page view tracked with consent
    Given User has provided analytics consent
    When Page loads
    Then Page view is tracked

  Scenario: UTM parameters associated correctly
    Given User arrives with UTM parameters
    When Attribution is processed
    Then UTM source, medium, and campaign are associated appropriately

  Scenario: Marketing scripts gated by consent
    Given User has not provided marketing consent
    When Marketo scripts attempt to load
    Then Marketing scripts are gated and do not execute

  Scenario: Page functional when Marketo unavailable
    Given Marketo is unavailable
    When Page renders
    Then Page remains fully functional

  Scenario: LinkedIn tag gated by marketing consent
    Given Marketing consent not provided
    When LinkedIn tag attempts to execute
    Then LinkedIn tag does not execute before required marketing consent

  Scenario: Core page independent of LinkedIn
    Given LinkedIn tag fails or is blocked
    When Page renders
    Then Core page remains independent of LinkedIn tag status

  Scenario: Wistia player accessible when configured
    Given Wistia video is configured
    When Page renders
    Then Player has accessible title and controls

  Scenario: No player without YouTube embed
    Given No YouTube embed is configured
    When Page loads
    Then No YouTube player resources are required
