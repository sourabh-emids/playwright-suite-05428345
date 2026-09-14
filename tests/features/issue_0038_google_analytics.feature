Feature: Support Google Analytics after consent

  Scenario: Analytics initializes following consent
    Given User grants analytics/statistics consent
    When Page loads
    Then Google Analytics initializes and begins collecting permitted data

  Scenario: Denial leaves page functional
    Given User denies analytics consent
    When Page loads and renders
    Then Page functions completely; no analytics collection occurs

  Scenario: Analytics events do not contain form field values
    Given Contact form is on page
    When Analytics events fire
    Then Event payloads do not include form field contents

  Scenario: Statistics consent required for analytics
    Given User has not granted statistics consent
    When Analytics attempts collection
    Then Collection does not occur

  Scenario: Page view event fires appropriately
    Given Page loads with analytics consent
    When Page finishes loading
    Then Page view event fires with appropriate data

  Scenario: Offline handling
    Given User is offline
    When Analytics attempts to send data
    Then No errors displayed to user; analytics queues or drops gracefully

  Scenario: Consent revoked handled
    Given User revokes analytics consent
    When Analytics attempts next collection
    Then Analytics respects revoked consent; stops collecting

  Scenario: Duplicate page view prevented
    Given Single page load scenario
    When Checking analytics page view count
    Then Single page view event fires per actual page load

  Scenario: Event properties sanitized
    Given Analytics event contains user input
    When Checking event payload
    Then Event properties are sanitized; no raw user content in payload
