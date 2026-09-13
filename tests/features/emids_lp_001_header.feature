Feature: Render global header and brand entry point

    @emids_lp_001
    Scenario: Verify_header_visible_on_initial_load
        Given User opens the Emids homepage
        When Page finishes loading
        Then Global header is visible and displays the Emids logo, navigation items (Solutions, Capabilities, Industries, Insights, Company), and Connect CTA

    @emids_lp_001
    Scenario: Verify_logo_returns_to_homepage
        Given User is on any page of the website
        When User clicks the Emids logo
        Then User is navigated to the homepage at URL '/'

    @emids_lp_001
    Scenario: Verify_all_navigation_reachable_by_keyboard
        Given User focuses on the header area using keyboard only
        When User tabs through navigation items
        Then All top-level navigation items (Solutions, Capabilities, Industries, Insights, Company) receive visible focus and are selectable

    @emids_lp_001
    Scenario: Verify_connect_cta_routes_to_contact
        Given User is on the homepage with header visible
        When User clicks the Connect CTA button
        Then User is navigated to the contact experience page

    @emids_lp_001
    Scenario: Verify_desktop_grouped_navigation
        Given User views the page on a desktop viewport (1024px or wider)
        When Header is rendered
        Then Navigation items are presented in grouped format with Connect as a prominent action button

    @emids_lp_001
    Scenario: Verify_no_dead_links_in_header
        Given All navigation items and CTAs are rendered in the header
        When Automated check tests each navigation destination
        Then All URLs return successful responses (200-299) with no dead links

    @emids_lp_001
    Scenario: Verify_only_one_primary_connect_cta
        Given Header is fully rendered
        When Automated check counts Connect CTA elements
        Then Only one primary Connect CTA exists in the header

    @emids_lp_001
    Scenario: Verify_responsive_preserves_navigation_access
        Given User views the page on a narrow mobile viewport (320px)
        When Navigation collapses into mobile menu
        Then All navigation destinations remain accessible without losing access to any item

    @emids_lp_001
    Scenario: Verify_long_menu_label_handling
        Given Navigation contains labels at maximum character length
        When Header is rendered on various viewport sizes
        Then Long labels do not break layout and text wraps appropriately

    @emids_lp_001
    Scenario: Verify_header_with_javascript_disabled
        Given JavaScript is disabled in the browser
        When User loads the homepage
        Then Header with static navigation links remains visible and functional
