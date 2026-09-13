Feature: Implement Industries mega-menu

    @emids_lp_004
    Scenario: verify_industries_menu_contains_five_audiences
        Given Industries menu is open
        When User views menu content
        Then Menu contains exactly five destinations: Payer, Provider, HealthTech, Life Sciences, and Consumer

    @emids_lp_004
    Scenario: verify_industry_links_keyboard_accessible
        Given Industries menu is open
        When User navigates via keyboard
        Then All five audience destinations are reachable without mouse

    @emids_lp_004
    Scenario: verify_industry_urls_canonical
        Given Industries menu displays URLs
        When Automated check validates URLs
        Then All five URLs use canonical format (/segments/payer/, /segments/provider/, etc.)

    @emids_lp_004
    Scenario: verify_desktop_grouped_industries_menu
        Given User is on desktop viewport
        When User opens Industries menu
        Then Menu displays as grouped desktop menu

    @emids_lp_004
    Scenario: verify_mobile_stacked_industries_list
        Given User is on mobile viewport
        When User opens Industries menu
        Then Menu displays as stacked list or disclosure pattern

    @emids_lp_004
    Scenario: verify_one_segment_unpublished_handling
        Given One industry segment is unpublished
        When Menu renders
        Then Only published segments appear in menu; no broken links

    @emids_lp_004
    Scenario: verify_long_translation_handling
        Given Menu labels have long translated text
        When Menu renders at mobile width
        Then Labels wrap appropriately without breaking layout
