Feature: Render five audience/industry entries

  Scenario: All five audiences visible
    Given User views Who We Serve section
    When Checking audience display
    Then Payer, Provider, HealthTech, Life Sciences, and Consumer are all visible

  Scenario: Each Explore action routes to canonical segment page
    Given User clicks Explore action on any audience
    When Navigation triggered
    Then User navigates to respective canonical URL: /segments/payer/, /segments/provider/, /segments/healthtech/, /segments/life-sciences/, or /segments/consumer/

  Scenario: Explore actions work on keyboard and touch
    Given User tests Explore interactions
    When Using keyboard Tab/Enter or touch tap
    Then Navigation functions correctly with both input methods

  Scenario: Exactly five audiences for this content version
    Given Content version specification
    When Counting audiences
    Then Exactly five audience entries display

  Scenario: Audience URLs canonical
    Given User inspects audience destination URLs
    When Checking URL format
    Then All URLs use canonical /segments/ paths

  Scenario: One segment unavailable handled
    Given One audience segment page is unavailable
    When Page renders
    Then Unavailable segment either shows appropriate fallback or is hidden; other four segments display normally

  Scenario: Tab state preserved after resize
    Given User interacts with audience tabs/accordion
    When Window resizes from desktop to mobile
    Then Active tab state is preserved appropriately for new layout

  Scenario: No duplicate active panels
    Given User interacts with audience controls
    When Checking active state
    Then Only intended panel is active; no duplicate active states occur
