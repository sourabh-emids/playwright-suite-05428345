"""Feature: Implement Insights navigation group (emids_lp_005)."""
Feature: Implement Insights navigation group

    @emids_lp_005 @insights-nav
    Scenario: Insights menu opens reliably
        Given User focuses on Insights navigation
        When User activates Insights menu trigger
        Then Menu opens consistently
        And Child links are visible and readable

    @emids_lp_005 @insights-nav @responsive
    Scenario: Insights links operable at all breakpoints
        Given Insights menu is open on various viewport sizes
        When User activates menu and clicks links
        Then Links remain operable
        And Content is readable
        And No truncation of essential text

    @emids_lp_005 @insights-nav
    Scenario: No empty menu groups
        Given User opens Insights menu
        When User examines menu structure
        Then All groups contain at least one item
        And No empty containers displayed

    @emids_lp_005 @insights-nav
    Scenario: Destination URLs canonical
        Given Insights menu is open
        When User clicks insight destinations
        Then All links resolve to canonical URLs under /insights/ and related paths
