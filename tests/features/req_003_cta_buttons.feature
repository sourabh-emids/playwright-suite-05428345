@REQ-003
Feature: Primary CTA buttons function correctly

  @functional @user_interaction
  Scenario: Learn More CTA button navigates to expected destination
    Given User is on a page containing primary CTA buttons (Contact Us / Learn More)
    When User clicks on each important button
    Then Buttons function as intended and open the expected page, section, or modal

  @functional @user_interaction
  Scenario: See How We Deliver Outcomes button navigates correctly
    Given User is on the homepage
    When User clicks on "See How We Deliver Outcomes" button
    Then The page should navigate to the Forward-Deployed Context Engineering page

  @functional @user_interaction
  Scenario: See the model button navigates correctly
    Given User is on the homepage
    When User clicks on "See the model" button
    Then The page should navigate to the Forward-Deployed Context Engineering page

  @functional @user_interaction
  Scenario: All solutions button navigates correctly
    Given User is on the homepage
    When User clicks on "All solutions" button
    Then The page should navigate to the Solutions page

  @functional @user_interaction
  Scenario: Contact CTA button navigates to contact page
    Given User is on the homepage
    When User clicks on "Connect" CTA button
    Then The page should navigate to the Contact page
