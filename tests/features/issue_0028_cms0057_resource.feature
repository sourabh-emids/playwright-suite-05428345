"""Feature file for Issue 0028 - CMS-0057 interoperability resource card."""
Feature: CMS-0057 interoperability resource card

  Scenario: Card title/type/action populated
    Given A user views the CMS-0057 interoperability resource card
    When The card renders
    Then Card title, type, and action are populated from approved content

  Scenario: CMS-0057 card routes to intended resource
    Given A user clicks the CMS-0057 card action
    When The action is activated
    Then User is navigated to the intended CMS-0057 resource destination

  Scenario: No empty title or destination
    Given A user examines the CMS-0057 card
    When The card content is analyzed
    Then Title and destination are not empty

  Scenario: Content unpublished handling
    Given The CMS-0057 content is unpublished
    When The Insights section renders
    Then The card is excluded or shows appropriate unavailable state
