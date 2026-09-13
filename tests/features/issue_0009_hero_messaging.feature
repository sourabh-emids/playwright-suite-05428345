Feature: Hero messaging and visual rendering

  Scenario: One primary H1 present
    Given User navigates to Emids homepage
    When Page loads
    Then Exactly one primary H1 heading is present containing 'In Healthcare, Only Outcomes Matter'

  Scenario: Supporting content is readable
    Given Hero section is rendered
    When User views hero supporting copy
    Then Supporting content is readable with proper contrast and font sizing

  Scenario: Media has appropriate alternative handling
    Given Hero media (image/video) is present
    When User uses screen reader or media fails to load
    Then Alternative text or fallback content is provided appropriately

  Scenario: CTA visible before deep page scrolling on desktop
    Given User views Emids homepage on common desktop size (1280px+)
    When Page loads at default scroll position
    Then Hero CTA is visible without deep page scrolling

  Scenario: Eyebrow text renders
    Given Hero section is rendered
    When User views hero content
    Then Eyebrow text is present

  Scenario: Hero body copy renders
    Given Hero section is rendered
    When User views hero content
    Then Body copy is present and readable

  Scenario: H1 is non-empty and unique
    Given User views page source
    When User checks H1 elements
    Then H1 is non-empty and no duplicate H1 elements exist

  Scenario: Decorative media does not create redundant output
    Given Hero has decorative media
    When User uses screen reader
    Then Decorative media does not create redundant screen-reader output

  Scenario: Hero renders at small viewport
    Given User views Emids homepage at mobile width (375px)
    When Page renders
    Then Hero renders appropriately with responsive typography and media scaling

  Scenario: Reduced motion for hero
    Given User has prefers-reduced-motion enabled
    When Hero contains animations
    Then Animations are reduced or disabled
