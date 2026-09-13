Feature: Render hero messaging and visual

    @emids_lp_009
    Scenario: verify_single_h1_present
        Given Page renders hero section
        When Automated check scans heading hierarchy
        Then Exactly one H1 is present on the page

    @emids_lp_009
    Scenario: verify_hero_title_content
        Given Hero section renders
        When User views H1 content
        Then H1 displays 'In Healthcare, Only Outcomes Matter' as primary message

    @emids_lp_009
    Scenario: verify_h1_non_empty_unique
        Given H1 element exists
        When Automated check validates H1
        Then H1 is non-empty and unique on the page

    @emids_lp_009
    Scenario: verify_supporting_content_readable
        Given Hero section renders
        When User views supporting copy
        Then Supporting content is readable with appropriate contrast and font sizing

    @emids_lp_009
    Scenario: verify_hero_cta_visible_above_fold
        Given Page loads on common desktop viewport (1280x720 minimum)
        When Hero section renders without scrolling
        Then CTA is visible above/before deep page scrolling

    @emids_lp_009
    Scenario: verify_media_alternative_handling
        Given Hero contains media (image/video)
        When Media fails to load or screen reader is used
        Then Appropriate alternative text or fallback is provided; decorative media has no redundant screen reader output

    @emids_lp_009
    Scenario: verify_hero_eyebrow_present
        Given Hero section renders
        When User views eyebrow content
        Then Eyebrow text is displayed above H1 if configured

    @emids_lp_009
    Scenario: verify_hero_media_url_resolves
        Given Hero media URL is configured
        When Automated check tests media endpoint
        Then Media URL resolves successfully

    @emids_lp_009
    Scenario: verify_slow_media_handling
        Given Network is slow or media is large
        When Page loads
        Then Text content remains available even if media takes longer to load

    @emids_lp_009
    Scenario: verify_long_copy_handling
        Given Hero copy contains maximum text length
        When Page renders on narrow viewport
        Then Copy wraps appropriately without breaking layout

    @emids_lp_009
    Scenario: verify_small_viewport_hero
        Given Page renders on mobile viewport (320px)
        When Hero section is displayed
        Then Hero remains readable and CTA remains accessible

    @emids_lp_009
    Scenario: verify_hero_reduced_motion
        Given User prefers reduced motion
        When Hero with animated elements renders
        Then Animation is reduced or static fallback is shown
