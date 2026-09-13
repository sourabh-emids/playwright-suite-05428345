"""Feature: Provide See the model CTA (emids_lp_013)."""
Feature: Provide See the model CTA

    @emids_lp_013 @how-we-deliver @cta
    Scenario: See the model routes to FDCE detail page
        Given User views How We Deliver section
        When User clicks See the model CTA
        Then Browser navigates to /forward-deployed-context-engineering/

    @emids_lp_013 @how-we-deliver @cta @accessibility
    Scenario: CTA keyboard operable
        Given User focuses on See the model CTA
        When User activates with keyboard
        Then Navigation to FDCE page occurs

    @emids_lp_013 @how-we-deliver @cta @accessibility
    Scenario: Accessible name describes action
        Given User examines See the model CTA
        When User checks accessible name
        Then Label clearly describes the action destination

    @emids_lp_013 @how-we-deliver @cta
    Scenario: Destination valid
        Given User clicks See the model CTA
        When Navigation attempts
        Then FDCE destination URL is valid
        And No 404 returned

    @emids_lp_013 @how-we-deliver @cta
    Scenario: Visible hover/focus states
        Given User hovers or focuses on See the model CTA
        When User observes visual feedback
        Then Visible hover and focus states indicate interactivity

    @emids_lp_013 @how-we-deliver @cta
    Scenario: Duplicate focus target handling
        Given Multiple CTAs on page
        When User navigates via focus
        Then No duplicate focus targets
        And Keyboard navigation remains logical
