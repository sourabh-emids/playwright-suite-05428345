Feature: Display Payer data readiness blog card

  Scenario: Verify Blog type and Read More action shown
    Given Payer data readiness blog is configured
    When Insight card renders
    Then Card displays type 'Blog' with 'Read More' action

  Scenario: Verify correct title displayed
    Given Payer data readiness blog is configured
    When Card renders
    Then Card displays title 'Payers: Is Your Data Ready for AI?'

  Scenario: Verify link opens correct article
    Given Payer data readiness blog card renders
    When User clicks Read More
    Then Navigation opens correct article/detail experience

  Scenario: Verify CTA label reflects article navigation
    Given Card is for blog article
    When User views action label
    Then Action label is 'Read More', not 'Download' (since this is article, not file)

  Scenario: Verify article moved handled
    Given Payer data readiness article has moved
    When User clicks Read More
    Then Redirect to new location or appropriate error handling

  Scenario: Verify title truncation handled
    Given Payer data readiness blog has very long title
    When Card renders
    Then Title truncates gracefully with ellipsis or wraps without breaking layout
