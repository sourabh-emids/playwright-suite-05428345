Feature: Important buttons perform their expected actions
  As a visitor
  I want important calls to action to work
  So that I can contact Emids or learn how it delivers outcomes

  Scenario: The header Connect action opens the contact page
    Given the homepage is loaded for calls to action
    When the visitor selects the header Connect action
    Then the contact page opens successfully

  Scenario: The Company menu Contact Us action opens the contact page
    Given the homepage is loaded for calls to action
    When the visitor selects Contact Us from the Company menu
    Then the contact page opens successfully

  Scenario: The hero outcomes action opens its destination
    Given the homepage is loaded for calls to action
    When the visitor selects the See How We Deliver Outcomes action
    Then the outcomes page opens successfully
