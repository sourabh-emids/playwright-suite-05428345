Feature: Provide contact form with required fields

  Scenario: All required fields displayed on contact page
    Given User navigates to /contact/
    When Form renders
    Then Fields visible: First Name, Last Name, Work Email Address, Company Name, Title, Phone Number, Inquiry Type, and Comments

  Scenario: Labels associated with controls
    Given Screen reader or accessibility test
    When Checking label associations
    Then Each input has associated label via for/id attribute

  Scenario: Submission provides clear success feedback
    Given User submits valid form
    When Submission completes successfully
    Then User sees clear success message or confirmation

  Scenario: Submission provides clear failure feedback
    Given User submits form with error
    When Submission fails
    Then User sees clear error message explaining failure

  Scenario: Required fields enforced client-side
    Given User submits form with empty required field
    When Checking validation
    Then Client-side validation prevents submission; error shown

  Scenario: Email syntax validated
    Given User enters invalid email format
    When Submitting form
    Then Email validation error shown; proper email pattern required

  Scenario: Server revalidates submitted data
    Given Form passes client validation
    When Server receives submission
    Then Server re-validates all fields; rejects invalid server-side

  Scenario: Invalid email server rejection
    Given User submits form with server-side invalid email
    When Server processes
    Then Server rejects with appropriate error; user can correct

  Scenario: Long comments handled
    Given User enters very long comment
    When Form renders and submits
    Then Long text accepted within reasonable limits; no breaking errors

  Scenario: Duplicate submit prevented
    Given User clicks submit twice rapidly
    When First submission in progress
    Then Second click prevented; no duplicate submissions

  Scenario: Timeout handled gracefully
    Given Submission times out
    When User submits form
    Then User sees timeout message; can retry

  Scenario: Backend error handled
    Given Backend returns error
    When User submits form
    Then User sees error message; form data preserved for retry

  Scenario: Bot submission prevention
    Given Automated/bot attempts form submission
    When Bot detection triggers
    Then Submission blocked or challenged; legitimate users unaffected

  Scenario: Attribution context preserved in submission
    Given User arrives via campaign URL with UTM
    When Form submits
    Then Attribution context included in submission for analytics
