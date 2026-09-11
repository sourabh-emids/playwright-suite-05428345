Feature: TC-05 Required contact form validation
  Verify that an incomplete contact form is blocked and each required field provides clear validation feedback.

  Scenario: Empty required contact fields prevent submission
    Given the TC-05 user opens the contact form with required fields empty
    When the TC-05 user attempts to submit the incomplete contact form
    Then the TC-05 form remains unsubmitted and each required field shows a clear validation message
