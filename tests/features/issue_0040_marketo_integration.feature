Feature: Integrate Marketo with consent

  Scenario: Marketing scripts gated by consent
    Given User has not granted marketing consent
    When Page loads
    Then Marketo scripts do not load or execute

  Scenario: Page functional when Marketo unavailable
    Given Marketo script fails or blocked
    When Page renders
    Then Core content and functionality remain unaffected

  Scenario: Marketing consent required
    Given User denies marketing consent
    When Marketo attempts initialization
    Then Marketo does not initialize or track

  Scenario: Script blocked handled gracefully
    Given Marketo script blocked by browser
    When Page renders
    Then Page loads normally; blocked script handled without error to user

  Scenario: Vendor outage handled
    Given Marketo service unavailable
    When Page attempts Marketo integration
    Then Page remains functional; integration failure logged minimally

  Scenario: Consent revoked handled
    Given User revokes marketing consent
    When Marketo attempts tracking
    Then Marketo stops tracking; page unaffected

  Scenario: Integration logs sanitized
    Given Marketo integration error
    When Logging error
    Then Logs contain error codes/status, not raw lead data
