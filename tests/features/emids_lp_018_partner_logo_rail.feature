"""Feature: Render partner logo rail/marquee (emids_lp_018)."""
Feature: Render partner logo rail/marquee

    @emids_lp_018 @partnerships
    Scenario: All approved partner logos render
        Given User views partner section
        When User counts partner logos
        Then All logos present: ServiceNow, Unity, OutSystems, Kore.ai, UiPath, ONYX, TriZetto, e6data, Magical, Health Samurai, Databricks, AWS, Anthropic

    @emids_lp_018 @partnerships @accessibility
    Scenario: Meaningful accessible names for logos
        Given User with screen reader views partner logos
        When Screen reader reads logos
        Then Each logo has meaningful accessibility label
        And Partner name is announced

    @emids_lp_018 @partnerships @accessibility
    Scenario: No duplicate announcements for assistive tech
        Given Marquee uses DOM duplication for looping
        When Screen reader navigates partner section
        Then Partner list is not announced multiple times
        And Logical order maintained

    @emids_lp_018 @partnerships
    Scenario: Logo asset required validation
        Given CMS configures partners
        When Partner without logo is added
        Then Partner without logo asset does not display
        And Broken placeholder not shown

    @emids_lp_018 @partnerships @accessibility
    Scenario: Decorative logo handling
        Given Logo is treated as decorative
        When Screen reader encounters logo
        Then Appropriate alt or aria-hidden prevents redundant announcement

    @emids_lp_018 @partnerships
    Scenario: Transparent logo visibility
        Given Partner has transparent logo
        When Logo renders on page background
        Then Logo maintains sufficient visibility
        And Not invisible on background

    @emids_lp_018 @partnerships @reduced-motion
    Scenario: Reduced motion on marquee
        Given User has prefers-reduced-motion enabled
        When Partner marquee animation runs
        Then Animation pauses or reduces
        And Content remains visible and readable
