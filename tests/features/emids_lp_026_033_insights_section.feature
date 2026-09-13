"""Feature: Render Insights section and content cards (emids_lp_026-033)."""
Feature: Render Insights section and content cards

    @emids_lp_026 @insights
    Scenario: Six cards render with required fields
        Given User views Insights section
        When User counts and reads cards
        Then Six cards render
        And Each has content type, title, and Download/Read More action

    @emids_lp_026 @insights
    Scenario: Image where configured displays
        Given Card includes image
        When Card renders
        Then Image displays
        And Accessible alternative text or empty alt for decorative

    @emids_lp_026 @insights @responsive
    Scenario: Cards accessible at all breakpoints
        Given User views Insights on various viewports
        When Cards render
        Then Cards remain accessible
        And Content readable
        And No overflow

    @emids_lp_026 @insights
    Scenario: Published content only
        Given CMS manages insight content
        When Content renders
        Then Only published insight cards display
        And Drafts unavailable content not shown

    @emids_lp_026 @insights
    Scenario: Title and URL required validation
        Given CMS configures insight cards
        When Card saves without title or URL
        Then Validation prevents save
        And Empty cards not rendered

    @emids_lp_026 @insights
    Scenario: Action label matches content flow
        Given Card contains downloadable asset
        When Card renders
        Then Action label says 'Download'
        And For articles shows 'Read More'

    @emids_lp_027 @insights @ebook
    Scenario: Medicare Advantage eBook displays correctly
        Given User views Insights section
        When User locates Medicare Advantage card
        Then Card shows title 'Managing the Margin Reset in Medicare Advantage'
        And Type eBook
        And Imagery if available
        And Download action

    @emids_lp_027 @insights @ebook
    Scenario: eBook action routes correctly
        Given User clicks Download on Medicare Advantage eBook
        When Navigation completes
        Then Browser navigates to /insights/managing-the-margin-reset-in-medicare-advantage/

    @emids_lp_028 @insights
    Scenario: CMS-0057 card renders with populated content
        Given User views Insights section
        When User locates CMS-0057 card
        Then Card shows title, type, image if available, and action from approved content

    @emids_lp_028 @insights
    Scenario: CMS-0057 navigation to intended resource
        Given User clicks CMS-0057 card action
        When Navigation completes
        Then Browser navigates to configured resource destination

    @emids_lp_028 @insights
    Scenario: No empty title or destination
        Given CMS configures CMS-0057 card
        When Card saves
        Then Title and destination required
        And Validation prevents empty fields

    @emids_lp_029 @insights @ebook
    Scenario: Life Sciences eBook displays correctly
        Given User views Insights section
        When User locates Life Sciences card
        Then Card shows title 'Unlocking Trusted Digital Transformation in Life Sciences'
        And Type eBook
        And Download action

    @emids_lp_029 @insights @ebook
    Scenario: eBook routes to correct access experience
        Given User clicks Download on Life Sciences eBook
        When Navigation completes
        Then Browser navigates to /insights/unlocking-trusted-digital-transformation-in-life-sciences/

    @emids_lp_030 @insights @ebook
    Scenario: AI ROI eBook displays with eBook label
        Given User views Insights section
        When User locates AI ROI card
        Then Card shows title 'Closing the AI ROI Gap in Healthcare'
        And Type eBook
        And Expected action

    @emids_lp_030 @insights @ebook
    Scenario: AI ROI eBook has valid destination
        Given User examines AI ROI card destination
        When User clicks action
        Then URL is valid
        And Resolves to configured AI ROI detail page

    @emids_lp_031 @insights
    Scenario: FinOps resource card renders
        Given User views Insights section
        When User locates FinOps resource
        Then Card renders with title, type, image if available, and action routing correctly

    @emids_lp_031 @insights
    Scenario: Valid destination required
        Given User clicks FinOps resource action
        When Navigation completes
        Then Browser navigates to configured FinOps resource destination

    @emids_lp_031 @insights
    Scenario: Missing thumbnail handling
        Given FinOps card configured without image
        When Page renders
        Then Card displays without image
        And No broken placeholder

    @emids_lp_032 @insights @blog
    Scenario: Blog card shows Blog type and Read More action
        Given User views Insights section
        When User locates Payers data readiness blog
        Then Card shows title 'Payers: Is Your Data Ready for AI?'
        And Type Blog
        And Read More action (not Download)

    @emids_lp_032 @insights @blog
    Scenario: Blog links to article experience
        Given User clicks Read More on blog card
        When Navigation completes
        Then Browser navigates to configured blog URL

    @emids_lp_032 @insights @blog
    Scenario: CTA label reflects article navigation
        Given User views blog card actions
        When User checks CTA text
        Then CTA says 'Read More' not 'Download' for article content

    @emids_lp_033 @insights
    Scenario: Download reaches resource detail access flow
        Given User clicks Download on eBook card
        When Navigation completes
        Then User reaches resource detail/access experience
        And Not direct file download

    @emids_lp_033 @insights
    Scenario: Gate clearly communicates required steps
        Given Resource requires form/gate
        When User reaches resource detail page
        Then Gate communicates required steps clearly
        And User understands next action
