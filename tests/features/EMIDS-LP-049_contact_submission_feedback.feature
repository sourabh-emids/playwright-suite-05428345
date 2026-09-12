Feature: Contact form submission feedback and retry

  Scenario: Submit enters pending state
    Given User submits contact form
    When Submission is initiated
    Then UI enters pending state

  Scenario: Duplicate activation prevented while pending
    Given Form in pending state
    When Submit is clicked again
    Then Duplicate activation is prevented

  Scenario: Success announced accessibly
    Given Successful form submission
    When Success occurs
    Then Success is announced via accessible live region

  Scenario: Failure keeps user content for retry
    Given Failed form submission
    When Error occurs
    Then User-entered content is preserved for retry

  Scenario: Server validation errors map to fields
    Given Server-side validation error response
    When Error is returned
    Then Errors map to relevant fields where possible

  Scenario: 5xx vendor/CRM outage handling
    Given Backend vendor outage
    When Submission is attempted
    Then User receives error and can retry
