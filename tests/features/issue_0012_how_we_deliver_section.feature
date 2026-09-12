@issue_0012
Feature: How We Deliver section content rendering

  As a user, I want to see the How We Deliver section with proper content
  so that I understand emids delivery model.

  Background:
    Given I navigate to the homepage

  Scenario: How We Deliver section renders correctly
    When I view the How We Deliver section
    Then the section heading should be visible
    And the FDCE description should be present
    And the feature list should be rendered
