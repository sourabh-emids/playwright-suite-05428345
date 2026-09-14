Feature: Render footer corporate contact information

  Scenario: Corporate text readable at mobile widths
    Given User views footer on mobile viewport
    When Reading corporate text
    Then Text is readable without horizontal scroll

  Scenario: No conflict with legal navigation
    Given User views footer layout
    When Checking element overlap
    Then Corporate content does not overlap or conflict with legal navigation links

  Scenario: Address contact details render if configured
    Given Contact details are configured
    When Page renders
    Then Address and contact details display appropriately

  Scenario: Social links render if configured
    Given Social links configured
    When Page renders
    Then Social link icons or buttons display with valid destinations

  Scenario: Only approved current content published
    Given Content review
    When Checking footer content
    Then Footer displays only currently approved corporate content

  Scenario: Outdated contact info detection
    Given Contact info outdated in CMS
    When Content validation
    Then QA catches outdated info; content updated before publishing

  Scenario: External social link unavailable handled
    Given External social platform unavailable
    When User clicks social link
    Then External platform handles gracefully or error shown

  Scenario: Optional outbound analytics for social links
    Given User clicks social link
    When Tracking enabled and consented
    Then Optional analytics may track outbound navigation
