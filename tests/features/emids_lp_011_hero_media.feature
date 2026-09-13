Feature: Optimize hero media loading

    @emids_lp_011
    Scenario: verify_text_available_if_media_fails
        Given Hero media fails to load
        When Page renders
        Then Text content remains available and page is fully usable

    @emids_lp_011
    Scenario: verify_media_dimensions_reserved
        Given Hero contains media with known dimensions
        When Page loads without media
        Then Layout space is reserved to avoid cumulative layout shift (CLS)

    @emids_lp_011
    Scenario: verify_appropriately_sized_assets_served
        Given Hero media is requested
        When Server responds with image
        Then Image is appropriately sized for viewport (srcset/sizes used where applicable)

    @emids_lp_011
    Scenario: verify_lcp_asset_not_lazy_loaded
        Given Hero contains primary LCP (Largest Contentful Paint) media
        When Page loads
        Then LCP asset is not lazy-loaded as it would harm LCP metric

    @emids_lp_011
    Scenario: verify_poster_alt_provided
        Given Hero contains video media
        When Automated check validates video element
        Then Poster image and alt text are provided for accessibility

    @emids_lp_011
    Scenario: verify_cdn_timeout_handling
        Given CDN serving hero media times out
        When Page renders
        Then Fallback is shown and content remains accessible

    @emids_lp_011
    Scenario: verify_unsupported_format_handling
        Given Browser does not support media format
        When Media attempts to load
        Then Fallback or alternative is provided

    @emids_lp_011
    Scenario: verify_low_bandwidth_media_loading
        Given User is on low-bandwidth connection
        When Page loads
        Then Optimized lower-resolution media is served or loads gracefully
