@issue_0019
Feature: Reduced motion preference for partner animation

  As a user with motion sensitivity, I want the page to respect my reduced motion preference
  so that animations don't cause discomfort.

  Background:
    Given I navigate to the homepage

  Scenario: Page respects reduced motion preference
    When I have "prefers-reduced-motion: reduce" set
    And I view the Partnerships section
    Then the partner logo animation should be reduced or disabled
