Feature: Provide All Solutions CTA

    @emids_lp_016
    Scenario: verify_cta_visible_after_section
        Given Featured Solutions section renders
        When User scrolls to end of section
        Then All Solutions CTA is visible after/within the section

    @emids_lp_016
    Scenario: verify_cta_routes_to_solutions_portfolio
        Given User clicks All Solutions CTA
        When Navigation completes
        Then User lands on solutions portfolio page at /solutions/

    @emids_lp_016
    Scenario: verify_cta_url_canonical
        Given All Solutions CTA URL is configured
        When Automated check validates URL
        Then URL is canonical and resolves successfully

    @emids_lp_016
    Scenario: verify_portfolio_page_unavailable_handling
        Given Solutions portfolio page is unavailable
        When User clicks All Solutions CTA
        Then User sees appropriate error or redirect rather than broken link
