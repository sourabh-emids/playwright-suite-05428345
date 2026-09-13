Feature: Implement Industries mega-menu

  Scenario: Verify all five industry audiences are present
    Given The Industries mega-menu is open
    When The user inspects the menu content
    Then The menu contains Payer, Provider, HealthTech, Life Sciences, and Consumer destinations

  Scenario: Verify each industry is reachable without mouse
    Given The Industries menu is open
    When The user navigates using keyboard alone
    Then All five industry links (Payer, Provider, HealthTech, Life Sciences, Consumer) are reachable and activatable via keyboard

  Scenario: Verify industry links use canonical URLs
    Given The Industries menu is open
    When The user clicks each industry link
    Then Links resolve to canonical URLs: /segments/payer/, /segments/provider/, /segments/healthtech/, /segments/life-sciences/, /segments/consumer/

  Scenario: Verify mobile stacked list pattern
    Given The user is on mobile viewport
    When The Industries navigation is activated
    Then Industry destinations display as a stacked list or disclosure pattern

  Scenario: Verify graceful handling of unpublished segment
    Given One industry segment is unpublished
    When The user opens the Industries menu
    Then Only published segments appear; no broken or missing links are displayed

  Scenario: Verify long translations handled
    Given The site is in a locale with longer translated labels
    When The Industries menu opens
    Then Menu layout accommodates longer labels without overlapping or truncation
