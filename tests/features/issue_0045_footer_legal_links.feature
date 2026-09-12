@issue_0045
Feature: Footer legal navigation links

  As a user, I want to access legal navigation links in the footer
  so that I can review policies and compliance information.

  Background:
    Given I navigate to the homepage

  Scenario: Footer displays legal navigation links
    When I view the footer
    Then the Code of Conduct link should be present
    And the Privacy Policy link should be present
    And the Transparency in Coverage link should be present
    And the Cookie Policy link should be present
    And the Accessibility Statement link should be present
