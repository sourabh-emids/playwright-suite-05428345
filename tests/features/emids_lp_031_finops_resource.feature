Feature: Display FinOps healthcare payer resource card

  Scenario: Verify FinOps card renders title/type/action
    Given FinOps healthcare payer resource is configured
    When Insight card renders
    Then Card displays appropriate title, type, and action

  Scenario: Verify card routes correctly
    Given FinOps card renders
    When User clicks action
    Then Navigation routes to configured resource destination

  Scenario: Verify valid destination required
    Given FinOps resource is configured
    When Card renders
    Then Destination URL is valid and resolves

  Scenario: Verify broken link handled
    Given FinOps resource link is broken
    When User clicks
    Then Appropriate error handling without page break

  Scenario: Verify missing thumbnail handled
    Given FinOps card has no thumbnail configured
    When Card renders
    Then Card renders without image; no broken placeholder
