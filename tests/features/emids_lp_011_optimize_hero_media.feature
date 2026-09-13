"""Feature: Optimize hero media loading (emids_lp_011)."""
Feature: Optimize hero media loading

    @emids_lp_011 @hero @performance
    Scenario: Text available when media fails
        Given Hero media fails to load
        When Page renders
        Then Text content remains visible and accessible

    @emids_lp_011 @hero @performance
    Scenario: Media dimensions reserved to avoid layout shift
        Given Hero includes media element
        When Page loads before media fully renders
        Then Space is reserved for media
        And No unexpected layout shift occurs

    @emids_lp_011 @hero @performance
    Scenario: Appropriately sized assets served
        Given User views hero media
        When Network inspector examines asset requests
        Then Media uses optimized format/size for viewport
        And srcset/sizes attributes used where applicable

    @emids_lp_011 @hero @performance
    Scenario: Hero LCP not lazy loaded
        Given Hero includes primary LCP image
        When Page loads
        Then Principal LCP asset is not lazy-loaded
        And Loads eagerly to optimize LCP metric

    @emids_lp_011 @hero @performance
    Scenario: CDN timeout handling
        Given CDN is slow or times out
        When Hero media loads from CDN
        Then Fallback or graceful degradation occurs
        And Text content remains available

    @emids_lp_011 @hero @performance
    Scenario: Unsupported format handling
        Given Media uses unsupported browser format
        When Page renders
        Then Fallback or alternative is displayed
        And Page remains functional

    @emids_lp_011 @hero @performance
    Scenario: Low bandwidth media loading
        Given User is on low-bandwidth connection
        When Hero media attempts to load
        Then Appropriate sized or compressed asset is served
        And Page remains usable
