Feature: Implement Insights navigation group

  Scenario: Insights control opens reliably
    Given User is on any page with header visible
    When User activates the Insights navigation item
    Then Insights menu opens and displays thought leadership and resource destinations

  Scenario: Insights child links are readable at all breakpoints
    Given Insights menu is open on mobile
    When User views the menu content
    Then All insight links are readable and operable on mobile viewport

  Scenario: Insights menu has no empty groups
    Given User opens Insights menu
    When Checking menu content for empty groups
    Then All displayed groups contain at least one insight item

  Scenario: Insights destination URLs are canonical
    Given User clicks an Insights navigation link
    When Navigation occurs
    Then User lands on canonical URL under /insights/ path

  Scenario: Hover interaction accessible on touch devices
    Given User is on touch device without hover capability
    When User interacts with Insights menu
    Then Menu opens via tap/click, not requiring hover
