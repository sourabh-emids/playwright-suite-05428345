@REQ-005
Feature: Contact form displays validation for required fields

  @validation @form_validation
  Scenario: Empty form submission shows validation messages
    Given User navigates to and opens the contact form
    When User submits the form with all required fields left empty
    Then Clear validation messages appear for each required field indicating they are mandatory

  @validation @form_validation
  Scenario: Form is not submitted with incomplete required fields
    Given User submits contact form with incomplete required fields
    When Form validation is triggered
    Then The form is not submitted and appropriate error messaging guides user to complete required fields

  @validation @form_validation
  Scenario: Validation message appears for First Name field
    Given User is on the contact page
    When User submits the form without filling First Name
    Then The First Name field should show validation message "This field is required"

  @validation @form_validation
  Scenario: Validation message appears for Work Email field
    Given User is on the contact page
    When User submits the form without filling Work Email
    Then The Work Email field should show validation message "This field is required"

  @validation @form_validation
  Scenario: Validation message appears for Company Name field
    Given User is on the contact page
    When User submits the form without filling Company Name
    Then The Company Name field should show validation message "This field is required"
