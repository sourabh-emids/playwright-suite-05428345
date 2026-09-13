Feature: Render How We Deliver section

    @emids_lp_012
    Scenario: verify_section_sequence_and_accessibility
        Given Page renders 'How We Deliver' section
        When Section content is displayed
        Then Section heading, supporting explanation, visual/content elements, and CTA render in intended sequence and are accessible

    @emids_lp_012
    Scenario: verify_required_fields_not_empty
        Given 'How We Deliver' section renders
        When Automated check validates content fields
        Then Required content fields (title, body, CTA) are not empty

    @emids_lp_012
    Scenario: verify_heading_hierarchy_logical
        Given Page contains multiple sections with headings
        When Automated check scans heading levels
        Then Heading hierarchy follows logical order without skipped levels where avoidable

    @emids_lp_012
    Scenario: verify_responsive_content_block
        Given Section renders on mobile viewport
        When Content reflows
        Then Content block adapts responsively following hero section

    @emids_lp_012
    Scenario: verify_missing_media_handling
        Given Section media fails to load or is not configured
        When Section renders
        Then Content remains accessible without broken image placeholders

    @emids_lp_012
    Scenario: verify_long_copy_handling
        Given Section body copy is at maximum length
        When Page renders at mobile width
        Then Copy wraps appropriately without breaking layout

    @emids_lp_012
    Scenario: verify_section_without_cta_handling
        Given CTA field is missing from section data
        When Section renders
        Then Section renders without CTA or shows placeholder based on requirements
