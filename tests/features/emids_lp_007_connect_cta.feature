Feature: Provide header Connect CTA

    @emids_lp_007
    Scenario: verify_connect_cta_visually_distinct
        Given Header is rendered on page
        When User visually inspects the Connect CTA
        Then Connect CTA is visually distinct from other navigation elements

    @emids_lp_007
    Scenario: verify_connect_cta_accessible_name
        Given Connect CTA element exists
        When Screen reader reads the element
        Then CTA has an accessible name that describes its action

    @emids_lp_007
    Scenario: verify_connect_cta_routes_to_contact
        Given User clicks the Connect CTA
        When Navigation completes
        Then User lands on the contact page with valid HTTPS URL

    @emids_lp_007
    Scenario: verify_connect_cta_keyboard_activation
        Given User focuses on Connect CTA using keyboard
        When User activates CTA (Enter/Space)
        Then CTA triggers navigation to contact page

    @emids_lp_007
    Scenario: verify_connect_cta_responsive_placement
        Given User views page at various viewport sizes
        When Header reflows responsively
        Then Connect CTA placement is preserved and visible across all breakpoints

    @emids_lp_007
    Scenario: verify_cta_url_valid_https
        Given Connect CTA URL is defined
        When Automated check validates URL
        Then URL uses HTTPS protocol and is canonical

    @emids_lp_007
    Scenario: verify_no_duplicated_cta
        Given Header renders multiple CTAs
        When Automated check scans for Connect elements
        Then No duplicate Connect CTA exists in header

    @emids_lp_007
    Scenario: verify_cta_text_wrapping_handling
        Given Connect CTA has maximum label length
        When Header renders on narrow viewport
        Then Text wraps appropriately without breaking layout
