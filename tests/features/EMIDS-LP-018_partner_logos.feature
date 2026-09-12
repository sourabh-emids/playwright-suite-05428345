Feature: Partner logo rail/marquee rendering

  Scenario: All approved partner logos render
    Given Partnership section
    When Logos are inspected
    Then All 13 logos are present: ServiceNow, Unity, OutSystems, Kore.ai, UiPath, ONYX, TriZetto, e6data, Magical, Health Samurai, Databricks, AWS, Anthropic

  Scenario: Logos have meaningful accessible names
    Given Partner logo elements
    When Accessibility is checked
    Then Each logo has meaningful alt text or accessibility label

  Scenario: Logical list for assistive technology
    Given Partner logos using DOM duplication for looping animation
    When Read by screen reader
    Then Partner list is not duplicated and announced logically once

  Scenario: Logo asset required
    Given Partner logo configuration
    When Asset availability is checked
    Then Logo asset is present and loads

  Scenario: Missing logo handling
    Given Edge case where logo asset is missing
    When Page renders
    Then Fallback or placeholder is shown appropriately

  Scenario: Reduced motion for animation
    Given Marquee animation is used
    When User prefers reduced motion
    Then Animation stops or reduces meaningfully
