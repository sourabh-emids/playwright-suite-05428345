Feature: Google Analytics measurement after consent

  Scenario: Analytics initialization follows consent
    Given User consent state
    When Page loads
    Then Analytics initializes only after appropriate consent

  Scenario: Denial leaves page functional
    Given Analytics consent denied
    When Page loads and user interacts
    Then Page remains fully functional

  Scenario: Events do not contain contact form values
    Given Analytics event payloads
    When Events are monitored
    Then Events do not contain contact form field values

  Scenario: Page view events fire correctly
    Given Page navigation
    When Page loads
    Then Page view event fires appropriately after consent

  Scenario: Consent revoked handling
    Given Consent revoked mid-session
    When Analytics events would fire
    Then Analytics respects consent change
