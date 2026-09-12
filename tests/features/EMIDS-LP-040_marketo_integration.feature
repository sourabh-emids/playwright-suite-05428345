Feature: Marketo integration with consent

  Scenario: Marketing scripts gated by consent
    Given Marketo integration configuration
    When Marketing consent has not been granted
    Then Marketing scripts do not execute

  Scenario: Page functional when Marketo unavailable
    Given Marketo script blocked or unavailable
    When Page renders
    Then Core page remains independent and functional

  Scenario: Configuration stored appropriately
    Given Marketo IDs and configuration
    When Configuration is reviewed
    Then No unknown Munchkin/Form IDs hardcoded

  Scenario: Script blocked handling
    Given Marketo script blocked by browser/ad blocker
    When Page loads
    Then Page remains functional
