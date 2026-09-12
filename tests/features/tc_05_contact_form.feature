Feature: Contact form validates empty required fields
  As a visitor
  I want clear feedback when I submit an empty contact form
  So that I know which fields must be completed

  Scenario: Empty contact form shows required-field validation
    Given the contact form is open with empty required fields
    When the visitor submits the contact form
    Then every required contact field is marked invalid
    And a clear required-field validation message is displayed
