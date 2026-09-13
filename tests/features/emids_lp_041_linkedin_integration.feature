Feature: Integrate LinkedIn marketing tags conditionally

  Scenario: Verify tag does not execute before consent
    Given LinkedIn tag is configured
    When Page loads without marketing consent
    Then LinkedIn tag does not execute

  Scenario: Verify core page independent of LinkedIn tag
    Given LinkedIn tag fails to load
    When Page renders
    Then Core page functionality remains intact

  Scenario: Verify marketing consent required
    Given LinkedIn integration is configured
    When User denies marketing consent
    Then LinkedIn tag remains inactive

  Scenario: Verify ad blocker handled
    Given Ad blocker prevents LinkedIn tag loading
    When Page loads
    Then Core page remains functional

  Scenario: Verify vendor timeout handled
    Given LinkedIn tag loading times out
    When Page renders
    Then Core page renders without waiting for tag

  Scenario: Verify consent denied handled
    Given User has not granted marketing consent
    When Page loads
    Then LinkedIn tag does not execute; no impact on page
