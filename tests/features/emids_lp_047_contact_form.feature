Feature: Provide contact form reached by Connect CTAs

  Scenario: Verify all required fields displayed
    Given Contact form renders at /contact/
    When User views the form
    Then All fields display: First Name, Last Name, Work Email Address, Company Name, Title, Phone Number, Inquiry Type, Comments

  Scenario: Verify labels associated with controls
    Given Contact form renders
    When Screen reader reads form
    Then Each label is programmatically associated with its control

  Scenario: Verify clear success feedback
    Given User submits contact form with valid data
    When Submission succeeds
    Then User receives clear success feedback message

  Scenario: Verify clear failure feedback
    Given User submits contact form with invalid data or server error
    When Submission fails
    Then User receives clear failure feedback with actionable guidance

  Scenario: Verify required fields enforced
    Given User attempts to submit form without filling required fields
    When Submission is attempted
    Then Validation prevents submission; required fields are highlighted

  Scenario: Verify email has valid syntax
    Given User enters invalid email format
    When Form validates email field
    Then Validation error is displayed; format requirements are clear

  Scenario: Verify server-side revalidation
    Given User submits form after client-side validation passes
    When Server receives submission
    Then Server revalidates all fields

  Scenario: Verify long comments handled
    Given User enters very long comment text
    When Form renders or submits
    Then Text is accepted; UI handles gracefully with max length if applicable

  Scenario: Verify duplicate submit prevented
    Given Form is submitting
    When User clicks submit again
    Then Duplicate submission is prevented; button is disabled or feedback shown

  Scenario: Verify timeout handled
    Given Network or server timeout during submission
    When Form submission times out
    Then User receives clear timeout message; content preserved for retry

  Scenario: Verify backend error handled
    Given Server returns error during submission
    When Form processes response
    Then User-friendly error displayed; content preserved for retry

  Scenario: Verify bot submission handled
    Given Automated bot submits form
    When Submission is received
    Then Bot detection prevents or flags submission; legitimate users unaffected
