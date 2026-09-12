@issue_0051
Feature: SEO metadata and crawlable structure

  As a user, I want the page to have proper SEO metadata
  so that search engines can index it properly.

  Background:
    Given I navigate to the homepage

  Scenario: Page has proper SEO metadata
    When I view the page source
    Then the page should have a title tag
    And the page should have meta description
    And the page should have canonical URL
