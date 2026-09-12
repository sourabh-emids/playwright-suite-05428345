"""Feature file for Issue 0038 - Google Analytics measurement post-consent."""
Feature: Google Analytics measurement post-consent

  Scenario: Analytics initialization follows consent
    Given User has not provided statistics consent
    When Analytics script attempts to initialize
    Then Analytics initialization respects consent and does not track without permission

  Scenario: Analytics denial leaves page functional
    Given User denies analytics consent
    When User navigates the page
    Then Page remains fully functional with all features accessible

  Scenario: Events do not contain contact-form field values
    Given User fills out contact form
    When Analytics events are sent
    Then Event payloads do not contain contact form field values (email, name, etc.)

  Scenario: Statistics consent required
    Given User has not granted statistics consent
    When Analytics attempts to track
    Then Tracking does not occur

  Scenario: Consent revoked handling
    Given User revokes analytics consent mid-session
    When Consent change is processed
    Then Analytics tracking stops; subsequent events are not sent
