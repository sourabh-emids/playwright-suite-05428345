Feature: Display CMS-0057 interoperability card

    @emids_lp_028
    Scenario: verify_cms0057_title_populated
        Given CMS-0057 interoperability card renders
        When User views card
        Then Card title is populated from approved content

    @emids_lp_028
    Scenario: verify_cms0057_type_populated
        Given CMS-0057 card renders
        When Automated check validates type
        Then Card type is populated correctly

    @emids_lp_028
    Scenario: verify_cms0057_action_navigates_correctly
        Given User clicks CMS-0057 card action
        When Navigation completes
        Then User reaches intended resource destination

    @emids_lp_028
    Scenario: verify_no_empty_title_or_destination
        Given CMS-0057 card data
        When Automated check validates fields
        Then No empty title or destination; both required

    @emids_lp_028
    Scenario: verify_destination_changed_handling
        Given CMS-0057 destination URL changes
        When Page renders with new URL
        Then Card updates to new destination or validation catches mismatch
