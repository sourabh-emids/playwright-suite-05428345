"""Feature: Render five audience industry entries (emids_lp_024)."""
Feature: Render five audience industry entries

    @emids_lp_024 @who-we-serve
    Scenario: All five audiences visible
        Given User views Who We Serve section
        When User counts audience entries
        Then Payer, Provider, HealthTech, Life Sciences, and Consumer audiences all display

    @emids_lp_024 @who-we-serve
    Scenario: Each Explore action routes to canonical segment
        Given User clicks Explore on each audience card
        When Navigation completes
        Then Payer navigates to /segments/payer/
        And Provider to /segments/provider/
        And HealthTech to /segments/healthtech/
        And Life Sciences to /segments/life-sciences/
        And Consumer to /segments/consumer/

    @emids_lp_024 @who-we-serve @accessibility
    Scenario: Explore actions keyboard and touch operable
        Given User navigates via keyboard or touch
        When User activates Explore action
        Then Navigation works
        And Content accessible without mouse

    @emids_lp_024 @who-we-serve
    Scenario: Exactly five current audiences
        Given User views Who We Serve section
        When User counts audience items
        Then Exactly five audiences display for this content version

    @emids_lp_024 @who-we-serve
    Scenario: URLs canonical
        Given User examines audience destinations
        When User checks URLs
        Then All URLs use canonical segment paths

    @emids_lp_024 @who-we-serve
    Scenario: One segment unavailable handling
        Given One segment page is unavailable
        When Page renders Who We Serve section
        Then Available segments display
        And Unavailable segment handled gracefully

    @emids_lp_024 @who-we-serve @responsive
    Scenario: Tab state preserved after resize
        Given User selects an audience tab
        When User resizes browser window
        Then Tab selection or content state adapts appropriately
        And No permanent loss of state
