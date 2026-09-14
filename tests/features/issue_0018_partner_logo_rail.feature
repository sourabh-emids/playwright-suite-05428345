"""Feature: Partner Logo Rail/Marquee Rendering."""
Feature: Partner Logo Rail/Marquee Rendering

  @issue_0018
  Scenario: all_approved_partner_logos_render
    Given Partnerships section renders
    When Partner logos are counted
    Then All 13 approved partners render: ServiceNow, Unity, OutSystems, Kore.ai, UiPath, ONYX, TriZetto, e6data, Magical, Health Samurai, Databricks, AWS, Anthropic

  @issue_0018
  Scenario: partner_logos_meaningful_accessible_names
    Given Partner logos render
    When Accessibility inspection occurs
    Then All partner logos have meaningful accessible names

  @issue_0018
  Scenario: no_duplication_for_assistive_tech
    Given DOM uses duplication for looping animation
    When Screen reader visits section
    Then Logical partner list does not duplicate for assistive technologies

  @issue_0018
  Scenario: logo_asset_required
    Given Partner is configured
    When Logo renders
    Then Logo asset is present (or fallback handling)

  @issue_0018
  Scenario: alt_required_unless_decorative
    Given Partner logo is not paired with adjacent partner name text
    When Alt/accessibility label is checked
    Then Alt text is required unless logo is decorative with adjacent text

  @issue_0018
  Scenario: horizontal_logo_sequence
    Given Partnerships section renders
    When Layout is reviewed
    Then Logos present in horizontal sequence

  @issue_0018
  Scenario: missing_logo_handling
    Given Partner logo asset is missing
    When Section renders
    Then Fallback is displayed or graceful handling occurs

  @issue_0018
  Scenario: transparent_logo_on_background
    Given Logo has transparent areas on current background
    When Section renders
    Then Logo remains visible and distinguishable
