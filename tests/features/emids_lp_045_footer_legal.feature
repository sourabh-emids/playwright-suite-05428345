Feature: Render footer legal navigation

  Scenario: Verify each legal link has descriptive text
    Given Footer legal navigation renders
    When User views legal links
    Then Each link displays descriptive text (e.g., 'Privacy Policy', 'Cookie Policy', 'Accessibility Statement')

  Scenario: Verify legal links have valid destinations
    Given Footer legal links render
    When User clicks each link
    Then All legal links navigate to valid published pages

  Scenario: Verify visible focus state on legal links
    Given User tabs to legal navigation links
    When Links receive focus
    Then Visible focus indicator is displayed

  Scenario: Verify all URLs HTTPS
    Given Legal links are configured
    When User inspects link URLs
    Then All legal page URLs use HTTPS protocol

  Scenario: Verify labels not blank
    Given Legal navigation renders
    When User views link labels
    Then No link label is blank or empty

  Scenario: Verify responsive multi-column layout
    Given Footer renders at mobile width
    When User views legal navigation
    Then Legal links reflow appropriately without horizontal overflow

  Scenario: Verify legal page moved handled
    Given Legal page URL has changed
    When User clicks link
    Then Redirect occurs or appropriate error displayed

  Scenario: Verify long labels handled
    Given Legal link has very long label
    When Footer renders
    Then Label wraps gracefully without breaking layout
