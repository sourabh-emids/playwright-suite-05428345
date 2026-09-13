Feature: Support Google Analytics after consent

    @emids_lp_038
    Scenario: verify_analytics_consent_governed
        Given Google Analytics is configured
        When Page loads
        Then Analytics initializes only after consent is given

    @emids_lp_038
    Scenario: verify_page_works_if_consent_denied
        Given User denies statistics consent
        When Page renders
        Then Page remains fully functional without analytics

    @emids_lp_038
    Scenario: verify_events_no_contact_form_data
        Given Analytics events are tracked
        When Events are sent
        Then Events do not contain contact form field values

    @emids_lp_038
    Scenario: verify_page_view_tracking
        Given User navigates to page
        When Page view occurs
        Then Page view event is tracked if consent allows

    @emids_lp_038
    Scenario: verify_cta_event_tracking
        Given User clicks CTA
        When CTA event fires
        Then Event is tracked with consent

    @emids_lp_038
    Scenario: verify_content_interaction_tracking
        Given User interacts with content
        When Interaction event triggers
        Then Event tracked if consent allows

    @emids_lp_038
    Scenario: verify_statistics_consent_required
        Given Google Analytics is configured
        When Statistics consent is not given
        Then Statistics collection does not occur

    @emids_lp_038
    Scenario: verify_no_sensitive_data_in_events
        Given Analytics events are constructed
        When Automated check validates event data
        Then No sensitive/lead data in event payloads

    @emids_lp_038
    Scenario: verify_offline_handling
        Given User is offline
        When Analytics event attempts to fire
        Then No errors thrown; event queued or dropped gracefully

    @emids_lp_038
    Scenario: verify_consent_revoked_handling
        Given User revokes consent mid-session
        When Analytics attempts to track
        Then Tracking stops; no further events sent

    @emids_lp_038
    Scenario: verify_no_duplicate_pageview
        Given Single page load occurs
        When Page view event fires
        Then Only one page view event is recorded (no duplicates)
