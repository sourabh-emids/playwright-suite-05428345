Feature: Contact form reached by Connect CTAs

  Scenario: All required fields displayed
    Given Contact form at /contact/
    When Form is inspected
    Then All fields present: First Name, Last Name, Work Email Address, Company Name, Title, Phone Number, Inquiry Type, Comments

  Scenario: Labels associated with controls
    Given Contact form fields
    When Accessibility is checked
    Then Each label is properly associated with its control

  Scenario: Submission provides clear feedback
    Given Contact form submission
    When Form is submitted
    Then Clear success or failure feedback is provided

  Scenario: Required fields enforced
    Given Contact form validation
    When Required fields are empty
    Then Submission is prevented with appropriate error

  Scenario: Email validation
    Given Email field with invalid input
    When Submission is attempted
    Then Email must have valid syntax; server revalidates

  Scenario: Invalid email handling
    Given Invalid email format submitted
    When Form validation runs
    Then Error message displayed for invalid email

  Scenario: Timeout handling
    Given Server timeout during submission
    When Submission is attempted
    Then User receives timeout error and can retry
