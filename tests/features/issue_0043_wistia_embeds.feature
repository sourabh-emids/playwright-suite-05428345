@issue_0043
Feature: Wistia embeds conditional loading

  As a user, I want Wistia videos to load only after consent
  so that my media preferences are respected.

  Background:
    Given I navigate to the homepage

  Scenario: Wistia embeds load conditionally
    When I view a page with video content
    Then Wistia should not load before consent
