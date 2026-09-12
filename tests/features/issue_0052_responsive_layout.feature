"""Feature file for Issue 0052 - Responsive layout across viewports."""
Feature: Responsive layout across viewports

  Scenario: No horizontal scrolling at supported widths
    Given User views page at desktop, tablet, and mobile widths
    When Viewport changes to each supported width
    Then No unintended horizontal scrolling occurs

  Scenario: Typography remains readable
    Given User views page at mobile width (320px)
    When Text is rendered
    Then Typography remains readable at all supported widths

  Scenario: Controls do not overlap
    Given User views page at narrow viewport
    When Interactive elements are rendered
    Then Controls do not overlap

  Scenario: All cards/sections remain available
    Given User views page at various viewport widths
    When All sections are loaded
    Then All cards and sections remain accessible and available

  Scenario: Images preserve aspect ratio
    Given User views page at various widths
    When Images are rendered
    Then Images preserve aspect ratio

  Scenario: Content usable at 320px width
    Given User views page at 320 CSS px width
    When Content is rendered
    Then Content is usable without horizontal scrolling

  Scenario: Browser zoom 200% without regression
    Given User sets browser zoom to 200%
    When Page renders
    Then Layout reflows without overlap or loss of functionality

  Scenario: Very long text handling at mobile
    Given Content contains text exceeding expected length
    When Page renders at mobile width
    Then Text wraps gracefully without breaking layout

  Scenario: Landscape phone viewport
    Given User views page on phone in landscape orientation
    When Page renders
    Then Layout adapts appropriately

  Scenario: Tablet split-screen viewport
    Given User views page on tablet in split-screen mode
    When Page renders
    Then Layout adapts to available width without horizontal scroll
