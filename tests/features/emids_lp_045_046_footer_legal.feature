"""Feature: Render footer legal navigation and corporate info (emids_lp_045-046)."""
Feature: Render footer legal navigation and corporate info

    @emids_lp_045 @footer
    Scenario: Legal links have descriptive text and valid destinations
        Given User views footer legal links
        When User checks each link
        Then Privacy Policy, Cookie Policy, Accessibility Statement, and other approved links have descriptive text
        And URLs are HTTPS and valid

    @emids_lp_045 @footer @accessibility
    Scenario: Legal links have visible focus state
        Given User navigates to legal links with keyboard
        When Focus is on legal link
        Then Visible focus indicator displays

    @emids_lp_045 @footer
    Scenario: Labels may not be blank
        Given CMS configures legal links
        When Link saves without label
        Then Validation prevents empty labels

    @emids_lp_045 @footer
    Scenario: Legal page moved handling
        Given Legal page URL changes
        When User clicks legal link
        Then Redirect or updated link
        And No 404 broken pages

    @emids_lp_045 @footer @responsive
    Scenario: Long labels handling
        Given Legal link has long label
        When Page renders on mobile
        Then Label wraps or truncates appropriately
        And No overflow

    @emids_lp_046 @footer
    Scenario: Footer information readable at mobile widths
        Given User views footer on mobile viewport
        When Page renders
        Then Corporate text and details are readable
        And No overflow or truncation

    @emids_lp_046 @footer
    Scenario: Social links functional
        Given User clicks social links in footer
        When Navigation completes
        Then Social destinations load correctly
