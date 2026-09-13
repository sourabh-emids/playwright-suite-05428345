Feature: Implement Company navigation group

    @emids_lp_006
    Scenario: verify_company_menu_exposes_approved_links
        Given Company menu is open
        When User views menu content
        Then Menu displays only approved company information and contact-related destinations

    @emids_lp_006
    Scenario: verify_company_menu_keyboard_pointer_touch
        Given Company menu is open
        When User interacts via keyboard, pointer, or touch
        Then Menu works with all three interaction methods

    @emids_lp_006
    Scenario: verify_unpublished_page_not_displayed
        Given A company page is unpublished in CMS
        When Company menu renders
        Then Unpublished pages do not appear in menu

    @emids_lp_006
    Scenario: verify_no_redirect_loop_in_company_links
        Given Company menu URLs are validated
        When Automated check follows redirects
        Then No infinite redirect loops exist
