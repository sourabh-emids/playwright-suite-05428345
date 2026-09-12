@issue_0035
Feature: Delivery timing message rendering

  As a user, I want to see the delivery timing message
  so that I understand the quick time-to-value.

  Background:
    Given I navigate to the homepage

  Scenario: Delivery timing message is rendered
    When I view the final CTA section
    Then the timing message "1 Day · 2 Weeks · 3 Months" should be visible
    And the timing description should be present
