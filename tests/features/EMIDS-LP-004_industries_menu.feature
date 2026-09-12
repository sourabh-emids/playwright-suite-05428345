Feature: Industries mega-menu implementation

  Scenario: Industries menu contains all five audiences
    Given The Industries mega-menu is open
    When All menu items are inspected
    Then Payer, Provider, HealthTech, Life Sciences, and Consumer destinations are present

  Scenario: Each audience reachable without mouse
    Given The Industries menu is open
    When User navigates via keyboard
    Then All five audience links are reachable and activate on keyboard input

  Scenario: Audience links use canonical URLs
    Given Each industry audience link in the menu
    When URLs are verified
    Then All use canonical URLs: /segments/payer/, /segments/provider/, /segments/healthtech/, /segments/life-sciences/, /segments/consumer/

  Scenario: Mobile stacked list for Industries
    Given A user on mobile viewport
    When The Industries menu is accessed
    Then A stacked list or disclosure pattern is used
