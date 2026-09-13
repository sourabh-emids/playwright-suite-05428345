Feature: Render Insights section and six cards

    @emids_lp_026
    Scenario: verify_six_cards_render
        Given Insights section renders
        When User views cards
        Then Exactly six cards render with content type, title, image where configured, and Download or Read More action

    @emids_lp_026
    Scenario: verify_cards_accessible_at_all_breakpoints
        Given Insights section renders
        When User views at desktop, tablet, and mobile breakpoints
        Then Cards remain accessible without content hidden or broken layout

    @emids_lp_026
    Scenario: verify_published_content_only
        Given Six insights are configured
        When Page renders
        Then Only published content appears; unpublished items are excluded

    @emids_lp_026
    Scenario: verify_title_and_url_required
        Given Insight card data
        When Automated check validates fields
        Then Title and URL are required for each card

    @emids_lp_026
    Scenario: verify_action_label_matches_content_flow
        Given Insight cards render
        When Automated check validates CTA labels
        Then Action labels (Download/Read More) match content flow (eBook/Article)

    @emids_lp_026
    Scenario: verify_responsive_card_grid
        Given Insights section renders on various viewports
        When Content reflows
        Then Cards display in responsive grid/rail with consistent heights where practical

    @emids_lp_026
    Scenario: verify_resource_unpublished_handling
        Given One insight resource is unpublished
        When Section renders
        Then Only five published cards display; no broken links

    @emids_lp_026
    Scenario: verify_missing_image_handling
        Given Insight card image is missing
        When Card renders
        Then Card displays with placeholder or gracefully without image

    @emids_lp_026
    Scenario: verify_long_title_handling
        Given Insight title is at maximum length
        When Card renders at mobile width
        Then Title truncates or wraps appropriately

    @emids_lp_026
    Scenario: verify_url_changes_handling
        Given Insight resource URL changes
        When Page renders with stale URL
        Then Redirect handling or validation catches broken URL
