Feature: Contact form required-field validation

  Scenario: Contact form validates missing required information
    Given the contact form is open with all required fields empty
    When the user submits the empty contact form
    Then all required fields are marked invalid with a clear message
    And the contact form remains open without a successful submission
