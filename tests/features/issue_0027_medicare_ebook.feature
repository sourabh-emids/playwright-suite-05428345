Feature: Display Medicare Advantage eBook card

  Scenario: Medicare Advantage eBook card displays correctly
    Given User views Insights section
    When Locating specific card
    Then Card titled 'Managing the Margin Reset in Medicare Advantage' is visible with eBook type

  Scenario: eBook card has imagery if available
    Given Medicare Advantage eBook has thumbnail
    When Page renders
    Then Card displays eBook cover image

  Scenario: eBook card Download action present
    Given User views Medicare Advantage card
    When Checking action
    Then Download CTA is visible on card

  Scenario: eBook card navigates to correct detail page
    Given User clicks Download on Medicare Advantage card
    When Navigation occurs
    Then User navigates to /insights/managing-the-margin-reset-in-medicare-advantage/

  Scenario: Resource removed handled
    Given Medicare Advantage resource is removed
    When Page renders
    Then Card not displayed or shows appropriate unavailable state

  Scenario: Resource gated differently handled
    Given Medicare Advantage resource now requires different access flow
    When User clicks Download
    Then User reaches updated access experience
