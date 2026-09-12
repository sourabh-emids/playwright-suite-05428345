Feature: Insights navigation group implementation

  Scenario: Insights menu opens reliably
    Given A user interacts with the Insights navigation item
    When The menu trigger is activated
    Then Menu opens displaying thought leadership, resources, news, and related insight destinations

  Scenario: Child links readable at all breakpoints
    Given The Insights menu is open
    When Viewed at desktop, tablet, and mobile widths
    Then All child links are readable and operable

  Scenario: No empty menu groups
    Given The Insights navigation structure
    When All menu groups are inspected
    Then No empty menu groups exist; all destination URLs are canonical
