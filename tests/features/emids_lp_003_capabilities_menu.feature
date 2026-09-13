Feature: Implement Capabilities mega-menu

    @emids_lp_003
    Scenario: Verify_capabilities_menu_predictable_open_close
        Given User focuses on the Capabilities navigation item
        When User activates the Capabilities control
        Then Menu opens predictably with AI, Engineering, and Platforms capability groups

    @emids_lp_003
    Scenario: verify_all_capability_links_keyboard_operable
        Given Capabilities menu is open
        When User tabs through capability links
        Then All capability links are keyboard operable with visible focus states

    @emids_lp_003
    Scenario: verify_capability_labels_match_taxonomy
        Given Capabilities menu displays labels
        When Automated check validates against approved taxonomy
        Then Labels match the content-managed approved taxonomy (AI, Engineering, Platforms)

    @emids_lp_003
    Scenario: verify_capability_labels_unique
        Given Capabilities menu is rendered
        When Automated check scans all labels
        Then No duplicate labels exist within the menu

    @emids_lp_003
    Scenario: verify_capability_urls_resolve
        Given Capabilities menu displays URLs
        When Each capability URL is tested
        Then All URLs return successful responses

    @emids_lp_003
    Scenario: verify_mobile_capability_disclosure
        Given User is on mobile viewport
        When User activates Capabilities
        Then Accessible disclosure pattern is presented

    @emids_lp_003
    Scenario: verify_menu_overflow_handling
        Given Capabilities menu contains many items
        When Menu is open on various viewport sizes
        Then Menu handles overflow gracefully without breaking layout
