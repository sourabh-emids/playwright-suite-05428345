Feature: Main buttons functionality and navigation

  Scenario: Contact Us button opens contact form
    Given The user is on the homepage
    When The user clicks the Contact Us button
    Then The user is navigated to the contact page or a contact form modal opens displaying contact fields such as name, email, phone, and message

  Scenario: Learn More button navigates to expected page
    Given The user is on the homepage
    When The user clicks the Learn More button
    Then The user is navigated to the appropriate section or page with more detailed information about the featured service or offering

  Scenario: Call to Action buttons function correctly
    Given The user is on the homepage or any inner page
    When The user clicks primary Call to Action buttons such as Get Started, Request a Demo, or Explore Solutions
    Then Each button performs its intended action which may include navigating to a form, starting a chat, or redirecting to a relevant landing page

  Scenario: Buttons display hover and active states
    Given The user is viewing the homepage
    When The user hovers over and clicks on main buttons
    Then Buttons display appropriate visual feedback for hover state and pressed or active state to confirm interaction

  Scenario: Footer buttons navigate correctly
    Given The user has scrolled to the footer section
    When The user clicks on buttons in the footer such as social media links or newsletter subscription buttons
    Then Each footer button opens the correct destination such as social media profiles, email client with pre-filled address, or expands the subscription form
