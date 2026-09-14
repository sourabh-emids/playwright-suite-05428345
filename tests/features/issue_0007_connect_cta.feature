Feature: Provide header Connect CTA

  Scenario: Connect CTA is visually distinct
    Given User views the header
    When User identifies the Connect CTA
    Then CTA has visual differentiation from standard navigation links

  Scenario: Connect CTA has accessible name
    Given User inspects the CTA element
    When Checking accessibility attributes
    Then CTA has descriptive accessible name describing the action

  Scenario: Connect CTA routes to contact page
    Given User clicks the Connect CTA
    When Navigation occurs
    Then User lands on /contact/ page with valid HTTPS URL

  Scenario: Connect CTA keyboard activation works
    Given User focuses on Connect CTA
    When User presses Enter or Space key
    Then Contact page navigation is triggered

  Scenario: Connect CTA responsive placement preserved
    Given User views site on mobile device
    When Header renders in mobile layout
    Then Connect CTA remains visible and accessible in mobile header

  Scenario: Connect CTA handles contact page unavailable
    Given Contact page returns 404 or error
    When User clicks Connect CTA
    Then Error page displays or fallback content is shown

  Scenario: Connect CTA text wrapping acceptable
    Given Narrow viewport with Connect CTA
    When CTA text is long
    Then Text wraps gracefully without breaking functionality or overlapping
