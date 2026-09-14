Feature: Integrate LinkedIn tags conditionally

  Scenario: LinkedIn tag does not execute before marketing consent
    Given User has not granted marketing consent
    When Page loads
    Then LinkedIn insight tag does not execute

  Scenario: Core page independent of LinkedIn tag
    Given LinkedIn tag fails to load
    When Page renders
    Then Core content and navigation remain fully functional

  Scenario: Marketing consent required
    Given Consent state check
    When LinkedIn tag attempts to load
    Then Tag loads only after marketing consent granted

  Scenario: Ad blocker blocking LinkedIn handled
    Given Ad blocker prevents LinkedIn tag
    When Page renders
    Then Core page unaffected; tag blocked gracefully

  Scenario: Vendor timeout handled
    Given LinkedIn service slow or timeout
    When Page renders
    Then Core functionality unaffected; timeout logged minimally

  Scenario: Consent denied handled
    Given User denies marketing consent
    When LinkedIn tag attempts execution
    Then Tag does not execute; page functions normally
