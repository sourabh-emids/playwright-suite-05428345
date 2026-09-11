Feature: TC-03 Primary call-to-action navigation
  Verify available primary homepage calls to action reach their intended pages.

  Scenario Outline: A primary call to action opens its intended page
    Given the TC-03 user is on the Emids homepage
    When the TC-03 user selects the "<cta_name>" primary call to action
    Then the TC-03 "<cta_name>" destination "<expected_path>" loads without an error

    Examples:
      | cta_name                    | expected_path                         |
      | Connect                     | /contact/                             |
      | See How We Deliver Outcomes | /forward-deployed-context-engineering/ |
