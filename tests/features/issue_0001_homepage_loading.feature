Feature: Homepage loads without errors

  Scenario: Verify homepage loads successfully
    Given A user has access to a web browser
    When The user navigates to https://www.emids.com/
    Then The homepage loads successfully without obvious errors
