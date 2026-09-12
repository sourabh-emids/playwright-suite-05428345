"""Feature file for Issue 0030 - AI ROI eBook card display."""
Feature: AI ROI eBook card display

  Scenario: AI ROI eBook renders with correct labeling
    Given A user views the AI ROI eBook card
    When The card renders
    Then Card displays 'Closing the AI ROI Gap in Healthcare' with eBook labeling and expected action

  Scenario: AI ROI eBook published content and valid URL
    Given A user examines the AI ROI eBook card
    When The content is analyzed
    Then Content is published and URL is valid

  Scenario: Unpublished/redirected resource handling
    Given The AI ROI resource is unpublished or redirected
    When The Insights section renders
    Then Appropriate handling occurs without breaking page
