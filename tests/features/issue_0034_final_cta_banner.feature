Feature: Render final conversion banner

  Scenario: Banner appears before footer
    Given User views page structure
    When Checking section order
    Then Final CTA banner appears before footer section

  Scenario: Primary action is clear and keyboard operable
    Given User focuses on banner CTA
    When Pressing Tab to navigate
    Then CTA is keyboard accessible with visible focus

  Scenario: Supporting timing message readable
    Given User views banner content
    When Reading timing/message text
    Then Supporting timing/value text is legible

  Scenario: Required message and CTA fields present
    Given Content validation
    When Checking required fields
    Then Banner has non-empty title, body text, and CTA

  Scenario: High contrast closing CTA section
    Given User tests contrast ratios
    When Checking accessibility
    Then Banner meets contrast requirements for text readability

  Scenario: CTA routes to contact page
    Given User clicks final CTA
    When Navigation occurs
    Then User navigates to /contact/

  Scenario: CTA text wraps gracefully
    Given Narrow viewport with long CTA text
    When Page renders
    Then CTA text wraps without overlapping or breaking

  Scenario: Footer overlap prevented
    Given Viewport height is limited
    When Page renders
    Then CTA section does not overlap footer content

  Scenario: Contact route unavailable handled
    Given Contact page returns error
    When User clicks CTA
    Then Error handling occurs appropriately
