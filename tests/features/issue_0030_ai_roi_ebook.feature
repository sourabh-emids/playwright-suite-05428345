Feature: Display AI ROI eBook card

  Scenario: AI ROI eBook card renders with eBook labeling
    Given User views Insights section
    When Locating AI ROI card
    Then Card titled 'Closing the AI ROI Gap in Healthcare' displays with eBook type

  Scenario: AI ROI card has expected action
    Given User views AI ROI card
    When Checking CTA
    Then Download or Read More action visible per card configuration

  Scenario: AI ROI card has published content
    Given CMS validation
    When Checking content status
    Then AI ROI resource is in published state

  Scenario: AI ROI card has valid URL
    Given User inspects AI ROI URL
    When Checking validity
    Then URL resolves to valid AI ROI detail page

  Scenario: Unpublished or redirected resource handled
    Given AI ROI resource unpublished or redirected
    When Page renders
    Then Card either not displayed or shows current status
