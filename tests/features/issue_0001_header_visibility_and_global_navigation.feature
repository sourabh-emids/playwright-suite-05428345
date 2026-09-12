@issue_0001
Feature: Header visibility and global navigation access

  As a user, I want to clearly see the header and access global navigation
  so that I can browse the website effectively.

  Background:
    Given I navigate to the homepage

  Scenario: Header is visible and contains primary navigation
    When I view the page
    Then the header banner should be visible
    And the main navigation should be present
    And the logo link should navigate to homepage
    And the navigation should include "Solutions"
    And the navigation should include "Capabilities"
    And the navigation should include "Industries"
    And the navigation should include "Insights"
    And the navigation should include "Company"
    And the Connect CTA should be visible in the header
