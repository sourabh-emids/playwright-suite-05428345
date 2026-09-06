@tc_05
Feature: TC-05 Contact form validation

  Scenario: Empty required fields display validation feedback
    Given the contact form is open with every required field empty
    When the user submits the contact form
    Then the form remains open and every required field shows a clear message
