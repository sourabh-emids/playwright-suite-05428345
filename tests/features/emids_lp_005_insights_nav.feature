Feature: Implement Insights navigation group

    @emids_lp_005
    Scenario: verify_insights_control_opens_reliably
        Given User focuses on Insights navigation item
        When User activates Insights control
        Then Menu opens reliably and displays thought leadership, resources, news, and related insight destinations

    @emids_lp_005
    Scenario: verify_insights_child_links_operable
        Given Insights menu is open
        When User views and interacts with child links
        Then All child links are readable and operable at all supported breakpoints

    @emids_lp_005
    Scenario: verify_no_empty_insights_groups
        Given Insights menu is rendered
        When Automated check validates menu groups
        Then No empty menu groups exist; all groups contain at least one item

    @emids_lp_005
    Scenario: verify_insights_destination_urls_canonical
        Given Insights menu displays destination URLs
        When Automated check validates URLs
        Then All destination URLs are canonical and resolve successfully
