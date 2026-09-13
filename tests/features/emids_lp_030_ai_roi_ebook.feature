Feature: Display AI ROI eBook card

  Scenario: Verify AI ROI eBook card renders
    Given AI ROI eBook is configured
    When Insight card renders
    Then Card displays title 'Closing the AI ROI Gap in Healthcare' with eBook labeling

  Scenario: Verify expected action displayed
    Given AI ROI eBook card renders
    When User views card action
    Then Download action is displayed per content flow

  Scenario: Verify published content with valid URL
    Given AI ROI eBook is configured
    When Card renders
    Then Content is published and destination URL resolves successfully

  Scenario: Verify unpublished resource handled
    Given AI ROI eBook is unpublished or redirected
    When User attempts to access
    Then Appropriate handling without showing broken content
