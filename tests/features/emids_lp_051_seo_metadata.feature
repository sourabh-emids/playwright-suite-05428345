Feature: SEO metadata and crawlable structure

    @emids_lp_051
    Scenario: verify_unique_title
        Given Page renders
        When Automated SEO check scans
        Then Page has unique title tag

    @emids_lp_051
    Scenario: verify_meta_description_present
        Given Page renders
        When Automated SEO check scans
        Then Meta description is present and non-empty

    @emids_lp_051
    Scenario: verify_canonical_url_set
        Given Page renders
        When Automated SEO check validates
        Then Canonical URL is set correctly pointing to primary URL

    @emids_lp_051
    Scenario: verify_primary_text_crawlable
        Given Page renders
        When Search engine crawler analyzes
        Then Primary text is server-rendered and crawlable (not JS-dependent)

    @emids_lp_051
    Scenario: verify_social_preview_metadata
        Given Page renders
        When Social platforms fetch preview
        Then Open Graph and Twitter metadata configured

    @emids_lp_051
    Scenario: verify_headings_reflect_topic
        Given Page headings render
        When Crawler analyzes heading structure
        Then Headings reflect page topic appropriately

    @emids_lp_051
    Scenario: verify_single_canonical_homepage
        Given Homepage URL variations exist
        When Canonical is set
        Then One canonical homepage URL is defined

    @emids_lp_051
    Scenario: verify_no_duplicate_title_tags
        Given Page HTML renders
        When Automated check validates
        Then No duplicate conflicting title tags exist

    @emids_lp_051
    Scenario: verify_missing_og_image_handling
        Given Social metadata configured but image missing
        When Social platform fetches
        Then Fallback or error handling; page still renders

    @emids_lp_051
    Scenario: verify_duplicate_canonical_handling
        Given Multiple canonical references exist
        When Crawler analyzes
        Then No conflicting canonical references

    @emids_lp_051
    Scenario: verify_js_critical_content_handling
        Given Critical content requires JavaScript
        When Crawler without JS accesses
        Then Critical content is server-rendered or gracefully handled
