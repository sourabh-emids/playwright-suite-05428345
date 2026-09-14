Feature: Display FinOps healthcare payer card

  Scenario: FinOps healthcare payer card renders
    Given User views Insights section
    When Locating FinOps card
    Then FinOps best-practices card for healthcare payers displays

  Scenario: FinOps card title type action present
    Given User examines FinOps card
    When Checking content
    Then Card has title, content type, and CTA action visible

  Scenario: FinOps card routes correctly
    Given User clicks FinOps card CTA
    When Navigation occurs
    Then User navigates to configured FinOps resource destination

  Scenario: Broken link handled
    Given FinOps resource link is broken
    When User clicks card
    Then Error page displays or card not rendered

  Scenario: Missing thumbnail handled
    Given FinOps card has no thumbnail
    When Page renders
    Then Card renders without broken image placeholder
