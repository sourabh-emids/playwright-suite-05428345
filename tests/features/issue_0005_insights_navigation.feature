@issue_0005
Feature: Insights navigation group accessibility

  As a user, I want to access the Insights navigation group
  so that I can find content and resources.

  Background:
    Given I navigate to the homepage

  Scenario: Insights mega-menu displays content categories
    When I click the Insights navigation item
    Then the Insights mega-menu should appear
    And the menu should display "Insights and Resources"
    And the menu should display "News & Events"
    And the Insights Hub link should be present
    And the Case Studies link should be present
    And the eBooks & Guides link should be present
    And the Webinars link should be present
