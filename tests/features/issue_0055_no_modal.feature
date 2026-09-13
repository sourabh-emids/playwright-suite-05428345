Feature: No promotional modal in base experience

  Scenario: Base homepage loads without unsolicited modal
    Given User navigates to homepage
    When Page loads
    Then No unsolicited promotional modal appears

  Scenario: Campaign modal requires explicit config
    Given Campaign modal is not configured
    When Page loads
    Then No modal displays

  Scenario: Campaign modal dismissible
    Given Campaign modal is configured and displays
    When User interacts with modal
    Then Modal is dismissible

  Scenario: Campaign modal keyboard accessible
    Given Campaign modal displays
    When User navigates with keyboard
    Then Modal is keyboard accessible

  Scenario: Campaign modal non-blocking
    Given Campaign modal displays
    When Modal is open
    Then Modal does not block core page interaction

  Scenario: Repeated modal after dismissal prevention
    Given User dismisses campaign modal
    When User continues browsing
    Then Modal does not repeatedly display

  Scenario: Focus trap in campaign modal
    Given Campaign modal opens
    When User presses Tab
    Then Focus remains within modal until dismissed

  Scenario: Small viewport modal handling
    Given Campaign modal displays at small viewport
    When Page renders
    Then Modal handles small viewport appropriately

  Scenario: JS disabled modal handling
    Given JavaScript is disabled
    When Page loads
    Then No modal appears (base experience)
