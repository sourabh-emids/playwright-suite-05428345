Feature: Industries mega-menu implementation

  Scenario: Industries menu contains all five audiences
    Given Industries menu is open
    When User views menu content
    Then Menu contains Payer, Provider, HealthTech, Life Sciences, and Consumer destinations

  Scenario: All audience links reachable without mouse
    Given Industries menu is open
    When User uses keyboard to navigate
    Then All five audience destinations are keyboard accessible

  Scenario: Payer link routes correctly
    Given Industries menu is open
    When User clicks Payer
    Then User is navigated to '/segments/payer/'

  Scenario: Provider link routes correctly
    Given Industries menu is open
    When User clicks Provider
    Then User is navigated to '/segments/provider/'

  Scenario: HealthTech link routes correctly
    Given Industries menu is open
    When User clicks HealthTech
    Then User is navigated to '/segments/healthtech/'

  Scenario: Life Sciences link routes correctly
    Given Industries menu is open
    When User clicks Life Sciences
    Then User is navigated to '/segments/life-sciences/'

  Scenario: Consumer link routes correctly
    Given Industries menu is open
    When User clicks Consumer
    Then User is navigated to '/segments/consumer/'

  Scenario: Desktop grouped menu layout
    Given User is on desktop viewing Emids homepage
    When User activates Industries
    Then Desktop uses grouped menu layout

  Scenario: Mobile stacked list layout
    Given User is on mobile viewing Emids homepage
    When User activates Industries
    Then Mobile uses stacked list/disclosure pattern

  Scenario: Links use canonical URLs
    Given Industries menu is open
    When User inspects audience link URLs
    Then All links use canonical URLs matching the specified endpoints
