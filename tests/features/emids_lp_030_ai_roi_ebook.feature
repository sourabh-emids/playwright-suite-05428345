Feature: Display AI ROI eBook card

    @emids_lp_030
    Scenario: verify_ai_roi_title_displayed
        Given AI ROI eBook card renders
        When User views card title
        Then Title displays as 'Closing the AI ROI Gap in Healthcare'

    @emids_lp_030
    Scenario: verify_ai_roi_ebook_label
        Given AI ROI card renders
        When Automated check validates type
        Then Card is labeled as eBook

    @emids_lp_030
    Scenario: verify_ai_roi_expected_action
        Given AI ROI eBook card renders
        When User views CTA
        Then Expected action is displayed

    @emids_lp_030
    Scenario: verify_ai_roi_published_content
        Given AI ROI eBook data
        When Automated check validates status
        Then Content is published and URL is valid

    @emids_lp_030
    Scenario: verify_unpublished_redirect_handling
        Given AI ROI resource is unpublished or redirected
        When Card or link is accessed
        Then Appropriate handling: redirect to new location or removal
