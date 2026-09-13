"""Feature: Implement Industries mega-menu (emids_lp_004)."""
Feature: Implement Industries mega-menu

    @emids_lp_004 @industries-menu
    Scenario: All five industry destinations present
        Given Industries menu is open
        When User examines available destinations
        Then Payer, Provider, HealthTech, Life Sciences, and Consumer destinations are all present with correct labels

    @emids_lp_004 @industries-menu
    Scenario: Industry links reachable without mouse
        Given Industries menu is open
        When User navigates via keyboard
        Then All five industry links are keyboard accessible and navigable

    @emids_lp_004 @industries-menu
    Scenario: Industry links use canonical URLs
        Given Industries menu is open
        When User clicks each industry destination
        Then Links resolve to canonical URLs
        And Payer navigates to /segments/payer/
        And Provider navigates to /segments/provider/
        And HealthTech navigates to /segments/healthtech/
        And Life Sciences navigates to /segments/life-sciences/
        And Consumer navigates to /segments/consumer/

    @emids_lp_004 @industries-menu @mobile
    Scenario: Mobile stacked list pattern
        Given User is on mobile viewport
        When User opens Industries menu
        Then Destinations display as stacked list or disclosure
        And All five remain accessible

    @emids_lp_004 @industries-menu
    Scenario: One segment unavailable handling
        Given One industry segment page is unpublished
        When User opens Industries menu
        Then Menu does not include broken or unpublished links
        And Valid links remain functional
