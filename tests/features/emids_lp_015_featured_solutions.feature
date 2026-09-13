"""Feature: Render six featured solution items (emids_lp_015)."""
Feature: Render six featured solution items

    @emids_lp_015 @featured-solutions
    Scenario: All six solutions present with correct numbering
        Given User views Featured Solutions section
        When User enumerates solutions
        Then All six entries present: Modernization as a Service (01), Interoperability (02), Cloud Migration (03), Global Capability Center (04), Epic Implementation (05), Agentic AI (06)

    @emids_lp_015 @featured-solutions
    Scenario: Numbering 01-06 correct
        Given User views Featured Solutions cards
        When User checks numbering
        Then Numbers display as 01 through 06 in correct sequential order

    @emids_lp_015 @featured-solutions
    Scenario: Each entry has readable title and summary
        Given User examines each solution card
        When User reads content
        Then Each card contains readable title and supporting copy

    @emids_lp_015 @featured-solutions
    Scenario: Each entry has intended destination
        Given User views solution card
        When User checks card interaction
        Then Each card links to its intended solution page

    @emids_lp_015 @featured-solutions
    Scenario: Titles cannot be blank
        Given CMS manages solution content
        When Content is published
        Then No solution card displays with blank title field

    @emids_lp_015 @featured-solutions
    Scenario: Order is controlled
        Given User views Featured Solutions
        When User checks sequence
        Then Solutions display in CMS-defined order
        And No random or reverse order

    @emids_lp_015 @featured-solutions
    Scenario: One item unpublished handling
        Given One solution is unpublished
        When Featured Solutions section renders
        Then Only published solutions display
        And Section maintains 6 items when fully published

    @emids_lp_015 @featured-solutions @responsive
    Scenario: Very long title handling
        Given Solution has very long title
        When Page renders on mobile
        Then Title truncates or wraps gracefully
        And Does not break card layout
