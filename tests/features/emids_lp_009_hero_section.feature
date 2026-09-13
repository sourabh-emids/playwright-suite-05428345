Feature: Render hero messaging and visual

  Scenario: Verify one primary H1 is present
    Given The homepage loads
    When The user inspects the page heading structure
    Then Exactly one H1 element is present with content 'In Healthcare, Only Outcomes Matter'

  Scenario: Verify supporting content is readable
    Given The hero section renders
    When The user views hero eyebrow, body copy, and CTA
    Then All supporting content is visible and legible with appropriate contrast

  Scenario: Verify media has appropriate alternative handling
    Given The hero contains media (image/video)
    When The user views the page with screen reader or media fails to load
    Then Media has appropriate alt text or alternative content description

  Scenario: Verify CTA visible above fold on common desktop
    Given The page loads at standard desktop viewport
    When The user views the initial page without scrolling
    Then The hero CTA is visible before deep page scrolling

  Scenario: Verify H1 is non-empty and unique
    Given The hero section renders
    When The user inspects the H1 element
    Then H1 has non-empty content and no duplicate H1 exists elsewhere on the page

  Scenario: Verify media URL resolves
    Given The hero section is configured with media
    When The media resource loads
    Then Media URL resolves successfully without 404 error

  Scenario: Verify decorative media does not create redundant output
    Given Media is marked as decorative
    When Screen reader reads the page
    Then Decorative media does not create redundant or confusing screen reader output

  Scenario: Verify hero renders with slow media loading
    Given Network conditions are slow
    When Hero media loads slowly
    Then Text content remains available without waiting for media

  Scenario: Verify hero renders when media missing
    Given Hero media asset is unavailable
    When The page renders
    Then Hero content renders with fallback or gracefully degraded visual

  Scenario: Verify hero responsive at small viewport
    Given The user is on mobile viewport
    When The hero section renders
    Then Typography and media scale responsively without horizontal overflow
