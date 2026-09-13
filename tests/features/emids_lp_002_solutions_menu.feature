Feature: Implement Solutions mega-menu

    @emids_lp_002
    Scenario: Verify_solutions_menu_opens_accessibly
        Given User hovers over or focuses on the Solutions navigation item
        When User activates the Solutions control
        Then An accessible mega-menu opens displaying solution taxonomy grouped appropriately

    @emids_lp_002
    Scenario: Verify_all_solution_links_selectable
        Given Solutions mega-menu is open
        When User clicks each visible solution link
        Then Each link navigates to its valid destination URL

    @emids_lp_002
    Scenario: Verify_menu_focus_order_maintained
        Given Solutions menu is open and user begins tabbing
        When User navigates through menu items using keyboard
        Then Focus remains within expected navigation order without escaping unexpectedly

    @emids_lp_002
    Scenario: Verify_menu_close_restores_focus
        Given Solutions menu is open with focus on a menu item
        When User closes the menu (Escape key or clicking outside)
        Then Focus returns to the Solutions trigger control

    @emids_lp_002
    Scenario: Verify_solution_labels_non_empty
        Given Solutions menu is rendered
        When Automated check validates each solution item
        Then Every item has a non-empty label and valid URL (internal or approved external)

    @emids_lp_002
    Scenario: Verify_mobile_equivalent_disclosure
        Given User views page on mobile device
        When User activates Solutions navigation
        Then An accessible disclosure or drawer pattern is presented instead of mega-menu

    @emids_lp_002
    Scenario: Verify_menu_not_clipped_by_viewport
        Given Solutions menu is open near edge of browser window
        When Menu positions itself responsively
        Then Menu is not clipped and remains fully visible within viewport

    @emids_lp_002
    Scenario: Verify_touch_device_menu_accessibility
        Given User is on a touch device without hover capability
        When User taps Solutions navigation
        Then Menu opens on tap and is fully usable without hover interactions
