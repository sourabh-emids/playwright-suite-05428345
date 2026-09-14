Feature: Render Engineering capability content

  Scenario: Engineering label and supporting content render
    Given User views Engineering capability card
    When Checking content
    Then Engineering title and supporting summary text are visible

  Scenario: Engineering relevant link is operable
    Given User clicks Engineering capability link
    When Navigation triggered
    Then User navigates to valid Engineering capability destination

  Scenario: Engineering card matches visual system
    Given User views Engineering card
    When Comparing styling
    Then Card follows same visual pattern as AI and Platforms cards

  Scenario: Engineering title required validation
    Given Content validation
    When Checking required fields
    Then Engineering title field is populated

  Scenario: Engineering destination valid
    Given Engineering capability URL
    When Checking validity
    Then URL is valid internal path and resolves
