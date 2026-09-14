Feature: Contact form validation messages

  Scenario: Empty form submission shows validation errors
    Given The user is on the contact form page
    When The user clicks the Submit button without filling in any required fields
    Then Clear validation error messages appear indicating which required fields are missing such as Name, Email, Phone, and Message fields must be filled

  Scenario: Invalid email format shows error
    Given The user is on the contact form page
    When The user enters an invalid email format such as test@ or test.com and attempts to submit
    Then A validation message is displayed indicating the email format is invalid with guidance to enter a valid email address

  Scenario: Phone field validates numeric input
    Given The user is on the contact form page
    When The user enters non-numeric characters in the phone field and attempts to submit
    Then A validation message appears indicating the phone field should contain only numeric values or a valid phone number format

  Scenario: Empty required message field shows error
    Given The user is on the contact form page with all other required fields filled
    When The user leaves the message field empty and clicks Submit
    Then A clear validation message appears stating the message field is required

  Scenario: Submit is blocked until all validations pass
    Given The user has attempted to submit the form with multiple validation errors
    When The user corrects one field but leaves others invalid
    Then Form submission is still blocked and remaining validation errors are clearly displayed

  Scenario: Validation errors clear on field correction
    Given The user has submitted a form with validation errors visible
    When The user fills in the previously empty or invalid field with correct data
    Then The validation error message for that specific field is cleared or updated to confirm the field is now valid

  Scenario: Character limits enforced on text fields
    Given The user is on the contact form page with text fields that have character limits
    When The user attempts to enter text exceeding the character limit
    Then Additional text input is prevented or a character count indicator shows the remaining characters available
