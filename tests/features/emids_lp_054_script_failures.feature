Feature: Handle script failures gracefully

    @emids_lp_054
    Scenario: verify_header_readable_with_failed_scripts
        Given Optional analytics scripts fail to load
        When Page renders
        Then Header remains readable and functional

    @emids_lp_054
    Scenario: verify_main_content_accessible_with_failed_scripts
        Given Optional scripts fail
        When Page renders
        Then Main content remains accessible

    @emids_lp_054
    Scenario: verify_ctas_functional_with_failed_scripts
        Given Optional scripts fail
        When Page renders
        Then CTAs remain functional and navigable

    @emids_lp_054
    Scenario: verify_footer_accessible_with_failed_scripts
        Given Optional scripts fail
        when Page renders
        Then Footer remains navigable

    @emids_lp_054
    Scenario: verify_errors_contained
        Given Optional integration fails
        When Error occurs
        Then Error is contained; does not break core UI

    @emids_lp_054
    Scenario: verify_fallback_content_available
        Given Media or integration fails
        When Page renders
        Then Fallback text/images provide core experience

    @emids_lp_054
    Scenario: verify_csp_block_handling
        Given CSP blocks script
        When Page loads
        Then Core content renders; blocked script handled gracefully

    @emids_lp_054
    Scenario: verify_dns_failure_handling
        Given DNS resolution fails for third-party
        When Page loads
        Then Core content renders; DNS failure handled gracefully

    @emids_lp_054
    Scenario: verify_ad_blocker_handling
        Given Ad blocker blocks third-party script
        When Page loads
        Then Core functionality unaffected

    @emids_lp_054
    Scenario: verify_timeout_handling
        Given Third-party script times out
        When Page loads
        Then Core content renders without waiting for timeout

    @emids_lp_054
    Scenario: verify_malformed_vendor_script_handling
        Given Vendor script is malformed
        When Browser parses script
        Then Core UI remains functional; error contained

    @emids_lp_054
    Scenario: verify_no_stack_traces_user_content
        Given Error occurs in optional script
        When Logging happens
        Then No stack traces containing user content are logged
