Feature: Five audience entries render
  # issue_0024

  Scenario: All five audiences are visible
    Given The Who We Serve section is rendered
    When Visual inspection confirms content
    Then Payer, Provider, HealthTech, Life Sciences, and Consumer audiences are displayed

  Scenario: Each Explore action routes correctly
    Given Each audience entry has an Explore CTA
    When A user clicks an Explore action
    Then Navigation routes to the canonical segment page (/segments/payer/, /segments/provider/, etc.)

  Scenario: Explore actions work on keyboard
    Given The Who We Serve section is rendered
    When Keyboard navigation testing runs
    Then All Explore CTAs are keyboard accessible

  Scenario: Explore actions work on touch
    Given The page is viewed on a touch device
    When Touch testing validates interaction
    Then All Explore CTAs are touch accessible

  Scenario: Exactly five audiences for this content version
    Given The Who We Serve section is rendered
    When Automated testing counts audience entries
    Then Exactly five audience entries are present

  Scenario: Audience URLs are canonical
    Given Audience Explore links are rendered
    When Automated testing validates URLs
    Then All URLs follow canonical patterns
