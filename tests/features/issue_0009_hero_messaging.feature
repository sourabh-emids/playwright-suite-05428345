"""Feature: Hero Messaging and Visual Rendering."""
Feature: Hero Messaging and Visual Rendering

  @issue_0009
  Scenario: primary_h1_present
    Given Hero section renders
    When Heading structure is checked
    Then Exactly one primary H1 is present with content 'In Healthcare, Only Outcomes Matter'

  @issue_0009
  Scenario: supporting_content_readable
    Given Hero section renders
    When Supporting content (eyebrow, body copy) is reviewed
    Then Supporting content is readable with appropriate contrast and font sizing

  @issue_0009
  Scenario: hero_media_alternative_handling
    Given Hero has visual media (image/video)
    When Page is rendered without media loading or via screen reader
    Then Media has appropriate alternative handling

  @issue_0009
  Scenario: hero_cta_visible_above_fold
    Given Hero section renders at common desktop viewport (1280x720)
    When User views page without scrolling
    Then Primary CTA is visible above/before deep page scrolling

  @issue_0009
  Scenario: hero_h1_unique_nonempty
    Given H1 content is validated
    When Page is checked for duplicate or empty H1
    Then H1 is non-empty and unique on page

  @issue_0009
  Scenario: hero_media_url_resolves
    Given Hero media is configured
    When Media URL is validated
    Then Media URL resolves successfully

  @issue_0009
  Scenario: slow_media_handling
    Given Media network connection is slow
    When Page loads
    Then Text content remains available even if media delays

  @issue_0009
  Scenario: missing_image_video_handling
    Given Hero image/video fails to load
    When Page renders
    Then Fallback is provided and hero content remains accessible

  @issue_0009
  Scenario: long_hero_copy_handling
    Given Hero has unusually long body copy
    When Hero renders at viewport
    Then Layout accommodates content without breaking

  @issue_0009
  Scenario: small_viewport_hero
    Given Hero renders at mobile viewport (320px width)
    When Content is reviewed
    Then Hero content is fully visible and readable

  @issue_0009
  Scenario: reduced_motion_hero_media
    Given User has prefers-reduced-motion enabled
    When Hero renders with animated media
    Then Animated media respects reduced motion preference
