Feature: Integrate Marketo with consent

  Scenario: Verify marketing scripts gated by consent
    Given Marketo integration is configured
    When Page loads without marketing consent
    Then Marketing scripts do not execute

  Scenario: Verify page remains functional when Marketo unavailable
    Given Marketo script fails or is unavailable
    When Page loads and renders
    Then Page remains fully functional without Marketo

  Scenario: Verify marketing consent required
    Given Marketo integration is configured
    When User has not granted marketing consent
    Then Marketo scripts and tracking do not activate

  Scenario: Verify script blocked handled
    Given Marketo script is blocked by browser/extension
    When Page loads
    Then Page remains functional; integration failure handled gracefully

  Scenario: Verify vendor outage handled
    Given Marketo service is experiencing outage
    When Page loads
    Then Core functionality remains unaffected; integration errors logged minimally

  Scenario: Verify consent revoked handled
    Given User previously granted marketing consent
    When User revokes consent
    Then Marketo tracking stops; page remains functional

  Scenario: Verify no raw lead data logged
    Given Marketo integration events occur
    When Errors or status is logged
    Then Only integration status/error codes are logged; no raw lead data
