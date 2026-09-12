Feature: LinkedIn marketing tags conditional integration

  Scenario: LinkedIn tag respects marketing consent
    Given LinkedIn marketing tag configuration
    When Marketing consent not granted
    Then LinkedIn tag does not execute

  Scenario: Core page independent of LinkedIn
    Given LinkedIn tag blocked or unavailable
    When Page loads
    Then Core functionality unaffected

  Scenario: Marketing consent required
    Given LinkedIn tag execution
    When Consent is checked
    Then Marketing consent is required before execution
