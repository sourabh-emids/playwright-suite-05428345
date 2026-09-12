Feature: Footer corporate/contact information

  Scenario: Footer info readable at mobile widths
    Given Footer at mobile viewport
    When Content renders
    Then Corporate information remains readable

  Scenario: No conflict with legal navigation
    Given Footer layout
    When Content is verified
    Then Corporate info does not conflict with legal navigation

  Scenario: Social links functional if configured
    Given Social links in footer
    When Links are tested
    Then Social links navigate to valid destinations

  Scenario: Only approved current content
    Given Footer corporate content
    When Content is verified
    Then Only approved and current content is published
