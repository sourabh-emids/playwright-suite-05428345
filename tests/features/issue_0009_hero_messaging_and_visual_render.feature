Feature: Hero messaging and visual render
  # issue_0009

  Scenario: Hero displays primary H1 heading
    Given The homepage has fully loaded
    When Screen reader or automated tool analyzes the hero section
    Then Exactly one primary H1 is present containing 'In Healthcare, Only Outcomes Matter'

  Scenario: Supporting content is readable
    Given The hero section is rendered
    When Visual inspection confirms content presence
    Then Eyebrow text, body copy, and supporting elements are visible and readable

  Scenario: Hero media has alternative handling
    Given Hero visual assets are configured
    When The media fails to load or is unavailable
    Then Alternative content or text is available and the page remains usable

  Scenario: Hero CTA visible above fold on desktop
    Given The page loads on a common desktop viewport
    When The page renders without scrolling
    Then The hero CTA is visible in the initial viewport

  Scenario: H1 is non-empty and unique
    Given The page DOM is analyzed
    When Automated testing checks heading elements
    Then The H1 contains non-empty content and is the only H1 on the page

  Scenario: Media URL resolves successfully
    Given Hero media is configured
    When Automated testing validates the media URL
    Then The media URL resolves to accessible content
