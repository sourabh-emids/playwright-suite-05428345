Feature: Render footer corporate contact info

    @emids_lp_046
    Scenario: verify_footer_readable_mobile
        Given Footer renders on mobile viewport
        When User views footer content
        Then Footer information remains readable and does not conflict with legal navigation

    @emids_lp_046
    Scenario: verify_only_approved_content
        Given Footer corporate content is configured
        When Page renders
        Then Only approved current content is published

    @emids_lp_046
    Scenario: verify_social_links_valid
        Given Social links are configured
        When Automated check tests destinations
        Then Social links point to valid public destinations

    @emids_lp_046
    Scenario: verify_outdated_contact_info_detection
        Given Contact info in footer
        When Content validation runs
        Then Outdated contact information is caught before production

    @emids_lp_046
    Scenario: verify_external_social_unavailable_handling
        Given External social link is unavailable
        When User clicks social link
        Then Appropriate handling; site does not break

    @emids_lp_046
    Scenario: verify_optional_social_analytics
        Given Social links render
        When User clicks social link (with consent)
        Then Optional outbound-link analytics may be tracked
