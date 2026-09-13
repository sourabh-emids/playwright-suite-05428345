Feature: Medicare Advantage and other eBook/blog card displays

  Scenario: Medicare Advantage eBook card displays correctly
    Given Medicare Advantage eBook card renders
    When Page renders
    Then Card title reads 'Managing the Margin Reset in Medicare Advantage'

  Scenario: Medicare Advantage eBook type displayed
    Given Medicare Advantage eBook card renders
    When User views card
    Then Content type is displayed as eBook

  Scenario: Medicare Advantage Download action displayed
    Given Medicare Advantage eBook card renders
    When User views card action
    Then Download action is displayed

  Scenario: Medicare Advantage detail page URL correct
    Given User clicks Download
    When Navigation occurs
    Then User is navigated to '/insights/managing-the-margin-reset-in-medicare-advantage/'

  Scenario: Resource access handoff works
    Given User clicks Download on eBook card
    When Navigation occurs
    Then User reaches resource detail/access flow

  Scenario: No private asset endpoint exposed
    Given User inspects network traffic on eBook card click
    When Download is initiated
    Then Implementation does not expose private asset endpoints

  Scenario: Payer data readiness Blog type displayed
    Given User views Payer data readiness blog card
    When Page renders
    Then Content type is displayed as Blog

  Scenario: Payer data readiness Read More action displayed
    Given Payer data readiness blog card renders
    When User views card action
    Then Read More action is displayed (not Download)
