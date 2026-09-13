Feature: Render Engineering capability content

    @emids_lp_022
    Scenario: verify_engineering_label_and_content_render
        Given Engineering capability section renders
        When User views Engineering capability content
        Then Engineering label and supporting content are displayed

    @emids_lp_022
    Scenario: verify_engineering_link_operable
        Given Engineering capability link exists
        When User clicks or activates link/CTA
        Then Navigation to Engineering capability destination works

    @emids_lp_022
    Scenario: verify_engineering_title_required
        Given Engineering capability data
        When Automated check validates content
        Then Title field is required and non-empty

    @emids_lp_022
    Scenario: verify_engineering_url_valid
        Given Engineering capability URL is configured
        When Automated check tests URL
        Then URL resolves successfully

    @emids_lp_022
    Scenario: verify_engineering_card_visual_system
        Given Engineering capability card renders
        When User views card design
        Then Card matches the capability visual system styling
