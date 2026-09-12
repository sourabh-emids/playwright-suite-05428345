@issue_0044
Feature: YouTube embeds conditional loading

  As a user, I want YouTube videos to load only after consent
  so that my media preferences are respected.

  Background:
    Given I navigate to the homepage

  Scenario: YouTube embeds load conditionally
    When I view a page with YouTube content
    Then YouTube should not load before consent
