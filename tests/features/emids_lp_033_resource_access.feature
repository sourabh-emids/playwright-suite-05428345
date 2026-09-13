Feature: Resource access without false file download

    @emids_lp_033
    Scenario: verify_download_reaches_detail_flow
        Given User clicks Download on eBook card
        When Navigation completes
        Then User reaches resource detail/access flow, not direct file download

    @emids_lp_033
    Scenario: verify_no_private_asset_endpoint_exposed
        Given eBook card Download action
        When User inspects network traffic
        Then Implementation does not expose private asset endpoint URLs

    @emids_lp_033
    Scenario: verify_gate_communication
        Given Resource is gated
        When User reaches resource detail page
        Then Gate clearly communicates required steps

    @emids_lp_033
    Scenario: verify_only_verified_destinations
        Given Resource URLs are configured
        When Automated check validates destinations
        Then Only verified/published destinations are used

    @emids_lp_033
    Scenario: verify_no_direct_file_url_assumption
        Given eBook asset URL handling
        When Implementation determines URL
        Then System does not assume direct public file URL; uses resource detail flow

    @emids_lp_033
    Scenario: verify_gated_asset_unavailable_handling
        Given Gated asset is unavailable
        When User attempts access
        Then Appropriate error message or fallback

    @emids_lp_033
    Scenario: verify_submission_failure_handling
        Given User submits form on resource detail page
        When Submission fails
        Then Clear error feedback; user can retry

    @emids_lp_033
    Scenario: verify_resource_withdrawn_handling
        Given Resource is withdrawn after publishing
        When User or system accesses resource
        Then Appropriate handling: 404, redirect, or message

    @emids_lp_033
    Scenario: verify_popup_blocked_handling
        Given Resource access uses popup
        When Popup is blocked
        Then Fallback to inline or new tab navigation
