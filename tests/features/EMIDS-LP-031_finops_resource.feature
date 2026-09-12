Feature: FinOps healthcare payer resource card

  Scenario: FinOps resource renders correctly
    Given FinOps healthcare payer resource card
    When Card is verified
    Then Title, type, and action render and route correctly

  Scenario: Valid destination
    Given FinOps card link
    When URL is tested
    Then Destination is valid
