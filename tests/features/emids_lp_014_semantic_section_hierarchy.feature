"""Feature: Maintain semantic section hierarchy (emids_lp_014)."""
Feature: Maintain semantic section hierarchy

    @emids_lp_014 @semantics @accessibility
    Scenario: Exactly one page-level H1
        Given User examines page structure
        When User counts H1 elements
        Then Exactly one H1 exists on the page

    @emids_lp_014 @semantics @accessibility
    Scenario: Subsequent headings use logical levels
        Given User examines page heading hierarchy
        When User traces heading levels
        Then Section headings follow logical order
        And No skipped levels (H1 to H3 without H2)

    @emids_lp_014 @semantics @accessibility
    Scenario: Landmarks identifiable
        Given User views page landmarks
        When User or assistive technology examines landmarks
        Then main, header, footer, and section landmarks are properly identified

    @emids_lp_014 @semantics
    Scenario: Interactive text not headings solely for styling
        Given User examines clickable text
        When User checks heading elements
        Then No interactive elements use heading styling as sole purpose
        And Headings contain meaningful text

    @emids_lp_014 @semantics
    Scenario: Duplicate H1 from CMS handling
        Given CMS editor introduces duplicate H1
        When Page renders
        Then QA validation detects duplicate H1
        And Page does not ship with multiple H1s

    @emids_lp_014 @semantics @accessibility
    Scenario: Hidden heading focusable
        Given Hidden content with heading is revealed
        When User expands hidden section
        Then Hidden heading becomes visible/focusable
        And Heading hierarchy remains correct
