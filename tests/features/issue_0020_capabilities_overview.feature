"""Feature: Capabilities Overview Rendering."""
Feature: Capabilities Overview Rendering

  @issue_0020
  Scenario: three_capability_groups_visible
    Given Capabilities section renders
    When Content is reviewed
    Then All three groups (AI, Engineering, Platforms) are visible

  @issue_0020
  Scenario: capability_groups_have_content_actions
    Given Each capability group renders
    When Groups are checked for corresponding content/actions
    Then All three groups have corresponding content/actions

  @issue_0020
  Scenario: group_labels_match_navigation_taxonomy
    Given Capability group labels
    When Compared to navigation taxonomy
    Then Labels (AI, Engineering, Platforms) match navigation taxonomy

  @issue_0020
  Scenario: three_primary_groups_required
    Given Capabilities section is configured
    When Group count is validated
    Then Exactly three primary groups exist for this content version

  @issue_0020
  Scenario: responsive_capability_cards_panels
    Given Capabilities section renders across viewports
    When Viewport changes
    Then Responsive cards/panels adapt appropriately

  @issue_0020
  Scenario: group_missing_handling
    Given One capability group is not configured
    When Section renders
    Then Missing group handled gracefully

  @issue_0020
  Scenario: mislabeled_taxonomy_handling
    Given Group label does not match approved taxonomy
    When Section renders
    Then Content governance ensures correct labeling

  @issue_0021
  Scenario: ai_label_and_content_render
    Given Capabilities section renders
    When AI group is checked
    Then AI label and supporting content render correctly

  @issue_0021
  Scenario: ai_capability_link_operable
    Given AI capability has associated link
    When Link is activated
    Then Link routes to valid AI capability destination

  @issue_0021
  Scenario: ai_capability_title_required
    Given AI capability is configured
    When Title field is validated
    Then Title is present and non-empty

  @issue_0021
  Scenario: ai_capability_url_valid
    Given AI capability link is configured
    When URL is validated
    Then URL is valid and resolves

  @issue_0021
  Scenario: ai_card_visual_system
    Given AI capability renders
    When Visual design is reviewed
    Then Card/panel matches capability visual system

  @issue_0021
  Scenario: ai_capability_missing_destination
    Given AI capability link destination is unavailable
    When Link is clicked
    Then Graceful handling occurs

  @issue_0022
  Scenario: engineering_label_and_content_render
    Given Capabilities section renders
    When Engineering group is checked
    Then Engineering label and supporting content render correctly

  @issue_0022
  Scenario: engineering_capability_link_operable
    Given Engineering capability has associated link
    When Link is activated
    Then Link routes to valid engineering capability destination

  @issue_0022
  Scenario: engineering_capability_title_required
    Given Engineering capability is configured
    When Title field is validated
    Then Title is present and non-empty

  @issue_0022
  Scenario: engineering_capability_url_valid
    Given Engineering capability link is configured
    When URL is validated
    Then URL is valid and resolves

  @issue_0022
  Scenario: engineering_card_visual_system
    Given Engineering capability renders
    When Visual design is reviewed
    Then Card/panel matches capability visual system

  @issue_0023
  Scenario: platforms_content_renders
    Given Capabilities section renders
    When Platforms group is checked
    Then Platforms content renders correctly

  @issue_0023
  Scenario: platforms_labels_consistent_across_nav_body
    Given Platforms capability renders
    When Navigation and body labels are compared
    Then Labels use approved taxonomy consistently (e.g., 'Platforms' not alternate synonyms)

  @issue_0023
  Scenario: platforms_capability_title_required
    Given Platforms capability is configured
    When Title field is validated
    Then Title is present and non-empty

  @issue_0023
  Scenario: platforms_card_visual_system
    Given Platforms capability renders
    When Visual design is reviewed
    Then Card/panel matches capability visual system

  @issue_0023
  Scenario: navigation_body_naming_mismatch_handling
    Given CMS content has inconsistent synonyms for Platforms
    When Section renders
    Then Content governance prevents or corrects inconsistent naming
