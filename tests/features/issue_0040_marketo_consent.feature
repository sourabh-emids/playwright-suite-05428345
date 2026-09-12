"""Feature file for Issue 0040 - Marketo integration with consent."""
Feature: Marketo integration with consent

  Scenario: Marketing scripts gated by consent
    Given User has not granted marketing consent
    When Page loads
    Then Marketing scripts (including Marketo) do not execute

  Scenario: Page functional when Marketo unavailable
    Given Marketo integration fails or is blocked
    When User navigates the page
    Then Page remains functional independent of Marketo availability

  Scenario: Marketing consent required
    Given User has not provided marketing consent
    When Marketo attempts to initialize
    Then Marketo marketing integration does not activate

  Scenario: Script blocked handling
    Given Marketo script is blocked (ad blocker, CSP, etc.)
    When Page loads
    Then Core functionality remains unaffected

  Scenario: Consent revoked handling
    Given User revokes marketing consent
    When Consent change is processed
    Then Marketo integration stops; no further marketing tracking occurs
