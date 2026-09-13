Feature: Support Google Analytics measurement after consent

  Scenario: Verify analytics follows consent
    Given Google Analytics is configured
    When Page loads with user consent
    Then Analytics initializes and begins measurement per consent

  Scenario: Verify denial leaves page unaffected
    Given User denies analytics consent
    When Page loads
    Then Page remains fully functional without analytics tracking

  Scenario: Verify events contain no contact form field values
    Given Analytics events are configured
    When Events fire (page view, CTA clicks, content interactions)
    Then Events do not contain contact form field values or personal data

  Scenario: Verify statistics consent required
    Given Analytics tracking is requested
    When User has not granted statistics consent
    Then Analytics does not track user activity

  Scenario: Verify offline handling
    Given User is offline
    When Page loads with analytics
    Then Page functions normally; analytics queues or fails silently

  Scenario: Verify consent revoked handled
    Given User previously granted analytics consent
    When User revokes consent
    Then Analytics stops tracking; page remains functional

  Scenario: Verify no duplicate page-view events
    Given Page loads and user navigates
    When Analytics tracks page views
    Then Page views fire exactly once per navigation; no duplicates

  Scenario: Verify event properties sanitized
    Given Analytics events include properties
    When Events fire
    Then Event properties are sanitized; no sensitive data included
