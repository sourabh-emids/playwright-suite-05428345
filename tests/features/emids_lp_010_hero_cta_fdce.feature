Feature: Route hero CTA to FDCE experience

    @emids_lp_010
    Scenario: verify_hero_cta_resolves_to_fdce
        Given User clicks hero CTA
        When Navigation completes
        Then User lands on Forward-Deployed Context Engineering canonical page

    @emids_lp_010
    Scenario: verify_hero_cta_url_https_canonical
        Given Hero CTA URL is configured
        When Automated check validates URL
        Then URL uses HTTPS protocol and is canonical (/forward-deployed-context-engineering/)

    @emids_lp_010
    Scenario: verify_browser_navigation_behavior
        Given User clicks hero CTA
        When Navigation occurs
        Then Expected browser navigation behavior is preserved (history entry created, referrer set)

    @emids_lp_010
    Scenario: verify_new_tab_opening
        Given User right-clicks hero CTA and selects 'Open in new tab'
        When Navigation completes
        Then FDCE page opens in new tab successfully

    @emids_lp_010
    Scenario: verify_destination_unavailable_handling
        Given FDCE page returns error
        When User clicks hero CTA
        Then User sees appropriate error page (404/500) rather than broken experience
