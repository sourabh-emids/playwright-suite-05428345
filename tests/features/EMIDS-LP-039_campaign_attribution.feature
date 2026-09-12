Feature: Campaign attribution parameters safe handling

  Scenario: Attribution values preserved where permitted
    Given UTM parameters or gclid in URL
    When Page loads
    Then Values can be associated with analytics/lead flow

  Scenario: Invalid/oversized values ignored
    Given Malformed or oversized attribution parameters
    When Parameters are processed
    Then Invalid or oversized values are sanitized or ignored

  Scenario: Parameter content not executed
    Given Attribution parameters
    When Values are processed
    Then Parameter content is never executed as code

  Scenario: Consent denied handling
    Given Attribution parameters present but consent denied
    When Page loads
    Then Attribution is handled appropriately per consent

  Scenario: Full URLs not logged with sensitive query values
    Given URL logging implementation
    When Logs are reviewed
    Then Full URLs with potentially sensitive query values are not logged
