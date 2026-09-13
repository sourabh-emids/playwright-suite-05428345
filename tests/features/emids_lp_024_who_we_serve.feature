Feature: Render five audience/industry entries

    @emids_lp_024
    Scenario: verify_all_five_audiences_visible
        Given Who We Serve section renders
        When User views section content
        Then All five audiences are visible: Payer, Provider, HealthTech, Life Sciences, Consumer

    @emids_lp_024
    Scenario: verify_explore_action_routes_correctly
        Given Each audience has Explore action
        When User clicks Explore on each audience
        Then Navigation routes to canonical segment page: /segments/payer/, /segments/provider/, /segments/healthtech/, /segments/life-sciences/, /segments/consumer/

    @emids_lp_024
    Scenario: verify_keyboard_interaction
        Given Who We Serve section renders
        When User navigates via keyboard
        Then All audience entries and Explore actions are keyboard accessible

    @emids_lp_024
    Scenario: verify_touch_interaction
        Given Who We Serve section renders on touch device
        When User interacts via touch
        Then All audience entries are touch accessible

    @emids_lp_024
    Scenario: verify_exactly_five_current_audiences
        Given Who We Serve section renders
        When Automated check counts audiences
        Then Exactly five current audiences are present for this content version

    @emids_lp_024
    Scenario: verify_urls_canonical
        Given Audience URLs are configured
        When Automated check validates URLs
        Then All audience URLs are canonical and resolve successfully

    @emids_lp_024
    Scenario: verify_one_segment_unavailable_handling
        Given One segment is unavailable
        When Section renders
        Then Only available segments display; no broken links

    @emids_lp_024
    Scenario: verify_tab_state_lost_after_resize
        Given Tab-based layout is active
        When User resizes viewport
        Then Tab state is preserved or gracefully resets without breaking layout

    @emids_lp_024
    Scenario: verify_no_duplicate_active_panels
        Given Accordion or tab layout renders
        When Automated check validates state
        Then No duplicate active panels exist simultaneously
