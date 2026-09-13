Feature: Integrate ZoomInfo WebSights conditionally

    @emids_lp_042
    Scenario: verify_tooling_loads_conditionally
        Given ZoomInfo/WebSights is configured and enabled
        When Page loads
        Then Tooling loads only when enabled and permitted by consent

    @emids_lp_042
    Scenario: verify_failure_does_not_affect_content
        Given ZoomInfo/WebSights fails
        When Page renders
        Then Content and navigation remain unaffected

    @emids_lp_042
    Scenario: verify_no_private_identifiers_exposed
        Given Visitor intelligence config exists
        When Page renders
        Then Private account identifiers are not exposed in page copy

    @emids_lp_042
    Scenario: verify_vendor_blocked_handling
        Given ZoomInfo/WebSights is blocked
        When Page renders
        Then Page continues normally

    @emids_lp_042
    Scenario: verify_network_error_handling
        Given ZoomInfo/WebSights network request fails
        When Page renders
        Then Core functionality unaffected

    @emids_lp_042
    Scenario: verify_consent_denied_handling
        Given User denies required consent
        When ZoomInfo/WebSights attempts to load
        Then Tooling does not load or execute
