"""Feature: Insights Navigation Group."""
Feature: Insights Navigation Group

  @issue_0005
  Scenario: insights_control_opens_reliably
    Given User is on page with header
    When User activates Insights navigation control
    Then Insights control opens reliably with visible response

  @issue_0005
  Scenario: insights_child_links_readable_operable
    Given Insights menu is open
    When User views child links at all supported breakpoints
    Then Child links are readable and operable

  @issue_0005
  Scenario: insights_no_empty_menu_groups
    Given Insights navigation group is configured
    When Menu renders
    Then No empty menu groups are displayed

  @issue_0005
  Scenario: insights_destination_canonical_urls
    Given Insight links are rendered
    When URLs are validated
    Then Destination URLs are canonical

  @issue_0005
  Scenario: insights_hover_interaction_accessible
    Given User with mouse interacts with Insights menu
    When User hovers over menu items
    Then Interaction does not prevent keyboard/touch access
