"""Feature: Render AI capability content (emids_lp_021)."""
Feature: Render AI capability content

    @emids_lp_021 @capabilities @ai
    Scenario: AI capability label and content render
        Given User views AI capability card/panel
        When Content loads
        Then AI label displays
        And Supporting content renders with title and summary

    @emids_lp_021 @capabilities @ai
    Scenario: AI relevant link operable
        Given User clicks AI capability link
        When Navigation completes
        Then Link navigates to valid AI capability destination

    @emids_lp_021 @capabilities @ai
    Scenario: AI title required
        Given AI capability card renders
        When User checks content
        Then Title field is populated
        And No empty title

    @emids_lp_021 @capabilities @ai
    Scenario: AI URL valid
        Given User examines AI destination URL
        When User clicks link
        Then URL is valid
        And Resolves to AI capability page

    @emids_lp_021 @capabilities @ai
    Scenario: Missing destination handling
        Given AI capability destination is unavailable
        When User clicks AI link
        Then User receives appropriate feedback
        And No broken page
