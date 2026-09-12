"""Feature file for Issue 0018 - Partner logo rail/marquee rendering."""
Feature: Partner logo rail/marquee rendering

  Scenario: All approved partner logos render
    Given A user views the Partnerships section
    When The section loads
    Then All approved partner logos render

  Scenario: Partner logos have meaningful accessible names
    Given A user using assistive technology views partner logos
    When Screen reader encounters logo elements
    Then Each logo has a meaningful accessible name or alt text

  Scenario: No duplicate announcements for assistive tech
    Given A user using assistive technology views the partner rail
    When DOM duplication is used for looping animation
    Then Logical partner list does not duplicate for assistive technologies

  Scenario: Missing logo handling
    Given A partner logo asset is missing
    When The page renders
    Then Fallback or placeholder is displayed; no broken image icons visible

  Scenario: Transparent logo visibility
    Given A partner has a transparent logo
    When The logo is displayed
    Then The logo remains visible on the background

  Scenario: Reduced motion for animation
    Given A user has prefers-reduced-motion enabled
    When The user views the partner logo marquee
    Then Continuous animation is disabled or meaningfully reduced
