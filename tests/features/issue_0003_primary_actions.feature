Feature: Primary homepage actions

  Scenario Outline: Primary action opens its expected content
    Given the Emids homepage is open for primary actions
    When the user selects the "<action>" primary action
    Then the browser opens the action path "<path>"

    Examples:
      | action                      | path                                    |
      | Connect                     | /contact/                               |
      | See How We Deliver Outcomes | /forward-deployed-context-engineering/  |
      | All solutions               | /solutions/                             |
