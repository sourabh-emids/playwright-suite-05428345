@issue_0005
Feature: Contact form required-field validation

  Scenario: Empty required fields prevent contact form submission
    Given the contact form is open with every required field empty
    When the user submits the empty contact form
    Then each required field provides a clear validation message
    And the contact form is not submitted
