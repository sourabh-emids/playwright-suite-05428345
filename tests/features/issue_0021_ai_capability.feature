Feature: Render AI capability content

  Scenario: AI label and supporting content render
    Given User views AI capability card/panel
    When Checking content
    Then AI title and supporting summary text are visible

  Scenario: AI relevant link is operable
    Given User clicks AI capability link
    When Navigation triggered
    Then User navigates to valid AI capability destination

  Scenario: AI card matches visual system
    Given User views AI card alongside other capability cards
    When Comparing visual styling
    Then AI card follows same card/panel visual system as Engineering and Platforms cards

  Scenario: AI title required field validation
    Given CMS validation
    When Checking required fields
    Then AI title is present and non-empty

  Scenario: AI URL valid and resolves
    Given User clicks AI link
    When URL requested
    Then AI destination URL is valid and resolves successfully

  Scenario: AI card broken media handled
    Given AI card has optional media that fails
    When Page renders
    Then Text content remains; card is functional without broken media
