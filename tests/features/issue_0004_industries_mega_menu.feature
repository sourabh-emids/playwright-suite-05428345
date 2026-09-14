"""Feature: Industries Mega-Menu Implementation."""
Feature: Industries Mega-Menu Implementation

  @issue_0004
  Scenario: five_audience_destinations_present
    Given Industries menu is open
    When User views menu items
    Then Menu contains Payer, Provider, HealthTech, Life Sciences, and Consumer destinations

  @issue_0004
  Scenario: all_audience_links_keyboard_accessible
    Given Industries menu is open
    When User uses keyboard navigation
    Then Each of five audience destinations is reachable without mouse

  @issue_0004
  Scenario: audience_canonical_urls
    Given Audience links are rendered
    When URLs are checked
    Then Links use canonical URLs: /segments/payer/, /segments/provider/, /segments/healthtech/, /segments/life-sciences/, /segments/consumer/

  @issue_0004
  Scenario: desktop_grouped_industries_menu
    Given Page at desktop viewport
    When Industries menu opens
    Then Menu presents grouped navigation

  @issue_0004
  Scenario: mobile_stacked_industries_list
    Given Page at mobile viewport
    When Industries menu opens
    Then Menu presents stacked list or disclosure

  @issue_0004
  Scenario: one_segment_unpublished_handling
    Given One segment page is unpublished
    When Industries menu renders
    Then Unpublished segment does not appear or shows appropriate unavailable state
