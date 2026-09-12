@issue_0052
Feature: Responsive layout across common viewports

  As a user, I want the page to render correctly across different devices
  so that I have a good experience on any device.

  Background:
    Given I navigate to the homepage

  Scenario: Page renders correctly on desktop
    When I set the viewport to 1920x1080
    Then the page should render without horizontal overflow

  Scenario: Page renders correctly on tablet
    When I set the viewport to 768x1024
    Then the page should render without horizontal overflow

  Scenario: Page renders correctly on mobile
    When I set the viewport to 375x667
    Then the page should render without horizontal overflow
