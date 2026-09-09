@issue_0001
Feature: Public homepage availability

  Scenario: Homepage opens successfully
    Given the public homepage is open
    Then the homepage primary content is displayed without an error page
