Feature: Five audience/industry entries rendering

  Scenario: All five audiences are visible
    Given Who We Serve section
    When Audiences are inspected
    Then Payer, Provider, HealthTech, Life Sciences, and Consumer are all visible

  Scenario: Each Explore action routes to canonical segment page
    Given Each audience Explore CTA
    When URLs are verified
    Then Payer → /segments/payer/, Provider → /segments/provider/, HealthTech → /segments/healthtech/, Life Sciences → /segments/life-sciences/, Consumer → /segments/consumer/

  Scenario: Explore actions work on keyboard and touch
    Given Explore CTAs
    When Tested with keyboard and touch input
    Then All CTAs are operable with both input methods

  Scenario: Exactly five current audiences
    Given Audience count
    When Items are verified
    Then Exactly five audiences are configured for this content version

  Scenario: One segment unavailable
    Given Edge case where one segment is unavailable
    When Section renders
    Then Section handles gracefully without breaking

  Scenario: Tab state preserved after resize
    Given Tabbed audience interface
    When Window is resized
    Then Tab state is appropriately maintained or reset
