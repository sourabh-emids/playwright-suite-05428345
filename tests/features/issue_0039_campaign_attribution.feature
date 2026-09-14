Feature: Implement campaign attribution safely

  Scenario: UTM parameters preserved where permitted
    Given User lands on page via UTM-tagged URL
    When Page renders
    Then UTM parameters are captured for analytics/attribution

  Scenario: gclid preserved where applicable
    Given User arrives via Google Ads click
    When Page renders
    Then gclid parameter is captured for attribution

  Scenario: Invalid values ignored
    Given URL contains malformed UTM parameter
    When Attribution values processed
    Then Invalid values are sanitized/ignored; page continues normally

  Scenario: Oversized values handled
    Given UTM parameter exceeds reasonable length
    When Processing attribution
    Then Oversized values are truncated or ignored

  Scenario: Parameter content not executed
    given Malicious UTM value with script injection
    when Attribution processed
    Then Parameter content is never executed; values are escaped/sanitized

  Scenario: Full URLs not logged
    Given Analytics logging
    when Logging attribution context
    Then Full URLs with query parameters are not logged to prevent sensitive data exposure

  Scenario: Consent required for attribution tracking
    Given User has not granted consent
    when Attribution values available
    Then Attribution tracking respects consent state

  Scenario: Repeated parameters handled
    Given URL contains duplicate UTM parameters
    When Processing values
    Then Duplicate parameters handled consistently (first or last value)
