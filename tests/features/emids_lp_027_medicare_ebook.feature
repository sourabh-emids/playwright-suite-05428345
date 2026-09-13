Feature: Display Medicare Advantage eBook card

    @emids_lp_027
    Scenario: verify_medicare_ebook_title_correct
        Given Medicare Advantage eBook card renders
        When User views card title
        Then Title displays as 'Managing the Margin Reset in Medicare Advantage'

    @emids_lp_027
    Scenario: verify_medicare_ebook_type
        Given Medicare Advantage card renders
        When Automated check validates card type
        Then Card type is eBook

    @emids_lp_027
    Scenario: verify_medicare_ebook_download_action
        Given Medicare Advantage eBook card renders
        When User views CTA
        Then Download action is displayed

    @emids_lp_027
    Scenario: verify_medicare_ebook_url_resolves
        Given Medicare Advantage eBook URL is configured
        When Automated check tests URL
        Then URL resolves to /insights/managing-the-margin-reset-in-medicare-advantage/

    @emids_lp_027
    Scenario: verify_medicare_ebook_image_if_available
        Given Medicare Advantage eBook has imagery configured
        When Card renders
        Then Image displays correctly; if unavailable, fallback shown

    @emids_lp_027
    Scenario: verify_resource_removed_handling
        Given Medicare Advantage resource is removed
        When Card attempts to render
        Then Validation catches removed resource or graceful handling
