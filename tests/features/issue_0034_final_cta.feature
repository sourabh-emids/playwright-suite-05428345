Feature: Final conversion banner rendering

  Scenario: Banner appears before footer
    Given User views Emids homepage
    When User scrolls to bottom of page
    Then Final conversion banner appears before footer

  Scenario: Primary action is clear
    Given User views Final CTA section
    When User looks for primary action
    Then Primary action is clear and visually prominent

  Scenario: Primary action keyboard operable
    Given User tabs to Final CTA section
    When Focus reaches primary action
    Then Action is keyboard operable

  Scenario: Supporting content readable
    Given User views Final CTA section
    When Page renders
    Then Supporting timing/message content is readable

  Scenario: Required fields present
    Given Final CTA section renders
    When User validates content
    Then Required message and CTA fields are present

  Scenario: High contrast closing CTA
    Given User views Final CTA section
    When User assesses contrast
    Then Section has high-contrast design

  Scenario: CTA text wrapping handled
    Given User views Final CTA at narrow viewport
    When Page renders
    Then CTA text wraps appropriately without breaking

  Scenario: No footer overlap
    Given User views Final CTA section
    When Page renders
    Then CTA does not overlap footer

  Scenario: Contact route unavailable handling
    Given User clicks Final CTA
    When Contact route is unavailable
    Then User sees appropriate error handling
