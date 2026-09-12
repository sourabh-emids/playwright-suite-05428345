@issue_0033
Feature: Resource access handoff for eBook cards

  As a user, I want to access eBook resources by clicking cards
  so that I can download or read content.

  Background:
    Given I navigate to the homepage

  Scenario: eBook card links to resource page
    When I view the Insights section
    And I click an eBook card
    Then I should be navigated to the resource page
