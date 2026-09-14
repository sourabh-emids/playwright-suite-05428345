Feature: Display CMS-0057 interoperability card

  Scenario: CMS-0057 card displays with correct content
    Given User views Insights section
    When Locating CMS-0057 card
    Then Card displays with approved title, type, and action

  Scenario: CMS-0057 card has valid destination
    Given User clicks CMS-0057 card
    When Navigation occurs
    Then User navigates to configured resource destination

  Scenario: CMS-0057 no empty title or destination
    Given CMS validation for CMS-0057 card
    When Checking required fields
    Then Card has non-empty title and valid destination URL

  Scenario: Destination changed handled
    Given CMS-0057 resource URL changed
    When Page renders
    Then Card links to updated URL or broken link flagged in QA

  Scenario: Content unpublished handled
    Given CMS-0057 content is unpublished
    When Page renders
    Then Card not displayed or shows appropriate unavailable state
