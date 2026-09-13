Feature: Render Engineering capability content

  Scenario: Verify Engineering label and supporting content render
    Given Engineering capability is configured
    When The capabilities section renders
    Then Engineering label displays with supporting content including summary

  Scenario: Verify Engineering relevant link is operable
    Given Engineering capability card renders
    When User clicks Engineering capability link/CTA
    Then Link routes to valid Engineering capability destination

  Scenario: Verify title required
    Given Engineering capability is configured
    When Section renders
    Then Engineering capability has non-empty title

  Scenario: Verify URL valid
    Given Engineering capability links are configured
    When User activates Engineering capability link
    Then Destination URL resolves successfully

  Scenario: Verify card matches visual system
    Given Engineering capability renders
    When User views card styling
    Then Card/panel matches capability visual system design
