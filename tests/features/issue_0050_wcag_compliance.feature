Feature: WCAG 2.1 AA compliance

  Scenario: Keyboard access
    Given User navigates site using keyboard only
    When User interacts with page
    Then All functionality is accessible via keyboard

  Scenario: Visible focus
    Given User navigates with keyboard
    When Focus moves between elements
    Then Visible focus indicator is present on all interactive elements

  Scenario: Semantic landmarks
    Given User uses assistive technology
    When User identifies page regions
    Then Main, header, footer, and section landmarks are identifiable

  Scenario: Sufficient contrast
    Given User views page content
    When Color contrast is measured
    Then Text and interactive elements meet WCAG AA contrast ratios (4.5:1 normal text, 3:1 large text)

  Scenario: Meaningful alt text
    Given Images render on page
    When Screen reader encounters images
    Then Meaningful alt text is provided for informative images

  Scenario: Accessible names
    Given User uses screen reader
    When User encounters interactive elements
    Then All interactive elements have accessible names

  Scenario: 200% zoom support
    Given User sets browser zoom to 200%
    When User views page
    Then Content remains readable without horizontal scrolling

  Scenario: Reflow support
    Given User views page at 320px width
    When Page renders
    Then Content reflows without horizontal scrolling

  Scenario: Form errors accessible
    Given Form has validation errors
    When Errors occur
    Then Errors are accessible and programmatically determinable

  Scenario: Reduced motion handling
    Given User prefers reduced motion
    When Animations are present
    Then Motion is reduced or disabled

  Scenario: Media alternatives
    Given Video or audio content is present
    When User accesses media
    Then Alternatives are available

  Scenario: High zoom support
    Given User sets browser zoom high
    When User views page
    Then Content and functionality remain accessible

  Scenario: Screen reader navigation
    Given User uses screen reader
    When User navigates page
    Then Page is navigable and content is logically structured

  Scenario: Windows High Contrast support
    Given User has Windows High Contrast mode enabled
    When User views page
    Then Page remains functional with appropriate styling

  Scenario: Motion sensitivity support
    Given User has motion sensitivity
    When User views page
    Then Animations respect user preferences

  Scenario: Keyboard-only use
    Given User uses keyboard only
    When User completes page tasks
    Then All functionality is keyboard accessible
