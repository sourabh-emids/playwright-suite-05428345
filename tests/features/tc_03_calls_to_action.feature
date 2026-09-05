@TC-03 @functional @call-to-action
Feature: Important call-to-action links open expected destinations
  Contact Us and Learn More links must take the user to their expected pages.

  Scenario: Contact Us opens the contact page
    Given the Emids homepage is open
    When the user selects Contact Us from the Company menu
    Then the Emids contact page opens

  Scenario: Learn More opens the selected partner page
    Given the Emids partners page is open
    When the user selects Learn More for Snowflake
    Then the Snowflake partner page opens
