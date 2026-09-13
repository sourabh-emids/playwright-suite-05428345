Feature: Load GTM with consent governance

    @emids_lp_037
    Scenario: verify_page_works_if_gtm_fails
        Given Google Tag Manager fails to load
        When Page renders
        Then Core page remains functional without GTM

    @emids_lp_037
    Scenario: verify_non_essential_tags_consent_gated
        Given Non-essential analytics tags are configured
        When Required consent is not given
        Then Non-essential tags do not run before required consent

    @emids_lp_037
    Scenario: verify_gtm_does_not_block_rendering
        Given GTM script loads
        When Page renders
        Then GTM does not block critical rendering path

    @emids_lp_037
    Scenario: verify_consent_mode_respected
        Given GTM container is configured
        When Tags fire based on consent state
        Then Consent mode/configuration is obeyed by tag triggers

    @emids_lp_037
    Scenario: verify_ad_blocker_handling
        Given Ad blocker prevents GTM
        When Page renders
        Then Core functionality remains; GTM failure is contained

    @emids_lp_037
    Scenario: verify_csp_block_handling
        Given Content Security Policy blocks GTM
        When Page renders
        Then Core functionality remains; error is handled

    @emids_lp_037
    Scenario: verify_gtm_timeout_handling
        Given GTM script times out
        When Page renders
        Then Core content loads without waiting for GTM

    @emids_lp_037
    Scenario: verify_consent_denied_handling
        Given User has denied consent
        When Page renders with GTM
        Then Non-essential tags do not fire; page functions normally
