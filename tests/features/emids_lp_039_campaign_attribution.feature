Feature: Implement campaign attribution safely

    @emids_lp_039
    Scenario: verify_utm_params_preserved
        Given User arrives via URL with UTM parameters
        When Page loads
        Then Supported attribution values (utm_source, utm_medium, utm_campaign, utm_content, utm_term) are captured

    @emids_lp_039
    Scenario: verify_gclid_preserved
        Given User arrives via Google Ads with gclid
        When Page loads
        Then gclid parameter is captured if permitted

    @emids_lp_039
    Scenario: verify_referrer_captured
        Given User arrives from external site
        When Page loads
        Then Referrer is captured appropriately within consent rules

    @emids_lp_039
    Scenario: verify_invalid_values_ignored
        Given URL contains malformed or oversized UTM values
        When Page parses parameters
        Then Invalid/oversized values are ignored without breaking URLs

    @emids_lp_039
    Scenario: verify_length_limit_applied
        Given UTM parameter exceeds length limit
        When Parameter is processed
        Then Length limit is enforced; excess is truncated or ignored

    @emids_lp_039
    Scenario: verify_parameter_content_not_executed
        Given Malicious script in UTM parameter
        When Page processes parameters
        Then Parameter content is never executed as JavaScript

    @emids_lp_039
    Scenario: verify_no_full_urls_logged
        Given Attribution context is logged
        When Logging occurs
        Then Full URLs are not logged if they may contain sensitive query values

    @emids_lp_039
    Scenario: verify_consent_denied_handling
        Given User has not given marketing consent
        When Attribution values are captured
        Then Attribution collection respects consent limits

    @emids_lp_039
    Scenario: verify_malformed_query_handling
        Given URL has malformed query string
        When Page parses query
        Then Parsing handles malformed query without errors

    @emids_lp_039
    Scenario: verify_repeated_params_handling
        Given URL has repeated query parameters
        When Page parses query
        Then Repeated parameters are handled without breaking

    @emids_lp_039
    Scenario: verify_huge_values_handling
        Given Query parameter value is extremely large
        When Page parses value
        Then Value is sanitized or ignored without memory issues
