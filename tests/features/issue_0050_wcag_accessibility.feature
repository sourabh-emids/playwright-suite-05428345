Feature: Meet WCAG 2.1 AA accessibility target

  Scenario: Keyboard access to all interactive elements
    Given User navigates page using keyboard only
    When Tabbing through page
    Then All interactive elements reachable and operable via keyboard

  Scenario: Visible focus maintained
    Given User tabs through page
    When Focus indicator check
    Then Focus indicator visible on all interactive elements

  Scenario: Semantic landmarks identifiable
    Given Accessibility test or screen reader
    When Checking landmarks
    Then header, main, nav, footer landmarks properly identified

  Scenario: Sufficient color contrast ratios
    Given Contrast testing
    When Checking text against background
    Then Text meets 4.5:1 ratio for normal text, 3:1 for large text

  Scenario: Meaningful alt text on images
    Given Screen reader user encounters image
    When Reading alt text
    Then Images have meaningful alt text; decorative images have empty alt

  Scenario: Accessible names on interactive elements
    Given Accessibility audit
    When Checking accessible names
    Then All buttons and links have descriptive accessible names

  Scenario: 200% zoom support
    Given User sets browser zoom to 200%
    When Page renders
    Then Content fully accessible without horizontal scrolling

  Scenario: Reflow support at 320px width
    Given User views at 320px viewport width
    When Page renders
    Then Content reflows; no horizontal scrolling required

  Scenario: Form errors accessible
    Given User submits form with errors
    When Error messages display
    Then Errors associated with fields; announced by screen reader

  Scenario: Reduced motion preference respected
    Given User has prefers-reduced-motion
    When Page renders
    Then Animations reduced or disabled

  Scenario: Media alternatives provided
    Given Video or audio content present
    When Checking alternatives
    Then Captions or transcripts available where required

  Scenario: Not relying on color alone
    Given Status or information conveyed via color
    When Testing color independence
    Then Information not conveyed by color alone; additional cues provided

  Scenario: Touch targets minimum 44x44 CSS pixels
    Given Mobile touch testing
    When Checking interactive element sizes
    Then Touch targets meet minimum size requirement

  Scenario: Screen reader navigation logical
    Given Screen reader user navigates page
    When Reading content flow
    Then Content announced in logical order matching visual order

  Scenario: Windows High Contrast mode supported
    Given User enables Windows High Contrast
    When Page renders
    Then Content remains visible and distinguishable

  Scenario: Forced colors mode supported
    Given User enables forced colors
    When Page renders
    Then Content renders with system colors; styles adapt appropriately
