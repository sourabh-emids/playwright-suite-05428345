"""Feature file for Issue 0005 - Insights navigation group implementation."""
Feature: Insights navigation group implementation

  Scenario: Insights control opens reliably
    Given A user is viewing the Emids homepage desktop header
    When The user activates the Insights navigation item
    Then The menu opens displaying thought leadership, resources, and destinations

  Scenario: Insights child links operable at breakpoints
    Given A user has the Insights menu open at various viewport widths
    When The user views the menu at desktop, tablet, and mobile widths
    Then Child links are readable and operable at all supported breakpoints

  Scenario: No empty menu groups in Insights
    Given A user has the Insights menu open
    When The user examines the menu groups
    Then No menu groups are empty; each has at least one destination

  Scenario: Insights destination URLs are canonical
    Given A user has the Insights menu open
    When The user clicks on any Insights link
    Then The destination URL is canonical
