Feature: TC-01 Website homepage availability
  Verify the public homepage can be opened without an obvious error page.

  Scenario: Homepage opens successfully
    Given the TC-01 user opens the Emids homepage
    Then the TC-01 homepage is loaded without an obvious error
