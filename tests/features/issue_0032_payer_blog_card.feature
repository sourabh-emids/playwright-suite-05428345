Feature: Display Payer data readiness blog card

  Scenario: Payer data readiness blog card displays Blog type
    Given User views Insights section
    When Locating blog card
    Then Card titled 'Payers: Is Your Data Ready for AI?' displays with type=Blog

  Scenario: Blog Read More action visible
    Given User views Payer blog card
    When Checking CTA
    Then Read More action visible (not Download)

  Scenario: Blog CTA label reflects article navigation
    Given User validates CTA labels
    When Checking semantic accuracy
    Then Blog content uses Read More rather than Download

  Scenario: Blog link opens article experience
    Given User clicks Read More
    When Navigation occurs
    Then User navigates to configured blog URL

  Scenario: Article moved handled
    Given Blog article URL has changed
    When User clicks Read More
    Then Navigation resolves to new URL or broken link flagged

  Scenario: Title truncation handled gracefully
    Given Blog title is very long
    When Card renders at standard width
    Then Title truncates with ellipsis or displays fully without breaking layout
