Feature: Define homepage modal behavior as none required by base experience

  Scenario: Verify base homepage loads without unsolicited modal
    Given User loads the base homepage with no campaign modal configured
    When Page finishes loading
    Then No promotional modal appears automatically

  Scenario: Verify configured campaign modal is dismissible
    Given Campaign modal is configured and triggers
    When Modal displays
    Then User can dismiss the modal via close button, clicking outside, or pressing Escape

  Scenario: Verify campaign modal is keyboard accessible
    Given Campaign modal is open
    When User navigates via keyboard
    Then Modal focus is managed; close control is keyboard accessible

  Scenario: Verify campaign modal is non-blocking
    Given Campaign modal is open
    When User attempts to interact with page content behind modal
    Then Modal does not block interaction with underlying page elements inappropriately

  Scenario: Verify default state is disabled
    Given No campaign modal is configured
    When Homepage loads
    Then Default behavior is no modal; no modal code executes

  Scenario: Verify repeated modal after dismissal handled
    Given User dismisses campaign modal
    When User continues browsing
    Then Modal does not repeatedly appear unless intentionally re-triggered by configured rules

  Scenario: Verify focus trap in modal if present
    Given Campaign modal is open
    When User tabs through modal
    Then Focus remains trapped within modal until dismissed

  Scenario: Verify small viewport modal handled
    Given Campaign modal displays on small viewport
    When Modal renders
    Then Modal is appropriately sized; does not overflow viewport

  Scenario: Verify JS disabled modal behavior
    Given User has JavaScript disabled
    When Homepage loads with no campaign modal configured
    Then Page renders normally; no modal-related functionality breaks
