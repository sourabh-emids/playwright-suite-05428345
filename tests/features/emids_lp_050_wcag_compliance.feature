Feature: Meet WCAG 2.1 AA target across landing page

  Scenario: Verify keyboard access for all interactive elements
    Given User uses keyboard only to navigate
    When User tabs through page
    Then All interactive elements are reachable and operable via keyboard

  Scenario: Verify visible focus maintained
    Given User tabs through interactive elements
    When Focus moves between elements
    Then Visible focus indicator is present on all interactive elements

  Scenario: Verify semantic landmarks identifiable
    Given Page renders
    When User or assistive technology inspects page structure
    Then Header, main, nav, footer, and other landmarks are properly identified

  Scenario: Verify sufficient color contrast
    Given Page renders with text and interactive elements
    When Contrast is measured
    Then Text and interactive elements meet 4.5:1 contrast ratio (AA standard)

  Scenario: Verify meaningful alt text on images
    Given Page contains images
    When Screen reader reads images
    Then Informative images have meaningful alt text; decorative images are marked appropriately

  Scenario: Verify accessible names on interactive elements
    Given Interactive elements render (buttons, links, controls)
    When Screen reader or keyboard user accesses elements
    Then Each element has an accessible name that describes its purpose

  Scenario: Verify 200% zoom supported
    Given User has browser zoom at 200%
    When Page renders
    Then Content remains usable; no horizontal scrolling required

  Scenario: Verify reflow supported at 320px
    Given Viewport is 320 CSS pixels wide
    When Page renders
    Then Content reflows to single column; all content accessible without horizontal scrolling

  Scenario: Verify form errors are accessible
    Given Form validation fails
    When User submits invalid form
    Then Error messages are associated with fields; accessible to screen readers

  Scenario: Verify reduced motion handled
    Given User prefers reduced motion
    When Page renders with animations
    Then Animations are reduced or disabled per user preference

  Scenario: Verify media alternatives provided
    Given Page contains video or audio content
    When User accesses media
    Then Captions, transcripts, or audio descriptions are available where applicable

  Scenario: Verify Windows High Contrast supported
    Given User has Windows High Contrast or forced colors enabled
    When Page renders
    Then Content remains visible and distinguishable; colors not sole differentiator

  Scenario: Verify not reliant on color alone
    Given Page uses color to convey information
    When User views content without color perception
    Then Information is conveyed through additional means (text, icons, patterns)
