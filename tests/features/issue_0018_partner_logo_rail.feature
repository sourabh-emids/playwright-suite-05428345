@issue_0018
Feature: Partner logo rail rendering and accessibility

  As a user, I want to see partner logos that are accessible
  so that I know who emids partners with.

  Background:
    Given I navigate to the homepage

  Scenario: Partner logos are rendered and accessible
    When I view the Partnerships section
    Then partner logos should be visible
    And logos should have alt text for accessibility
