"""Feature: Provide All Solutions CTA (emids_lp_016)."""
Feature: Provide All Solutions CTA

    @emids_lp_016 @featured-solutions @cta
    Scenario: All Solutions CTA visible
        Given User views Featured Solutions section
        When User looks for additional action
        Then CTA is visible within or after the section

    @emids_lp_016 @featured-solutions @cta
    Scenario: CTA routes to solutions portfolio
        Given User clicks All Solutions CTA
        When Navigation completes
        Then Browser loads /solutions/ page

    @emids_lp_016 @featured-solutions @cta
    Scenario: CTA URL is canonical
        Given User examines All Solutions CTA
        When User checks destination
        Then URL resolves to canonical /solutions/ destination

    @emids_lp_016 @featured-solutions @cta
    Scenario: Portfolio page unavailable handling
        Given Solutions portfolio page is unavailable
        When User clicks All Solutions CTA
        Then User receives appropriate error or redirect
        And No broken page
