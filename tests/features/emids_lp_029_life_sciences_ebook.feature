Feature: Display Life Sciences eBook card

    @emids_lp_029
    Scenario: verify_life_sciences_title_correct
        Given Life Sciences eBook card renders
        When User views card title
        Then Title displays as 'Unlocking Trusted Digital Transformation in Life Sciences'

    @emids_lp_029
    Scenario: verify_life_sciences_download_action
        Given Life Sciences eBook card renders
        When User views CTA
        Then Download action opens correct detail/access experience

    @emids_lp_029
    Scenario: verify_life_sciences_canonical_url
        Given Life Sciences eBook URL is configured
        When Automated check validates URL
        Then URL is canonical: /insights/unlocking-trusted-digital-transformation-in-life-sciences/

    @emids_lp_029
    Scenario: verify_resource_access_unavailable_handling
        Given Life Sciences resource access flow unavailable
        When User clicks Download
        Then Graceful error handling; user not left with broken experience
