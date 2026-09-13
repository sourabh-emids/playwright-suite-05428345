Feature: Render AI capability content

    @emids_lp_021
    Scenario: verify_ai_label_and_content_render
        Given AI capability section renders
        When User views AI capability content
        Then AI label and supporting content are displayed

    @emids_lp_021
    Scenario: verify_ai_link_operable
        Given AI capability link exists
        When User clicks or activates AI link/CTA
        Then Navigation to AI capability destination works

    @emids_lp_021
    Scenario: verify_ai_title_required
        Given AI capability data
        When Automated check validates content
        Then Title field is required and non-empty

    @emids_lp_021
    Scenario: verify_ai_url_valid
        Given AI capability URL is configured
        When Automated check tests URL
        Then URL resolves successfully

    @emids_lp_021
    Scenario: verify_card_matches_visual_system
        Given AI capability card renders
        When User views card design
        Then Card matches the capability visual system styling

    @emids_lp_021
    Scenario: verify_missing_destination_handling
        Given AI capability destination URL is missing
        When Card renders
        Then Card displays with disabled link or validation catches error
