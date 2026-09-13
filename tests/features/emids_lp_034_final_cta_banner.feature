Feature: Render final conversion banner

  Scenario: Verify banner appears before footer
    Given Homepage renders
    When User scrolls to bottom of page
    Then Final conversion banner appears before footer section

  Scenario: Verify primary action is clear and keyboard operable
    Given Final CTA banner renders
    When User focuses on primary action via keyboard
    Then Primary CTA is visible, clear, and activatable via keyboard

  Scenario: Verify supporting timing/message readable
    Given Final CTA banner renders
    When User views supporting content
    Then Timing and message content are readable

  Scenario: Verify required fields present
    Given Final CTA is configured
    When Banner renders
    Then Required message and CTA fields are present and not empty

  Scenario: Verify high-contrast visual treatment
    Given Final CTA banner renders
    When User views the section
    Then Section has high-contrast visual treatment per design

  Scenario: Verify CTA text wrapping handled
    Given Final CTA button has long text
    When Banner renders at narrow viewport
    Then CTA text wraps gracefully without breaking button

  Scenario: Verify no footer overlap
    Given Final CTA banner and footer render
    When Page loads or resizes
    Then Banner and footer do not overlap or obscure each other

  Scenario: Verify contact route unavailable handled
    Given Contact page is unavailable
    When User clicks final CTA
    Then Graceful error handling without page break
