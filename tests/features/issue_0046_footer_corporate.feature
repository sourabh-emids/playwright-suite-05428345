Feature: Footer corporate and contact information

  Scenario: Corporate text readable at mobile
    Given User views footer at mobile width
    When Page renders
    Then Corporate text remains readable

  Scenario: Address/contact details if configured
    Given Address/contact details are configured
    When Page renders
    Then Address/contact details display where configured

  Scenario: Social links present if configured
    Given Social links are configured
    When Page renders
    Then Social links display

  Scenario: No conflict with legal navigation
    Given User views footer
    When Footer renders
    Then Corporate information does not conflict with legal navigation

  Scenario: Only approved current content
    Given Footer renders
    When User validates content
    Then Only approved current corporate content is published

  Scenario: Responsive footer layout
    Given User views footer at various viewport widths
    When Page renders
    Then Footer layout is responsive

  Scenario: Outdated contact info detection
    Given Contact information is outdated
    When Content is managed in CMS
    Then CMS workflow alerts for outdated content

  Scenario: External social link unavailable handling
    Given External social link is unavailable
    When User clicks social link
    Then Appropriate handling occurs
