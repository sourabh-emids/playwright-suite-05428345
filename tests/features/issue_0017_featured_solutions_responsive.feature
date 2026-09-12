@issue_0017
Feature: Featured solutions responsive interaction

  As a user, I want to interact with featured solutions on different devices
  so that I can browse solutions on any device.

  Background:
    Given I navigate to the homepage

  Scenario: Featured solutions display correctly on desktop
    When I set the viewport to desktop size
    And I view the Featured Solutions section
    Then solution cards should be displayed in a grid layout

  Scenario: Featured solutions display correctly on mobile
    When I set the viewport to mobile size
    And I view the Featured Solutions section
    Then solution cards should be displayed in a single column or stacked layout
