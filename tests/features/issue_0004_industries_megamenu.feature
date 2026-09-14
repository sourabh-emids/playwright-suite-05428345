Feature: Implement Industries mega-menu

  Scenario: Industries menu displays all five audience destinations
    Given User activates the Industries navigation item
    When Menu opens on desktop
    Then Payer, Provider, HealthTech, Life Sciences, and Consumer destinations are all visible

  Scenario: All industry links reachable without mouse
    Given Industries menu is open
    When User navigates using keyboard only
    Then Each of the five audience links is keyboard accessible

  Scenario: Industry links use canonical URLs
    Given User inspects industry link URLs
    When Comparing to specified canonical paths
    Then Links resolve to /segments/payer/, /segments/provider/, /segments/healthtech/, /segments/life-sciences/, and /segments/consumer/

  Scenario: Mobile industry navigation uses stacked list
    Given User is on mobile device
    When User expands Industries section
    Then Five audience destinations display in stacked list or disclosure pattern

  Scenario: Industry menu with one segment unpublished
    Given One industry segment is in unpublished state
    When Industries menu opens
    Then Unpublished segment does not appear in menu; remaining segments display normally
