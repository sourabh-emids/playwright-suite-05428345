@TC-05
Feature: Contact form validates empty required fields
  An incomplete contact request must remain on the form and clearly identify
  every required field that needs attention.

  Scenario: Submit the contact form with every required field empty
    Given the contact form is open with all required fields empty
    When the empty contact form is submitted
    Then every empty required field shows a clear validation message
    And the incomplete contact form is not submitted
