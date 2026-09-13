Feature: Render footer corporate/contact information

  Scenario: Verify footer info readable at mobile widths
    Given Footer renders at mobile viewport
    When User views corporate/contact information
    Then Text remains readable; no overlap or truncation issues

  Scenario: Verify no conflict with legal navigation
    Given Footer renders corporate info and legal navigation
    When User views footer
    Then Corporate/contact information does not overlap or conflict with legal navigation

  Scenario: Verify approved current content only
    Given Corporate information is configured
    When Footer renders
    Then Only approved current content is published

  Scenario: Verify social links functional
    Given Social links are configured in footer
    When User clicks social links
    Then Links navigate to valid external social destinations

  Scenario: Verify address/contact details handled if configured
    Given Footer includes address or contact details
    When Page renders
    Then Details display correctly; placeholder used if not configured

  Scenario: Verify outdated contact info flagged
    Given Contact information in footer is outdated
    When Content is published
    Then CMS workflow flags outdated content for update

  Scenario: Verify external social link unavailable handled
    Given Social platform is temporarily unavailable
    When User clicks social link
    Then Appropriate error handling or redirect
