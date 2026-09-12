"""Feature file for Issue 0026 - Insights section and content cards rendering."""
Feature: Insights section and content cards rendering

  Scenario: Six cards render with required content
    Given A user views the Insights section
    When The section loads
    Then Six cards render with content type, title, image (where configured), and Download or Read More action

  Scenario: Cards accessible at all breakpoints
    Given A user views the Insights section at desktop, tablet, and mobile widths
    When The viewport changes
    Then Cards remain accessible and properly laid out at all breakpoints

  Scenario: Published content only displayed
    Given A user views the Insights section
    When The cards are analyzed
    Then Only published content is displayed; unpublished resources are excluded

  Scenario: Title and URL required for each card
    Given A user examines an Insights card
    When The card content is analyzed
    Then Each card has a non-empty title and valid URL

  Scenario: Action label matches content flow
    Given A user views an Insights card
    When The action label is examined
    Then Action label correctly reflects content flow (Download for eBooks, Read More for articles)

  Scenario: Resource unpublished handling
    Given A resource is unpublished after card is configured
    When The Insights section renders
    Then The unpublished resource is excluded; remaining cards display correctly
