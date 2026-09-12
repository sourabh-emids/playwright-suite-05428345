"""Feature file for Issue 0055 - No base promotional modal on homepage."""
Feature: No base promotional modal on homepage

  Scenario: Base homepage loads without unsolicited modal
    Given A user loads the Emids homepage with no campaign modal configured
    When Page loads
    Then No promotional modal appears

  Scenario: Configured modal dismissible
    Given A campaign modal is configured and displays
    When User interacts with the modal
    Then Modal is dismissible via close button, Escape key, or overlay click

  Scenario: Configured modal keyboard accessible
    Given A campaign modal is configured and displays
    When User navigates with keyboard
    Then Modal focus is managed; close control is keyboard accessible

  Scenario: Configured modal non-blocking
    Given A campaign modal is configured and displays
    When Modal is open
    Then Modal is non-blocking; underlying content remains accessible

  Scenario: Default state is disabled
    Given No campaign modal is configured
    When Page loads
    Then No modal appears (default state is disabled)

  Scenario: Repeated modal after dismissal prevented
    Given User has dismissed a campaign modal
    When User reloads page or continues browsing
    Then Modal does not repeatedly appear after dismissal (session-based suppression)

  Scenario: Focus trap in modal
    Given Campaign modal is open
    When User tabs through modal
    Then Focus is trapped within modal until closed

  Scenario: Modal at small viewport
    Given Campaign modal displays at narrow viewport
    When Modal renders
    Then Modal is readable and functional at small viewport
