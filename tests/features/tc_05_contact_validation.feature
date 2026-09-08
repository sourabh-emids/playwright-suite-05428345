@TC-05
Feature: Emids contact form required-field validation
  As a website visitor
  I want clear validation on required contact fields
  So that I know what information must be supplied

  Scenario: Contact form validates empty required fields
    Given the Emids contact form is open with every required field empty
    When I submit the empty contact form
    Then the contact form submission is rejected
    And every empty required field provides clear validation feedback
