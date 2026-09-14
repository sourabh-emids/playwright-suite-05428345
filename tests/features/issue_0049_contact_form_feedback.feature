Feature: Contact form submission feedback and retry

  Scenario: Submit enters pending state
    Given User clicks Submit
    When Submission in progress
    Then Button shows pending/loading state; disabled to prevent double submit

  Scenario: Duplicate activation prevented while pending
    Given Submit button in pending state
    When User clicks again
    Then Second click does not trigger another submission

  Scenario: Success announced accessibly
    Given Form submission succeeds
    When Success message displays
    Then Screen reader announces success via live region

  Scenario: Failure keeps user content for retry
    Given Form submission fails
    When Error displays
    Then User-entered content preserved; user can correct and resubmit

  Scenario: Server validation errors map to fields
    Given Server returns field-level errors
    When Error displays
    Then Error messages associated with relevant fields; not just general error

  Scenario: Timeout error handled
    Given Submission times out
    When User waits for response
    Then Timeout error shown; form data preserved

  Scenario: 4xx validation error handled
    Given Server returns 400 Bad Request
    When Form submission receives validation error
    Then User sees specific validation errors; form data preserved

  Scenario: 5xx vendor CRM outage handled
    Given Backend returns 500 error
    When User submits form
    Then User sees friendly error message; form data preserved for retry

  Scenario: User navigates away during submission
    Given Form submission in progress
    When User navigates away
    Then Browser warns user about pending submission if appropriate

  Scenario: Submission outcome logged
    Given Form submission completes
    When Logging submission result
    Then Outcome, timestamp, form ID, and correlation ID logged; not raw field values
