@issue_0028
Feature: CMS-0057 interoperability resource card display

  As a user, I want to see the CMS-0057 interoperability resource card
  so that I can access relevant content.

  Background:
    Given I navigate to the homepage

  Scenario: CMS-0057 eBook card is displayed
    When I view the Insights section
    Then the CMS-0057 eBook card should be visible
    And the card should have the eBook type indicator
