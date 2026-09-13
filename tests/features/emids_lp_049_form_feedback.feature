Feature: Contact form submission feedback retry

    @emids_lp_049
    Scenario: verify_submit_pending_state
        Given User clicks Submit
        When Form submission begins
        Then Submit button enters pending/loading state

    @emids_lp_049
    Scenario: verify_duplicate_activation_prevented
        Given Submission is pending
        When User attempts second submission
        Then Duplicate activation is prevented

    @emids_lp_049
    Scenario: verify_success_announced
        Given Form submits successfully
        When Response received
        Then Success is announced via accessible live region or message

    @emids_lp_049
    Scenario: verify_failure_keeps_content
        Given Form submission fails
        When Error occurs
        Then User-entered content is preserved for retry

    @emids_lp_049
    Scenario: verify_retry_permitted
        Given Form submission failed
        When User retries
        Then User can submit again with same or corrected content

    @emids_lp_049
    Scenario: verify_fields_cleared_on_success
        Given Form submission succeeds
        When Success response received
        Then Fields are cleared after successful submission

    @emids_lp_049
    Scenario: verify_server_validation_errors_map_to_fields
        Given Server returns validation errors
        When Error message displays
        Then Errors are mapped to fields where possible

    @emids_lp_049
    Scenario: verify_timeout_retry
        Given Form submission times out
        When Timeout occurs
        Then User can retry; content preserved

    @emids_lp_049
    Scenario: verify_4xx_validation_handling
        Given Server returns 4xx validation error
        When Error response received
        Then Field-level errors shown; content preserved

    @emids_lp_049
    Scenario: verify_5xx_outage_handling
        Given Server returns 5xx error (vendor/CRM outage)
        When Error response received
        Then Generic error shown; user can retry later

    @emids_lp_049
    Scenario: verify_user_navigates_away_handling
        Given User navigates away during submission
        When Navigation occurs
        Then Warning shown if submission in progress; state handled gracefully
