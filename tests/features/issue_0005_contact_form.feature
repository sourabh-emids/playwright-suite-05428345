@issue_0005 @contact_form
Feature: Contact form validates required fields

  Scenario: Empty required fields prevent contact form submission
    Given the contact form is open with every required field empty
    When the user attempts to submit the contact form
    Then the contact form submission is prevented
    And clear validation feedback appears for every required field
