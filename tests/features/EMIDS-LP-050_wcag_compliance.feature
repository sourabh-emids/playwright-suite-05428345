Feature: WCAG 2.1 AA compliance across landing page

  Scenario: Keyboard access for all interactive elements
    Given All interactive page elements
    When Keyboard-only navigation is tested
    Then All elements are accessible via keyboard

  Scenario: Visible focus indicators
    Given Focused elements
    When Elements receive focus
    Then Visible focus indicator is present

  Scenario: Semantic landmarks identified
    Given Page structure
    When Landmarks are verified
    Then Semantic landmarks (main, header, nav, footer) are present

  Scenario: Sufficient color contrast
    Given Text and background combinations
    When Contrast is measured
    Then Color contrast meets WCAG 2.1 AA requirements

  Scenario: Meaningful alt text for images
    Given Images on page
    When Alt text is verified
    Then Images have meaningful alt text or are marked as decorative

  Scenario: Accessible names for interactive elements
    Given Buttons, links, form controls
    When Accessibility is verified
    Then All interactive elements have accessible names

  Scenario: 200% zoom and reflow support
    Given Browser zoom set to 200%
    When Page is tested
    Then Content reflows without horizontal scrolling and remains usable

  Scenario: Form error identification
    Given Form validation errors
    When Errors occur
    Then Errors are properly identified and associated with fields

  Scenario: Reduced motion handling
    Given User prefers reduced motion
    When Animations would run
    Then Motion is reduced appropriately

  Scenario: Media alternatives provided
    Given Video and animated media
    When Media is present
    Then Alternatives are provided for non-text content

  Scenario: High zoom testing
    Given Browser zoom at high percentage
    When Page is tested
    Then Content remains accessible and usable

  Scenario: Windows High Contrast support
    Given Windows High Contrast mode
    When Page renders
    Then Content and controls remain visible and distinguishable
