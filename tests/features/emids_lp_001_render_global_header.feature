"""Feature: Render global header and Emids brand (emids_lp_001)."""
Feature: Render global header and Emids brand

    @emids_lp_001 @header
    Scenario: Header visible on initial page load
        Given User navigates to the emids homepage
        When Page load completes
        Then Header is visible at the top of the viewport
        And Emids logo/brand link is present
        And Primary navigation items (Solutions, Capabilities, Industries, Insights, Company) are visible
        And Connect CTA is prominently displayed

    @emids_lp_001 @header
    Scenario: Emids logo navigates to homepage
        Given User is on any page within the site
        When User clicks the Emids logo or brand link in the header
        Then Browser navigates to the homepage (/)

    @emids_lp_001 @header
    Scenario: All navigation items keyboard accessible
        Given User navigates to the emids homepage with keyboard only
        When User tabs through header navigation items
        Then Each navigation item (Solutions, Capabilities, Industries, Insights, Company) receives visible focus indicator
        And All items are reachable without mouse
        And Connect CTA is keyboard operable

    @emids_lp_001 @header
    Scenario: Connect CTA routes to contact page
        Given User is on the homepage
        When User clicks or activates the Connect CTA in the header
        Then Browser navigates to /contact/ page

    @emids_lp_001 @header
    Scenario: No dead links in header navigation
        Given User is on the emids homepage
        When User clicks each navigation item and Connect CTA
        Then All navigation links resolve to valid destinations
        And No 404 or error pages are returned

    @emids_lp_001 @header
    Scenario: Only one primary Connect CTA
        Given User views the header
        When User examines the header for Connect actions
        Then Exactly one primary Connect CTA is visible and distinguished from other navigation

    @emids_lp_001 @header @responsive
    Scenario: Header responsive on narrow viewport
        Given User views the site on a narrow viewport (320px)
        When Page renders
        Then Navigation does not cause horizontal scrolling
        And All destinations remain accessible via menu toggle or equivalent

    @emids_lp_001 @header
    Scenario: Header functions with JS disabled
        Given User has JavaScript disabled in browser
        When User navigates to the homepage
        Then Header renders with visible content
        And Brand link and basic navigation remain functional
