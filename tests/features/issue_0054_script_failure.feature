Feature: Script failure resilience

  Scenario: Header readable when analytics fails
    Given Analytics scripts fail
    When Page renders
    Then Header remains readable and functional

  Scenario: Main content readable when consent fails
    Given Consent scripts fail
    When Page renders
    Then Main content remains readable

  Scenario: CTAs functional when media fails
    Given Media scripts fail
    When Page renders
    Then CTAs remain functional

  Scenario: Footer navigable when marketing fails
    Given Marketing scripts fail
    When Page renders
    Then Footer remains navigable

  Scenario: Errors contained
    Given Optional integration fails
    When Error occurs
    Then Error does not break core functionality

  Scenario: CSP block handling
    Given Content Security Policy blocks script
    When Page loads
    Then Core functionality remains intact

  Scenario: DNS failure handling
    Given DNS resolution fails for third-party
    When Page loads
    Then Core functionality remains intact

  Scenario: Ad blocker handling
    Given Ad blocker blocks third-party script
    When Page loads
    Then Core functionality remains intact

  Scenario: Timeout handling
    Given Third-party script times out
    When Page loads
    Then Core functionality remains intact

  Scenario: Malformed vendor script handling
    Given Vendor script is malformed
    When Page loads
    Then Core functionality remains intact
