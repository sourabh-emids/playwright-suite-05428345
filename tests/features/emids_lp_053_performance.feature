Feature: Performance and Core Web Vitals

    @emids_lp_053
    Scenario: verify_critical_content_without_analytics_wait
        Given Page with analytics scripts configured
        When Page loads
        Then Critical content renders without waiting for analytics

    @emids_lp_053
    Scenario: verify_images_optimized
        Given Images on page
        When Images are served
        Then Images are optimized in format and size for viewport

    @emids_lp_053
    Scenario: verify_below_fold_lazy_loaded
        Given Below-the-fold media exists
        When Page loads
        Then Below-the-fold media is lazy-loaded where appropriate

    @emids_lp_053
    Scenario: verify_layout_shifts_minimized
        Given Page renders
        When Core Web Vitals metrics measured
        Then Layout shifts (CLS) are minimized

    @emids_lp_053
    Scenario: verify_third_party_async_deferred
        Given Third-party scripts exist
        When Page loads
        Then Third-party scripts use async/defer or consent gating as appropriate

    @emids_lp_053
    Scenario: verify_no_large_unoptimized_assets
        Given Assets are configured
        When Automated check validates
        Then No large unoptimized assets block rendering

    @emids_lp_053
    Scenario: verify_slow_network_handling
        Given User on slow network
        When Page loads
        Then Critical content renders progressively

    @emids_lp_053
    Scenario: verify_blocked_third_party_handling
        Given Third-party script blocked
        When Page loads
        Then Core content renders; blocked scripts handled gracefully

    @emids_lp_053
    Scenario: verify_cached_stale_asset_handling
        Given Stale asset in cache
        When Page loads
        Then Cache busting or version strategy prevents stale content

    @emids_lp_053
    Scenario: verify_large_viewport_image_optimization
        Given Large viewport sizes render
        When Images are served
        Then Images are appropriately sized for viewport dimensions

    @emids_lp_053
    Scenario: verify_web_vitals_telemetry_consent
        Given Performance metrics collection
        When User has not consented to telemetry
        Then Web Vitals/performance telemetry not collected

    @emids_lp_053
    Scenario: verify_no_sensitive_dimensions_logged
        Given Performance metrics logged
        When Logs are created
        Then No sensitive dimensions captured in logs
