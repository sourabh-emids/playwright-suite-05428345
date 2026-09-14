Feature: Handle script failures without breaking content

  Scenario: Header readable when optional scripts fail
    Given Optional third-party script fails
    When Page renders
    Then Header remains visible and functional

  Scenario: Main content readable when scripts fail
    Given Optional script fails to load
    When Page renders
    Then Main content area remains accessible and functional

  Scenario: CTAs functional when scripts fail
    Given Optional analytics script fails
    When Page renders
    Then All CTAs remain clickable and navigate correctly

  Scenario: Footer navigable when scripts fail
    Given Script fails during page load
    When Page renders
    Then Footer content fully accessible

  Scenario: Errors contained to failing integration
    Given Third-party script throws error
    When Page processes
    Then Error does not propagate to break core functionality

  Scenario: CSP block handled gracefully
    Given Content Security Policy blocks script
    When Page renders
    Then Core functionality unaffected; blocked script handled

  Scenario: DNS failure for vendor handled
    Given Third-party domain DNS fails
    When Page renders
    Then Core content loads; vendor failure logged

  Scenario: Ad blocker blocking vendor handled
    Given Ad blocker prevents vendor script
    When Page renders
    Then Core functionality unaffected

  Scenario: Vendor timeout handled
    Given Third-party script times out
    When Page renders
    Then Core content loads; timeout logged

  Scenario: Malformed vendor script handled
    Given Third-party script has syntax error
    When Browser parses script
    Then Error caught; core functionality preserved

  Scenario: Error logs sanitized
    Given Script error occurs
    When Logging error
    Then Logs contain sanitized error info; no stack traces with user content
