@issue_0053
Feature: Performance and Core Web Vitals optimization

  As a user, I want the page to load quickly with good Core Web Vitals
  so that I have a fast and smooth experience.

  Background:
    Given I navigate to the homepage

  Scenario: Page has good performance metrics
    When I measure performance metrics
    Then the page should load within acceptable time
    And LCP should be within acceptable range
