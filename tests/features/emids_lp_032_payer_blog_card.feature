Feature: Display Payer data readiness blog card

    @emids_lp_032
    Scenario: verify_payer_blog_title_displayed
        Given Payer data readiness blog card renders
        When User views card title
        Then Title displays as 'Payers: Is Your Data Ready for AI?'

    @emids_lp_032
    Scenario: verify_blog_type_label
        Given Payer blog card renders
        When Automated check validates type
        Then Card type is Blog

    @emids_lp_032
    Scenario: verify_read_more_action
        Given Payer blog card renders
        When User views CTA
        Then Read More action is displayed (not Download)

    @emids_lp_032
    Scenario: verify_article_navigation
        Given User clicks Read More
        When Navigation completes
        Then Link opens correct article/detail experience

    @emids_lp_032
    Scenario: verify_cta_label_article_not_download
        Given Blog content card data
        When Automated check validates CTA
        Then CTA label reflects article navigation, not file download

    @emids_lp_032
    Scenario: verify_article_moved_handling
        Given Payer blog article has moved
        When User clicks Read More
        Then Redirect or appropriate error handling

    @emids_lp_032
    Scenario: verify_title_truncation_handling
        Given Blog title is long
        When Card renders at mobile width
        Then Title truncates or wraps appropriately
