@issue_0047
Feature: Contact form fields and accessibility

  As a user, I want to access the contact form with accessible fields
  so that I can submit inquiries.

  Background:
    Given I navigate to the contact page

  Scenario: Contact form has accessible fields
    When I view the contact form
    Then the form fields should have labels
    And the fields should be keyboard accessible
