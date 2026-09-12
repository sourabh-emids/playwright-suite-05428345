Feature: Hero messaging and visual rendering

  Scenario: Hero renders with primary H1
    Given The homepage hero section
    When Content is inspected
    Then Exactly one primary H1 is present containing 'In Healthcare, Only Outcomes Matter'

  Scenario: Supporting content is readable
    Given The hero section
    When Body copy is reviewed
    Then Supporting copy is present and readable

  Scenario: Hero media has alternative handling
    Given The hero visual media
    When Media fails to load or is read by screen reader
    Then Alternative text or fallback is provided; decorative media does not create redundant screen-reader output

  Scenario: CTA visible above deep page scrolling on desktop
    Given Common desktop viewport sizes
    When Page loads and user scrolls to find CTA
    Then Hero CTA is visible without requiring deep page scrolling

  Scenario: Hero content at small viewport
    Given Mobile viewport width
    When Hero section renders
    Then Content remains readable and media scales appropriately

  Scenario: Hero with reduced motion preference
    Given User prefers reduced motion
    When Hero animations are present
    Then Motion effects are reduced appropriately
