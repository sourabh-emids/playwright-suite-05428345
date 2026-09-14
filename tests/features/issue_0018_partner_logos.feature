Feature: Render partner logo rail/marquee

  Scenario: All approved partner logos render
    Given User views partner section
    When Counting logos
    Then All thirteen approved logos are visible: ServiceNow, Unity, OutSystems, Kore.ai, UiPath, ONYX, TriZetto, e6data, Magical, Health Samurai, Databricks, AWS, and Anthropic

  Scenario: Partner logos have meaningful accessible names
    Given User or screen reader reads partner section
    When Checking accessible names
    Then Each logo has descriptive alt text or accessibility label identifying the partner

  Scenario: Logical partner list not duplicated for assistive tech
    Given DOM uses duplication for looping animation
    When Screen reader navigates partner section
    Then Partners are not announced multiple times due to animation loop

  Scenario: Logo asset required for each partner
    Given Partner configuration exists
    When Checking logo rendering
    Then Each partner displays its logo asset; missing logo is flagged

  Scenario: Alt text required for non-decorative logos
    Given Partner logo is not decorative
    When Checking alt attribute
    Then Logo has alt text or partner name is otherwise announced

  Scenario: Partner section without partner text uses decorative treatment
    Given Partner logos have adjacent partner names
    When Checking alt attributes
    Then Logos with adjacent text may be treated as decorative with empty alt

  Scenario: Transparent logo visible on background
    Given Partner has transparent PNG logo
    When Logo renders on page background
    Then Logo maintains sufficient visibility/contrast against background

  Scenario: Reduced motion preference for marquee
    Given User has prefers-reduced-motion
    When Marquee animation would run
    Then Animation pauses or reduces to static display
