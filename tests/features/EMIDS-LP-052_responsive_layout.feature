Feature: Responsive layout across common viewports

  Scenario: No horizontal scrolling at any viewport
    Given All supported viewport widths
    When Layout is tested
    Then No unintended horizontal scrolling occurs

  Scenario: Typography readable at all sizes
    Given Text content across viewport sizes
    When Typography is verified
    Then Typography remains readable at all supported widths

  Scenario: Controls do not overlap
    Given Interactive elements at various widths
    When Layout is verified
    Then Controls do not overlap at any breakpoint

  Scenario: All cards/sections remain available
    Given Responsive layout across breakpoints
    When Content is verified
    Then All cards and sections remain available and accessible

  Scenario: Images preserve aspect ratio
    Given Images at different viewport widths
    When Images render
    Then Images preserve aspect ratio

  Scenario: 320px width support
    Given Narrow mobile viewport at 320 CSS px
    When Page renders
    Then Content remains usable

  Scenario: 200% zoom layout stability
    Given Browser zoom at 200%
    When Layout is verified
    Then Layout remains stable without horizontal scroll
