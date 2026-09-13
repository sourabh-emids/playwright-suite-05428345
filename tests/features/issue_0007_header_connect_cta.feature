Feature: Header Connect CTA functionality

  Scenario: Connect CTA is visually distinct
    Given User is on Emids homepage
    When User views the header
    Then Connect CTA is visually distinct from other navigation elements

  Scenario: Connect CTA has accessible name
    Given User uses screen reader on Emids homepage
    When User encounters Connect CTA
    Then CTA has accessible name that describes the action

  Scenario: Connect CTA routes to contact page
    Given User is on Emids homepage
    When User clicks Connect CTA
    Then User is navigated to '/contact/' with valid HTTPS URL

  Scenario: Connect CTA works with keyboard activation
    Given User is on Emids homepage with keyboard focus on Connect CTA
    When User presses Enter or Space on CTA
    Then Contact page is loaded

  Scenario: CTA responsive placement preserved
    Given User views Emids homepage at various viewport widths
    When Page renders
    Then Connect CTA placement is preserved and responsive

  Scenario: Contact page unavailable handling
    Given User clicks Connect CTA
    When Contact page is unavailable (404/503)
    Then User sees appropriate error page and core navigation remains functional

  Scenario: No duplicated CTA
    Given User views header
    When User counts Connect CTAs
    Then Exactly one primary Connect CTA exists
