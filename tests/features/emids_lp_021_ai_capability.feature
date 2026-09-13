Feature: Render AI capability content

  Scenario: Verify AI label and supporting content render
    Given AI capability is configured
    When The capabilities section renders
    Then AI label displays with supporting content including summary

  Scenario: Verify AI relevant link is operable
    Given AI capability card renders
    When User clicks AI capability link/CTA
    Then Link routes to valid AI capability destination

  Scenario: Verify title required
    Given AI capability is configured
    When Section renders
    Then AI capability has non-empty title

  Scenario: Verify URL valid
    Given AI capability links are configured
    When User activates AI capability link
    Then Destination URL resolves successfully

  Scenario: Verify missing destination handled
    Given AI capability has missing or broken destination
    When User clicks link
    Then Appropriate error handling without page break

  Scenario: Verify card matches visual system
    Given AI capability renders
    When User views card styling
    Then Card/panel matches capability visual system design
