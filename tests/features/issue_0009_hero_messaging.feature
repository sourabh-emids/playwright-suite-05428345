Feature: Render hero messaging and visual

  Scenario: Hero contains single primary H1
    Given User views the homepage hero section
    When Checking heading structure
    Then Exactly one H1 element exists containing 'In Healthcare, Only Outcomes Matter'

  Scenario: Supporting content is readable
    Given User views hero section
    When Reading supporting copy and eyebrow text
    Then Body copy is legible and properly styled

  Scenario: Hero media has alternative text handling
    Given Hero contains image or video media
    When Page is read by screen reader or image fails to load
    Then Media has appropriate alt text or aria-label; decorative media does not create redundant output

  Scenario: Hero CTA visible above fold on common desktop sizes
    Given User views hero on standard desktop viewport (1280x720 or larger)
    When Page loads without scrolling
    Then Primary CTA button is visible above the fold

  Scenario: Hero H1 is non-empty and unique
    Given User validates heading semantics
    When Checking H1 content
    Then H1 contains text content and is the only H1 on the page

  Scenario: Media URL resolves successfully
    Given Hero contains media asset
    When Media URL is requested
    Then Media asset URL resolves to valid resource

  Scenario: Long copy handles gracefully in hero
    Given Hero content contains extended copy
    When Page renders at various viewports
    Then Long copy does not cause layout break or overlap CTA

  Scenario: Small viewport hero renders correctly
    Given User views hero on mobile viewport
    When Page renders at 320px width
    Then Hero text and media scale appropriately without horizontal scroll

  Scenario: Reduced motion affects hero animation
    Given User has prefers-reduced-motion enabled
    When Hero has animated elements
    Then Animation is reduced or disabled per user preference
