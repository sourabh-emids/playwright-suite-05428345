@TC-03
Feature: Emids homepage primary calls to action
  As a website visitor
  I want primary calls to action to open their assigned destinations
  So that I can continue to relevant content

  Scenario Outline: Primary call-to-action opens its expected destination
    Given the Emids homepage primary calls to action are available
    When I select the "<call_to_action>" primary call to action
    Then its assigned destination "<path>" loads without a visible error

    Examples:
      | call_to_action                 | path                                    |
      | See How We Deliver Outcomes    | /forward-deployed-context-engineering/  |
      | See the model                  | /forward-deployed-context-engineering/  |
      | All solutions                  | /solutions/                             |
      | Explore Payer                  | /segments/payer/                        |
      | Connect                        | /contact/                               |
