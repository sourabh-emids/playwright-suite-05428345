Feature: Responsive layout across viewports

    @emids_lp_052
    Scenario: verify_no_horizontal_scroll_desktop
        Given Page renders at desktop viewport (1024px+)
        When User scrolls horizontally
        Then No unintended horizontal scrolling

    @emids_lp_052
    Scenario: verify_no_horizontal_scroll_tablet
        Given Page renders at tablet viewport (768px-1023px)
        When User scrolls horizontally
        Then No unintended horizontal scrolling

    @emids_lp_052
    Scenario: verify_no_horizontal_scroll_mobile
        Given Page renders at mobile viewport (320px+)
        When User scrolls horizontally
        Then No unintended horizontal scrolling

    @emids_lp_052
    Scenario: verify_typography_readable
        Given Page renders at various viewports
        When User views text content
        Then Typography remains readable at all supported sizes

    @emids_lp_052
    Scenario: verify_controls_not_overlapping
        Given Page renders at various viewports
        When Interactive elements display
        Then Controls do not overlap

    @emids_lp_052
    Scenario: verify_all_cards_sections_available
        Given Page renders at mobile viewport
        When User scrolls through content
        Then All cards/sections remain available

    @emids_lp_052
    Scenario: verify_images_aspect_ratio
        Given Images render at various viewports
        When Container resizes
        Then Images preserve aspect ratio

    @emids_lp_052
    Scenario: verify_320px_width_functional
        Given Page renders at 320 CSS px width
        When Content displays
        Then Content remains usable

    @emids_lp_052
    Scenario: verify_200_zoom_functional
        Given Page at 200% browser zoom
        When Content reflows
        Then Content remains usable where applicable

    @emids_lp_052
    Scenario: verify_very_long_text_handling
        Given Content contains very long text
        When Page renders at narrow viewport
        Then Text wraps without breaking layout

    @emids_lp_052
    Scenario: verify_landscape_phone_handling
        Given Phone in landscape orientation
        When Page renders
        Then Layout adapts appropriately

    @emids_lp_052
    Scenario: verify_tablet_split_screen_handling
        Given Tablet in split-screen mode
        When Page renders
        Then Layout adapts to reduced width
