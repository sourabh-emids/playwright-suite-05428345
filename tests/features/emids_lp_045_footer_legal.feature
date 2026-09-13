Feature: Render footer legal navigation

    @emids_lp_045
    Scenario: verify_each_legal_link_descriptive
        Given Footer legal links render
        When User views link text
        Then Each legal link has descriptive text (Privacy Policy, Cookie Policy, Accessibility Statement, other approved legal links)

    @emids_lp_045
    Scenario: verify_legal_links_valid_destinations
        Given Legal link URLs are configured
        When Automated check tests URLs
        Then All legal URLs return successful responses and use HTTPS

    @emids_lp_045
    Scenario: verify_legal_links_visible_focus_state
        Given User focuses on legal links via keyboard
        When Focus is on legal navigation items
        Then Visible focus state is displayed

    @emids_lp_045
    Scenario: verify_labels_not_blank
        Given Legal link labels are configured
        When Automated check validates
        Then No labels are blank or empty

    @emids_lp_045
    Scenario: verify_multi_column_responsive_footer
        Given Footer renders at various viewport sizes
        When Layout reflows
        Then Multi-column/stacked responsive footer works at all sizes

    @emids_lp_045
    Scenario: verify_legal_page_moved_handling
        Given Legal page has been moved
        When User clicks legal link
        Then Redirect or appropriate error handling

    @emids_lp_045
    Scenario: verify_long_label_handling
        Given Legal link has maximum label length
        When Footer renders at mobile width
        Then Labels wrap appropriately without breaking layout

    @emids_lp_045
    Scenario: verify_locale_variant_handling
        Given Site has multiple locales
        When Legal links render for each locale
        Then Locale variants exist where required
