"""Feature: Route hero CTA to FDCE experience (emids_lp_010)."""
Feature: Route hero CTA to FDCE experience

    @emids_lp_010 @hero @cta
    Scenario: Hero CTA resolves to FDCE page
        Given User is on homepage hero section
        When User clicks the primary hero CTA
        Then Browser navigates to /forward-deployed-context-engineering/

    @emids_lp_010 @hero @cta
    Scenario: FDCE URL is HTTPS and canonical
        Given User examines hero CTA destination
        When User checks URL attributes
        Then URL uses HTTPS protocol
        And URL is canonical

    @emids_lp_010 @hero @cta
    Scenario: Browser navigation behavior preserved
        Given User clicks hero CTA
        When Navigation occurs
        Then Standard browser navigation behavior occurs
        And No unexpected popups or behaviors

    @emids_lp_010 @hero @cta
    Scenario: New tab navigation works
        Given User right-clicks hero CTA to open in new tab
        When User selects open in new tab
        Then FDCE page opens in new tab correctly

    @emids_lp_010 @hero @cta
    Scenario: Destination unavailable handling
        Given FDCE destination page is temporarily unavailable
        When User clicks hero CTA
        Then User receives appropriate error page
        And Core site remains functional
