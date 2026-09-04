@TC-05
Feature: Contact form required-field validation
  As a website visitor
  I want clear feedback when required contact details are missing
  So that I know what must be supplied

  Scenario: Empty contact form identifies required fields
    Given the contact form is open with every required field empty
    When the user submits the empty contact form
    Then every required contact field is identified and a clear validation message is displayed
