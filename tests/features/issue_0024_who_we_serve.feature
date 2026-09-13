Feature: Five audience/industry entries rendering

  Scenario: All five audiences visible
    Given User views Who We Serve section
    When Page renders
    Then All five audiences are visible: Payer, Provider, HealthTech, Life Sciences, Consumer

  Scenario: Each Explore action routes to canonical segment
    Given Audience cards render
    When User clicks Explore action for each audience
    Then Each routes to its canonical segment page

  Scenario: Interactions work on keyboard
    Given Who We Serve section renders
    When User navigates with keyboard
    Then All audience Explore actions are keyboard accessible

  Scenario: Interactions work on touch
    Given Who We Serve section renders on touch device
    When User navigates with touch
    Then All audience Explore actions are touch accessible

  Scenario: Payer segment accessible
    Given User views Payer audience entry
    When User clicks Explore
    Then User is navigated to '/segments/payer/'

  Scenario: Provider segment accessible
    Given User views Provider audience entry
    When User clicks Explore
    Then User is navigated to '/segments/provider/'

  Scenario: HealthTech segment accessible
    Given User views HealthTech audience entry
    When User clicks Explore
    Then User is navigated to '/segments/healthtech/'

  Scenario: Life Sciences segment accessible
    Given User views Life Sciences audience entry
    When User clicks Explore
    Then User is navigated to '/segments/life-sciences/'

  Scenario: Consumer segment accessible
    Given User views Consumer audience entry
    When User clicks Explore
    Then User is navigated to '/segments/consumer/'

  Scenario: Exactly five audiences for this version
    Given Who We Serve section renders
    When User counts audiences
    Then Exactly five current audiences are displayed

  Scenario: Tab state preserved after resize
    Given User interacts with tab-based audience display
    When User resizes viewport
    Then Tab state is handled appropriately

  Scenario: One segment unavailable handling
    Given One segment page is unavailable
    When User clicks Explore for that segment
    Then Appropriate error handling occurs
