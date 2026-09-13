"""Feature: Provide header Connect CTA (emids_lp_007)."""
Feature: Provide header Connect CTA

    @emids_lp_007 @connect-cta
    Scenario: Connect CTA visually distinct
        Given User views the header
        When User identifies the Connect action
        Then Connect CTA is visually prominent compared to other navigation items

    @emids_lp_007 @connect-cta
    Scenario: Connect CTA has accessible name
        Given User examines the Connect CTA
        When User checks accessibility attributes
        Then CTA has meaningful accessible name describing its action

    @emids_lp_007 @connect-cta
    Scenario: Connect routes to contact page
        Given User clicks Connect CTA
        When Navigation completes
        Then Browser loads /contact/ page

    @emids_lp_007 @connect-cta
    Scenario: Connect CTA URL is HTTPS and valid
        Given User examines Connect CTA
        When User checks link attributes
        Then URL is HTTPS and resolves to valid destination

    @emids_lp_007 @connect-cta
    Scenario: Connect keyboard activation
        Given User focuses on Connect CTA
        When User activates with keyboard (Enter/Space)
        Then Navigation to contact page occurs

    @emids_lp_007 @connect-cta @responsive
    Scenario: Responsive placement preserved
        Given User views site on mobile viewport
        When Page renders
        Then Connect CTA remains visible and accessible in header

    @emids_lp_007 @connect-cta
    Scenario: No duplicate CTA
        Given User examines header
        When User counts Connect CTAs
        Then Only one primary Connect CTA exists in header
