Feature: Integrate LinkedIn tags conditionally

    @emids_lp_041
    Scenario: verify_linkedin_consent_required
        Given LinkedIn tag is configured
        When Page loads
        Then LinkedIn tag does not execute before required marketing consent

    @emids_lp_041
    Scenario: verify_page_independent_of_linkedin
        Given LinkedIn tag fails to load
        When Page renders
        Then Core content and navigation remain independent of LinkedIn

    @emids_lp_041
    Scenario: verify_ad_blocker_handling
        Given Ad blocker prevents LinkedIn tag
        When Page renders
        Then Core functionality remains unaffected

    @emids_lp_041
    Scenario: verify_vendor_timeout_handling
        Given LinkedIn tag times out
        When Page renders
        Then Page continues normally; timeout handled gracefully

    @emids_lp_041
    Scenario: verify_consent_denied_handling
        Given User denies marketing consent
        When LinkedIn tag attempts to load
        Then Tag does not execute
