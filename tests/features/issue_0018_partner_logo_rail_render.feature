Feature: Partner logo rail render
  # issue_0018

  Scenario: All approved partner logos render
    Given The Partnerships section is rendered
    When Visual inspection confirms logos
    Then Logos display for: ServiceNow, Unity, OutSystems, Kore.ai, UiPath, ONYX, TriZetto, e6data, Magical, Health Samurai, Databricks, AWS, and Anthropic

  Scenario: Partner logos have accessible names
    Given Partner logos are rendered
    When Accessibility testing runs
    Then Each logo has an alt attribute or aria-label providing meaningful accessible name

  Scenario: Assistive tech receives logical partner list
    Given A screen reader user navigates the Partnerships section
    When The user encounters the partner logos
    Then The content is not announced multiple times due to DOM duplication for looping animation

  Scenario: Logo assets are accessible
    Given Partner logos are configured
    When Automated testing validates assets
    Then All logo image assets resolve successfully

  Scenario: Marquee animation works on supported devices
    Given The Partnerships section uses a marquee animation
    When The page renders on devices supporting animation
    Then The animation plays smoothly
