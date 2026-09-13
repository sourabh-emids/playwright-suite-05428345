Feature: Contact form reached by Connect CTAs

  Scenario: All required fields displayed
    Given User is on contact form
    When Form renders
    Then All required fields are displayed: First Name, Last Name, Work Email Address, Company Name, Title, Phone Number, Inquiry Type, Comments

  Scenario: Labels associated with controls
    Given User views contact form
    When Screen reader is active
    Then Labels are properly associated with controls

  Scenario: Submission provides feedback
    Given User submits contact form
    When Submission completes
    Then Clear success or failure feedback is provided

  Scenario: Required fields enforced
    Given User attempts to submit incomplete form
    When Submission is initiated
    Then Required field validation is enforced

  Scenario: Email valid syntax validation
    Given User enters invalid email
    When Form validates
    Then Email field shows valid format error

  Scenario: Server revalidates
    Given User submits contact form
    When Client validation passes
    Then Server-side revalidation occurs

  Scenario: Invalid email error display
    Given User enters invalid email format
    When User attempts submit
    Then Error is displayed for email field

  Scenario: Long comments handling
    Given User enters very long comments
    When Form renders
    Then Comments field handles appropriately with max length

  Scenario: Duplicate submit prevention
    Given User clicks submit multiple times
    When Form is being submitted
    Then Duplicate submission is prevented

  Scenario: Timeout handling
    Given Submission times out
    When Form submits
    Then User sees error and can retry

  Scenario: Backend error handling
    Given Backend returns error
    When Form submits
    Then User sees error with clear messaging

  Scenario: Bot submission handling
    Given Bot attempts submission
    When Submission occurs
    Then Bot submission is detected and rejected
