"""Feature file for Issue 0047 - Contact form accessible from Connect CTAs."""
Feature: Contact form accessible from Connect CTAs

  Scenario: All required fields displayed on contact page
    Given A user navigates to /contact/
    When The contact form loads
    Then All fields are displayed: First Name, Last Name, Work Email Address, Company Name, Title, Phone Number, Inquiry Type, Comments

  Scenario: Labels associated with controls
    Given A user uses assistive technology to navigate the contact form
    When Form fields are encountered
    Then Labels are properly associated with their controls via for/id attributes

  Scenario: Submission provides clear feedback
    Given A user submits the contact form
    When Submission completes (success or failure)
    Then Clear success or failure feedback is provided

  Scenario: Required fields enforced client-side
    Given A user attempts to submit with required fields empty
    When Form validation occurs
    Then Required field validation is enforced

  Scenario: Email valid syntax enforced
    Given A user enters an invalid email address
    When Form validation occurs
    Then Email field validates for valid email syntax

  Scenario: Server revalidates form data
    Given A user submits the form
    When Server receives the submission
    Then Server-side validation re-validates all fields

  Scenario: Invalid email handling
    Given User enters invalid email
    When Form is submitted
    Then Appropriate error message is displayed; form data preserved for correction

  Scenario: Long comments handling
    Given User enters comments exceeding expected length
    When Form validates or submits
    Then Appropriate handling (truncation warning, validation error, or max length enforced)

  Scenario: Duplicate submit prevention
    Given User clicks submit multiple times rapidly
    When Form is being submitted
    Then Duplicate submission is prevented

  Scenario: Backend error handling
    Given Backend or CRM returns an error
    When Form is submitted
    Then User sees error message; user-entered content is preserved for retry

  Scenario: Bot submission handling
    Given Automated bot attempts to submit form
    When Submission is received
    Then Appropriate bot protection prevents submission or marks as bot
