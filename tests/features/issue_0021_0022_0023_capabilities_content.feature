Feature: AI, Engineering, and Platforms capability content rendering

  Scenario: AI label and supporting content render
    Given User views Capabilities section
    When Page renders
    Then AI label and supporting content render in the AI capability panel

  Scenario: AI relevant link operable
    Given AI capability panel renders
    When User clicks AI link
    Then Link is operable and navigates to AI capability page

  Scenario: AI title required
    Given AI capability panel renders
    When User validates content
    Then AI title is present and non-empty

  Scenario: Engineering label and supporting content render
    Given User views Capabilities section
    When Page renders
    Then Engineering label and supporting content render in the Engineering capability panel

  Scenario: Engineering relevant link operable
    Given Engineering capability panel renders
    When User clicks Engineering link
    Then Link is operable and navigates to Engineering capability page

  Scenario: Engineering title required
    Given Engineering capability panel renders
    When User validates content
    Then Engineering title is present and non-empty

  Scenario: Platforms content renders
    Given User views Capabilities section
    When Page renders
    Then Platforms label and supporting content render in the Platforms capability panel

  Scenario: Platforms title required
    Given Platforms capability panel renders
    When User validates content
    Then Platforms title is present and matches approved taxonomy
