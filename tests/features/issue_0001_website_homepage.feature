Feature: Public website availability

  Scenario: Website homepage opens successfully
    Given the user opens the Emids homepage
    Then the homepage loads successfully without a visible error page
