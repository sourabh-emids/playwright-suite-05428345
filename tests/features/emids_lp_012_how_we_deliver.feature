"""Feature: Render How We Deliver section (emids_lp_012)."""
Feature: Render How We Deliver section

    @emids_lp_012 @how-we-deliver
    Scenario: Section renders with required elements
        Given User scrolls to How We Deliver section
        When Section becomes visible
        Then Section heading, supporting explanation, visual/content elements, and CTA render in intended sequence

    @emids_lp_012 @how-we-deliver
    Scenario: Required content fields non-empty
        Given How We Deliver section renders
        When User examines content
        Then All required fields (title, body, CTA) contain content and are non-empty

    @emids_lp_012 @how-we-deliver
    Scenario: Heading hierarchy logical
        Given User examines page heading structure
        When User navigates through headings
        Then Heading levels follow logical hierarchy (H1 > H2 > H3)
        And No skipped levels where avoidable

    @emids_lp_012 @how-we-deliver @accessibility
    Scenario: Section accessible
        Given User with assistive technology views How We Deliver section
        When Section content is announced
        Then All content is properly labeled and accessible

    @emids_lp_012 @how-we-deliver
    Scenario: Missing media handling
        Given How We Deliver section visual is unavailable
        When Page renders
        Then Section renders with available content
        And Missing media does not break layout

    @emids_lp_012 @how-we-deliver @responsive
    Scenario: Long copy handling
        Given How We Deliver section contains long body copy
        When Page renders on narrow viewport
        Then Copy reflows appropriately
        And No overflow or truncation
