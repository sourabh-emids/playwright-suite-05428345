Feature: Render six featured solution items

    @emids_lp_015
    Scenario: verify_six_entries_present
        Given Featured Solutions section renders
        When User views section content
        Then All six entries are present: Modernization as a Service, Interoperability, Cloud Migration, Global Capability Center, Epic Implementation, and Agentic AI

    @emids_lp_015
    Scenario: verify_numbering_01_to_06_correct
        Given Featured Solutions render
        When User views numbered items
        Then Numbering displays as 01, 02, 03, 04, 05, 06 in correct sequence

    @emids_lp_015
    Scenario: verify_each_entry_readable
        Given Six solutions render
        When User views each entry
        Then Each entry contains readable title, supporting copy, and intended destination/action

    @emids_lp_015
    Scenario: verify_titles_not_blank
        Given Six solutions render
        When Automated check validates titles
        Then No titles are blank or empty

    @emids_lp_015
    Scenario: verify_order_controlled
        Given Six solutions render
        When Automated check validates order
        Then Solutions appear in controlled order: 01-06 as defined

    @emids_lp_015
    Scenario: verify_exactly_six_items
        Given CMS content for featured solutions
        When Page renders
        Then Exactly six approved featured items are displayed for this content version

    @emids_lp_015
    Scenario: verify_one_item_unpublished_handling
        Given One of six solutions is unpublished
        When Page renders
        Then Only published items display; section maintains five items or validation prevents display

    @emids_lp_015
    Scenario: verify_no_duplicate_order
        Given Solutions render
        When Automated check validates order values
        Then No duplicate order numbers exist

    @emids_lp_015
    Scenario: verify_very_long_title_handling
        Given Solution title is at maximum character length
        When Page renders on mobile viewport
        Then Title wraps appropriately without breaking card layout

    @emids_lp_015
    Scenario: verify_card_media_missing_handling
        Given Solution card media fails to load
        When Card renders
        Then Card remains usable with text content; placeholder or fallback shown
