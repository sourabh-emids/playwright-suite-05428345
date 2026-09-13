Feature: Integrate Marketo with consent

    @emids_lp_040
    Scenario: verify_marketing_scripts_consent_gated
        Given Marketo is configured
        When Marketing consent is not given
        Then Marketing scripts do not execute

    @emids_lp_040
    Scenario: verify_page_functional_when_marketo_unavailable
        Given Marketo fails to load
        When Page renders
        Then Page remains functional without Marketo

    @emids_lp_040
    Scenario: verify_marketing_consent_required
        Given Marketo integration is configured
        When Analytics initializes
        Then Marketing consent is required for Marketo execution

    @emids_lp_040
    Scenario: verify_script_blocked_handling
        Given Marketo script is blocked by browser
        When Page renders
        Then Core functionality unaffected; error handled gracefully

    @emids_lp_040
    Scenario: verify_vendor_outage_handling
        Given Marketo vendor is experiencing outage
        When Page renders or form submits
        Then User experience continues; error logged appropriately

    @emids_lp_040
    Scenario: verify_consent_revoked_handling
        Given User revokes marketing consent
        When Marketo attempts to track
        Then Marketo stops executing; no further tracking

    @emids_lp_040
    Scenario: verify_no_raw_lead_data_logged
        Given Marketo integration events occur
        When Logging happens
        Then Only integration status/error codes logged, not raw lead data
