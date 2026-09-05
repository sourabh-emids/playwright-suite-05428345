@TC-05 @validation @contact-form
Feature: Contact form validates required fields
  Submitting an empty contact form must show clear required-field validation.

  Scenario: Submit the contact form with all required fields empty
    Given the contact form is open with all required fields empty
    When the user submits the empty contact form
    Then a clear required-field validation message is displayed
