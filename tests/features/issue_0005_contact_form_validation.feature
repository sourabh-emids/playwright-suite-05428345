Feature: Contact form validates required fields

  Scenario: Verify contact form shows validation for empty required fields
    Given The contact form page is loaded with all required fields visible
    When The user submits the contact form with all required fields left empty
    Then Clear validation messages appear indicating required fields must be completed
