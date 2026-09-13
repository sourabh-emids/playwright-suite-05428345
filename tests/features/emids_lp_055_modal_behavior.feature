Feature: Homepage modal behavior none by default

    @emids_lp_055
    Scenario: verify_base_homepage_no_unsolicited_modal
        Given Homepage renders in base configuration
        When Page loads
        Then No unsolicited promotional modal appears

    @emids_lp_055
    Scenario: verify_consent_ui_not_marketing_modal
        Given Consent UI opens
        When User interacts with cookie preferences
        Then Consent UI is separate from promotional modal behavior

    @emids_lp_055
    Scenario: verify_resource_gate_not_base_modal
        Given User accesses gated resource
        When Gate displays
        Then Resource gate is separate from base homepage modal

    @emids_lp_055
    Scenario: verify_configured_modal_separately_governed
        Given Campaign modal is configured
        When Modal activates
        Then Modal is governed by separate configuration (dismissible, keyboard accessible, non-blocking)

    @emids_lp_055
    Scenario: verify_default_state_disabled
        Given Campaign modal configuration
        When Page renders in default state
        Then Campaign modal is disabled by default

    @emids_lp_055
    Scenario: verify_configured_modal_has_title
        Given Campaign modal is configured
        When Modal renders
        Then Modal has title defined

    @emids_lp_055
    Scenario: verify_configured_modal_has_content
        Given Campaign modal is configured
        When Modal renders
        Then Modal has content defined

    @emids_lp_055
    Scenario: verify_configured_modal_dismissible
        Given Campaign modal displays
        When User interacts with dismiss control
        Then Modal is dismissible

    @emids_lp_055
    Scenario: verify_configured_modal_keyboard_accessible
        Given Campaign modal displays
        When User interacts via keyboard
        Then Modal is keyboard accessible

    @emids_lp_055
    Scenario: verify_repeated_modal_after_dismissal
        Given Modal was dismissed
        When User continues browsing
        Then Modal does not repeatedly reappear inappropriately

    @emids_lp_055
    Scenario: verify_focus_trap_in_modal
        Given Campaign modal opens
        When User tabs through content
        Then Focus is trapped within modal; Escape closes

    @emids_lp_055
    Scenario: verify_small_viewport_modal
        Given Campaign modal configured
        When Modal renders on small viewport
        Then Modal adapts appropriately without breaking

    @emids_lp_055
    Scenario: verify_js_disabled_modal_handling
        Given JavaScript disabled
        When Page loads
        Then No modal displays; base experience works

    @emids_lp_055
    Scenario: verify_campaign_display_consent_check
        Given Campaign modal configured
        When Analytics consent not given
        Then Display/dismiss events not logged inappropriately
