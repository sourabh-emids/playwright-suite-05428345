@issue_0003
Feature: Primary call-to-action destinations

  Scenario Outline: A primary call to action opens its expected destination
    Given the homepage primary calls to action are available
    When the user selects the "<call_to_action>" call to action
    Then the call-to-action path is "<path>" with heading "<heading>"

    Examples:
      | call_to_action              | path                                    | heading                              |
      | See How We Deliver Outcomes | /forward-deployed-context-engineering/ | Forward Deployed Context Engineering |
      | All solutions               | /solutions/                             | Solutions                            |
      | Connect                     | /contact/                               | Let's Connect                        |
