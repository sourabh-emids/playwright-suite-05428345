Feature: Display FinOps healthcare payer card

    @emids_lp_031
    Scenario: verify_finops_title_action_present
        Given FinOps healthcare payer card renders
        When User views card
        Then Card displays title, type, and action

    @emids_lp_031
    Scenario: verify_finops_routes_correctly
        Given User clicks FinOps card action
        When Navigation completes
        Then User reaches configured destination

    @emids_lp_031
    Scenario: verify_finops_valid_destination
        Given FinOps URL is configured
        When Automated check tests URL
        Then URL resolves successfully

    @emids_lp_031
    Scenario: verify_broken_link_handling
        Given FinOps link is broken
        When User clicks link
        Then Error handling or validation catches broken link

    @emids_lp_031
    Scenario: verify_missing_thumbnail_handling
        Given FinOps card thumbnail is missing
        When Card renders
        Then Card displays without image or with placeholder
