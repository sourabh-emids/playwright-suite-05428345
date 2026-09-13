Feature: Render five audience/industry entries

  Scenario: Verify all five audiences visible
    Given Who We Serve section renders
    When User views the section
    Then All five audiences display: Payer, Provider, HealthTech, Life Sciences, Consumer

  Scenario: Verify Explore action routes to canonical segment
    Given Each audience entry has Explore action
    When User clicks audience Explore CTA
    Then Action routes to canonical segment URL

  Scenario: Verify keyboard and touch interaction works
    Given Audience entries render
    When User interacts via keyboard and touch
    Then All audience entries and Explore actions are operable via keyboard and touch

  Scenario: Verify exactly five current audiences
    Given Who We Serve section renders
    When User counts audience entries
    Then Exactly five audiences are configured for this content version

  Scenario: Verify URLs canonical
    Given Audience entries render
    When User inspects segment URLs
    Then All URLs match canonical pattern: /segments/payer/, /segments/provider/, etc.

  Scenario: Verify one segment unavailable handled
    Given One segment page is unavailable
    When User clicks that segment's Explore action
    Then Graceful error handling without breaking page

  Scenario: Verify tab state maintained after resize
    Given Tab-based audience view is active
    When Viewport resizes
    Then Active tab state is maintained or gracefully adapted

  Scenario: Verify responsive layout per design
    Given Who We Serve section renders at different viewports
    When User views at mobile, tablet, desktop
    Then Layout uses tabs/cards/accordion/rail as designed without hiding access to any audience
