Feature: Partner logo rail/marquee rendering

  Scenario: All approved partner logos render
    Given User views Partnerships section
    When Page renders
    Then All approved partner logos render: ServiceNow, Unity, OutSystems, Kore.ai, UiPath, ONYX, TriZetto, e6data, Magical, Health Samurai, Databricks, AWS, Anthropic

  Scenario: Partner logos have accessible names
    Given Partner logos render
    When User uses screen reader
    Then Each partner logo has meaningful accessible name via alt text or aria-label

  Scenario: Logical partner list for assistive technology
    Given DOM duplicates partner list for looping animation
    When User uses screen reader
    Then Partner list is not duplicated for assistive technologies

  Scenario: Logo assets required
    Given Partnerships section renders
    When Partner data is configured
    Then Logo assets are present for each partner

  Scenario: Alt text or accessibility label provided
    Given Partner logo renders
    When Logo is not treated as decorative
    Then Alt text or accessibility label is provided

  Scenario: Missing logo handling
    Given A partner logo asset is missing
    When Page renders
    Then Placeholder or fallback displays appropriately

  Scenario: Transparent logo visibility
    Given Partner has transparent logo
    When Logo renders on page background
    Then Logo remains visible with appropriate contrast/background

  Scenario: Reduced motion for marquee
    Given User prefers reduced motion
    When Marquee animation is active
    Then Animation is disabled or reduced
