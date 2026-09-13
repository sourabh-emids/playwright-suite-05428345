Feature: Industries mega-menu implementation
  # issue_0004

  Scenario: Industries menu contains all five audiences
    Given A user opens the Industries navigation menu
    When The menu is fully rendered
    Then The menu contains Payer, Provider, HealthTech, Life Sciences, and Consumer destinations

  Scenario: All industry links reachable without mouse
    Given The Industries menu is open
    When The user navigates using only keyboard
    Then All five industry destinations are keyboard accessible

  Scenario: Industry URLs use canonical paths
    Given The Industries menu displays all audience links
    When Automated testing validates URLs
    Then All URLs follow canonical patterns: /segments/payer/, /segments/provider/, /segments/healthtech/, /segments/life-sciences/, /segments/consumer/

  Scenario: Mobile Industries uses stacked list
    Given A user is on a mobile device
    When The Industries menu is expanded
    Then A stacked list or disclosure pattern provides access to all five audiences
