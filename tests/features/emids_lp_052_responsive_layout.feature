Feature: Provide responsive layout across common viewports

  Scenario: Verify no horizontal scrolling at supported widths
    Given Page renders at supported viewport widths (320px to 1920px)
    When User views without scrolling horizontally
    Then Content fits within viewport without requiring horizontal scroll

  Scenario: Verify typography remains readable
    Given Page renders at various viewport sizes
    When User views text content
    Then Typography scales appropriately; text remains legible at all breakpoints

  Scenario: Verify controls do not overlap
    Given Page renders at narrow viewport
    When User views interactive controls
    Then Controls do not overlap or obscure each other

  Scenario: Verify all cards/sections remain available
    Given Page renders on mobile
    When User scrolls through page
    Then All sections and cards are visible and accessible; no content hidden off-screen

  Scenario: Verify images preserve aspect ratio
    Given Page renders with images
    When User views at different viewport sizes
    Then Images scale proportionally; aspect ratio is preserved

  Scenario: Verify 320px width supported
    Given Page renders at 320 CSS pixels width
    When User views content
    Then Content reflows to single column; all functionality preserved

  Scenario: Verify very long text handled
    Given Content has very long text strings (words, URLs)
    When Page renders at mobile viewport
    Then Text wraps or truncates gracefully without breaking layout

  Scenario: Verify browser zoom at 200% supported
    Given User has browser zoom at 200%
    When Page renders
    Then Content remains usable; reflows appropriately

  Scenario: Verify landscape phone handled
    Given Phone is in landscape orientation
    When Page renders
    Then Layout adapts appropriately for landscape proportions

  Scenario: Verify tablet split-screen handled
    Given Tablet is in split-screen or multitasking mode
    When Page renders
    Then Content reflows for reduced viewport width without breaking
