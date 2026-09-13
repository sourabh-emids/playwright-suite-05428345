Feature: Insights navigation group
  # issue_0005

  Scenario: Insights menu opens reliably
    Given A user focuses on the Insights navigation item
    When The user activates the trigger
    Then The Insights menu opens displaying thought leadership, resources, news, and related destinations

  Scenario: Insights child links operable at breakpoints
    Given The Insights menu is open
    When The user tests at desktop, tablet, and mobile widths
    Then Child links remain readable and operable across all supported breakpoints

  Scenario: No empty menu groups in Insights
    Given The Insights navigation group is rendered
    When Automated testing checks menu content
    Then All menu groups contain at least one navigation item
