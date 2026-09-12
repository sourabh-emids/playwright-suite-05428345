@issue_0008
Feature: Responsive navigation behavior across viewports

  As a user, I want to experience appropriate navigation on different devices
  so that I can browse the website on any device.

  Background:
    Given I navigate to the homepage

  Scenario: Navigation displays correctly on desktop viewport
    When I set the viewport to desktop size
    Then the full navigation menu should be visible
    And the Connect CTA should be visible

  Scenario: Navigation behavior on mobile viewport
    When I set the viewport to mobile size
    Then the mobile menu toggle should be visible
    And tapping the menu toggle should reveal navigation options
