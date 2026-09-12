@issue_0048
Feature: Contact form Inquiry Type values

  As a user, I want to select from inquiry type options
  so that my inquiry is properly categorized.

  Background:
    Given I navigate to the contact page

  Scenario: Contact form has inquiry type dropdown
    When I view the contact form
    Then the Inquiry Type field should be present
    And the field should have multiple options
