Feature: Script failure graceful handling

  Scenario: Header readable when third-party scripts fail
    Given Optional third-party scripts fail
    When Page renders
    Then Header remains readable and functional

  Scenario: Main content accessible without scripts
    Given Third-party script failures
    When Page renders
    Then Main content remains accessible

  Scenario: CTAs functional without optional scripts
    Given Call-to-action buttons
    When Optional scripts fail
    Then CTAs remain functional

  Scenario: Footer navigable without scripts
    Given Footer section
    When Optional scripts fail
    Then Footer remains navigable

  Scenario: Errors are contained
    Given Script failure scenarios
    When Errors occur
    Then Errors do not cascade to break core functionality

  Scenario: CSP block handling
    Given Content Security Policy blocks script
    When Page loads
    Then Core functionality continues

  Scenario: Ad blocker interference
    Given Ad blocker blocks scripts
    When Page renders
    Then Core page remains functional
