Feature: Render partner logo rail/marquee

  Scenario: Verify all approved partner logos render
    Given Partner logos section renders
    When User views the partners
    Then All approved partners render: ServiceNow, Unity, OutSystems, Kore.ai, UiPath, ONYX, TriZetto, e6data, Magical, Health Samurai, Databricks, AWS, Anthropic

  Scenario: Verify partner logos have accessible names
    Given Partner logos render
    When Screen reader reads the section
    Then Each logo has meaningful accessible name or is marked decorative with adjacent text

  Scenario: Verify no duplicate for assistive technologies
    Given Marquee uses DOM duplication for looping effect
    When Screen reader reads the page
    Then Logical partner list does not announce duplicates

  Scenario: Verify missing logo handled
    Given A partner logo asset is unavailable
    When Partner section renders
    Then Fallback placeholder or text name displays without breaking layout

  Scenario: Verify transparent logo visible on background
    Given Partner has transparent logo
    When Logo renders on page background
    Then Logo has sufficient contrast or background treatment for visibility

  Scenario: Verify reduced motion for marquee
    Given User prefers reduced motion
    When Marquee animation is configured
    Then Animation is disabled or pauses; content remains accessible
