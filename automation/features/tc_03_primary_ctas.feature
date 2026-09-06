@tc_03
Feature: TC-03 Primary call-to-action navigation

  Scenario Outline: Primary calls to action open their expected destinations
    Given the Emids homepage is displayed
    When the user selects the primary "<action>" call to action
    Then "<path>" is displayed with the heading "<heading>"

    Examples:
      | action                      | path                                    | heading                              |
      | Connect                     | /contact/                               | Let's Connect                        |
      | See How We Deliver Outcomes | /forward-deployed-context-engineering/  | Forward Deployed Context Engineering |
