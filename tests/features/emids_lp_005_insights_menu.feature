Feature: Implement Insights navigation group

  Scenario: Verify Insights control opens reliably
    Given The user is on the homepage
    When The user activates the Insights navigation control
    Then The Insights menu opens and displays thought leadership, resources, news, and related destinations

  Scenario: Verify child links readable and operable at all breakpoints
    Given The Insights menu is open
    When The user views at desktop, tablet, and mobile widths
    Then Child links remain readable and operable across all supported breakpoints

  Scenario: Verify no empty menu groups
    Given The Insights menu is open
    When The user inspects each navigation group
    Then No menu groups are empty; all contain at least one link

  Scenario: Verify destination URLs are canonical
    Given The Insights menu is open
    When The user clicks an Insights destination link
    Then URLs resolve to canonical destinations under /insights/ or related resource paths

  Scenario: Verify hover interaction not required for access
    Given The user is on a touch device or prefers no hover
    When The user taps the Insights navigation control
    Then Menu opens without requiring hover interaction
