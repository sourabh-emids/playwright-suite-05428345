Feature: Provide See the model CTA

    @emids_lp_013
    Scenario: verify_cta_routes_to_fdce_detail
        Given User clicks 'See the model' CTA
        When Navigation completes
        Then User lands on FDCE detail page at /forward-deployed-context-engineering/

    @emids_lp_013
    Scenario: verify_cta_keyboard_operable
        Given User focuses on 'See the model' CTA
        When User activates via keyboard (Enter/Space)
        Then CTA triggers navigation to FDCE detail page

    @emids_lp_013
    Scenario: verify_cta_accessible_name_describes_action
        Given CTA element exists
        When Screen reader reads the element
        Then Accessible name describes the action ('See the model')

    @emids_lp_013
    Scenario: verify_cta_destination_valid
        Given 'See the model' CTA URL is configured
        When Automated check tests destination
        Then URL returns 200 status; no 404 error

    @emids_lp_013
    Scenario: verify_no_duplicate_focus_target
        Given Multiple CTAs on page have focus behavior
        When User tabs through page
        Then Each CTA is a distinct focus target with appropriate behavior

    @emids_lp_013
    Scenario: verify_cta_visible_hover_focus_states
        Given User interacts with 'See the model' CTA
        When User hovers or focuses on CTA
        Then Visible hover and focus states are displayed
