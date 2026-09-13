Feature: Implement campaign attribution parameters safely

  Scenario: Verify attribution values preserved
    Given URL contains UTM parameters or gclid
    When Page loads
    Then Attribution values (utm_source, utm_medium, utm_campaign, utm_content, utm_term, gclid) are captured for analytics/lead flow

  Scenario: Verify invalid/oversized values ignored
    Given URL contains malformed or very large UTM values
    When Page parses parameters
    Then Invalid or oversized values are ignored without causing errors

  Scenario: Verify parameter content not executed
    Given UTM parameters contain potential XSS content
    When Page processes parameters
    Then Parameter content is not executed as code; values are sanitized

  Scenario: Verify malformed query handled
    Given URL has malformed query string
    When Page parses parameters
    Then Parsing fails gracefully; no errors thrown

  Scenario: Verify repeated params handled
    Given URL has repeated query parameters
    When Page parses parameters
    Then Parameters are handled without causing unexpected behavior

  Scenario: Verify consent denied handled
    Given User has not granted analytics consent
    When Attribution parameters exist in URL
    Then Attribution may be associated with session but not shared with analytics

  Scenario: Verify full URLs not logged
    Given URL contains query parameters with potential sensitive values
    When Navigation errors are logged
    Then Full URLs are not logged if they may contain sensitive query values
