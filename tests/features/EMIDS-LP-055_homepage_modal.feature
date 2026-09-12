Feature: Homepage modal behavior baseline

  Scenario: Base homepage loads without unsolicited modal
    Given Default homepage configuration
    When Page loads
    Then No promotional modal appears unsolicited

  Scenario: Configured modal is dismissible
    Given Campaign modal is configured and triggered
    When User interacts with modal
    Then Modal is dismissible via close control

  Scenario: Configured modal keyboard accessible
    Given Campaign modal when displayed
    When Keyboard interaction is tested
    Then Modal is keyboard accessible

  Scenario: Modal is non-blocking
    Given Campaign modal is displayed
    When Modal is open
    Then Modal does not block access to page content

  Scenario: Repeated modal after dismissal
    Given Campaign modal dismissed by user
    When User continues browsing
    Then Modal does not reappear immediately without appropriate trigger

  Scenario: JS disabled modal fallback
    Given JavaScript disabled
    When Page loads
    Then Base page functions; conditional modals do not break page
