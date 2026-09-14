Feature: Base homepage without unsolicited modal

  Scenario: Base homepage loads without promotional modal
    Given Default homepage configuration
    When Page loads
    Then No unsolicited promotional modal appears on load

  Scenario: Campaign modal governed separately when enabled
    Given Campaign modal is configured and enabled
    When Page loads
    Then Modal only appears per configured activation rule

  Scenario: Configured modal dismissible
    Given Campaign modal appears
    When User clicks dismiss or close
    Then Modal closes immediately

  Scenario: Campaign modal keyboard accessible
    Given Campaign modal is open
    When User presses Tab
    Then Focus trapped within modal; close button reachable

  Scenario: Campaign modal non-blocking
    Given Campaign modal is open
    When User tries to interact with page behind
    Then Modal does not block page interaction inappropriately

  Scenario: Default state is disabled
    Given Configuration review
    When Checking campaign modal config
    Then Campaign modal enabled flag is false by default

  Scenario: Configured modal requires title content and dismiss
    Given Campaign modal configuration
    When Checking required fields
    Then Modal has title, content, dismiss control, and activation rule

  Scenario: Repeated modal after dismissal prevented
    Given User dismissed campaign modal
    When User continues browsing or returns
    Then Modal does not reappear without new session or explicit re-enable

  Scenario: Focus trap in modal works correctly
    Given Campaign modal open
    When Pressing Tab repeatedly
    Then Focus stays within modal; Escape or close button exits

  Scenario: Modal at small viewport usable
    Given Mobile viewport with campaign modal
    When Modal renders
    Then Modal fits viewport; scrollable if needed; dismiss button accessible

  Scenario: Modal with JavaScript disabled handled
    Given User has JavaScript disabled
    When Page loads
    Then Modal does not appear; page functions without JS

  Scenario: Campaign display dismiss logged with consent
    Given Campaign modal configured and consent given
    When Modal displays or dismisses
    Then Events logged per consent policy
