Feature: Expose Cookie Preferences control

    @emids_lp_036
    Scenario: verify_cookie_preferences_visible_in_footer
        Given Page renders footer
        When User scrolls to footer
        Then Cookie Preferences control is visible in footer

    @emids_lp_036
    Scenario: verify_control_opens_consent_ui
        Given User clicks Cookie Preferences
        When Control is activated
        Then Consent management UI opens allowing user to revise or withdraw consent

    @emids_lp_036
    Scenario: verify_control_available_after_banner_dismissal
        Given User has dismissed initial cookie banner
        When User returns to page or navigates
        Then Cookie Preferences control remains available in footer

    @emids_lp_036
    Scenario: verify_consent_script_blocked_handling
        Given Consent script is blocked
        When Page renders
        Then Cookie Preferences control gracefully handles unavailable consent UI

    @emids_lp_036
    Scenario: verify_storage_disabled_handling
        Given User has storage disabled
        When User interacts with consent UI
        Then System handles gracefully without causing errors

    @emids_lp_036
    Scenario: verify_user_clears_cookies_handling
        Given User clears cookies
        When User returns to page
        Then Cookie Preferences control remains functional to re-establish preferences
