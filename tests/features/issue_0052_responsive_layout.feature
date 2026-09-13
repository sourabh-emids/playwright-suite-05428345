Feature: Responsive layout across viewports

  Scenario: No horizontal scrolling at supported widths
    Given User views page at supported viewport widths
    When Page renders
    Then No unintended horizontal page scrolling occurs

  Scenario: Typography readable at all sizes
    Given User views page at various viewport widths
    When Page renders
    Then Typography remains readable

  Scenario: Controls do not overlap
    Given User views page at mobile width
    When Page renders
    Then Interactive controls do not overlap

  Scenario: All cards visible at all widths
    Given User views card sections at mobile width
    When Page renders
    Then All cards/sections remain available

  Scenario: Images preserve aspect ratio
    Given User views images at various viewport widths
    When Page renders
    Then Images preserve aspect ratio

  Scenario: 320px width supported
    Given User views page at 320px width
    When Page renders
    Then Page reflows appropriately and content is usable

  Scenario: 200% zoom support
    Given User sets browser zoom to 200%
    When Page renders
    Then Page reflows without horizontal scrolling and content is usable

  Scenario: Very long text handling
    Given Section contains very long text
    When Page renders at narrow viewport
    Then Text wraps appropriately without breaking layout

  Scenario: Landscape phone handling
    Given User views page on phone in landscape
    When Page renders
    Then Page renders appropriately

  Scenario: Tablet split-screen handling
    Given User views page in split-screen mode on tablet
    When Page renders
    Then Page handles reduced width appropriately
