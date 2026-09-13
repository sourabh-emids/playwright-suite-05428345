Feature: Platforms capability content render
  # issue_0023

  Scenario: Platforms content renders correctly
    Given The Platforms capability card/panel is rendered
    When Visual inspection runs
    Then The Platforms content is displayed with title and supporting elements

  Scenario: Labels use approved taxonomy consistently
    Given The Platforms capability is rendered
    When Labels are compared between navigation and body copy
    Then Labels use approved taxonomy consistently (e.g., 'Provider Platforms' vs body copy variants are reconciled)

  Scenario: Platforms link is operable
    Given The Platforms capability card/panel is rendered
    When The Platforms CTA or link is clicked
    Then Navigation to the Platforms capability destination occurs

  Scenario: Content governance prevents inconsistent synonyms
    Given The Platforms content is managed
    When Content is reviewed
    Then Inconsistent synonyms are avoided unless intentionally approved by content governance
