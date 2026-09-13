Feature: Provide contact-form submission feedback and retry behavior

  Scenario: Verify submit enters pending state
    Given User clicks submit button
    When Form begins processing
    Then Button enters disabled/loading state; clear pending indication shown

  Scenario: Verify duplicate activation prevented
    Given Form is in pending/submitting state
    When User clicks submit again
    Then Duplicate activation is prevented; button remains disabled

  Scenario: Verify success announced
    Given Form submission succeeds
    When Success response received
    Then Success message is announced via accessible live region or focus management

  Scenario: Verify failure keeps user content
    Given Form submission fails
    When Error is displayed
    Then User-entered content remains in fields; user can correct and retry

  Scenario: Verify retry permitted
    Given Form submission has failed
    When User corrects errors
    Then User can submit again successfully

  Scenario: Verify 4xx validation errors mapped to fields
    Given Server returns 4xx validation error
    When Response is received
    Then Field-level errors map to specific fields where possible

  Scenario: Verify 5xx outage handled
    Given Server returns 5xx error or CRM is unavailable
    When Submission fails with 5xx
    Then User-friendly error displayed; content preserved; retry option available

  Scenario: Verify timeout handled
    Given Submission times out
    When Timeout occurs
    Then User notified; content preserved; retry available

  Scenario: Verify user navigates away handled
    Given User submits form and then navigates away
    When Submission outcome is pending
    Then User is warned if in-flight submission will be lost

  Scenario: Verify no PII in logs
    Given Submission result is logged
    When Server logs outcome
    Then Only outcome, timestamp, form ID, and correlation ID logged; no full message or unnecessary PII
