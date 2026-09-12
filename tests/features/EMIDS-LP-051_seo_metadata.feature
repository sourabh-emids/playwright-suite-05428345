Feature: SEO metadata and crawlable structure

  Scenario: Unique page title
    Given Homepage document head
    When Title tag is verified
    Then Page has unique title

  Scenario: Meta description present
    Given Homepage metadata
    When Meta description is verified
    Then Meta description is present and descriptive

  Scenario: Canonical URL set
    Given Homepage canonical link
    When Canonical is verified
    Then Canonical URL points to primary homepage URL

  Scenario: Primary text server-rendered
    Given Critical page content
    When Page source is analyzed
    Then Primary text is server-rendered and crawlable

  Scenario: Social preview metadata configured
    Given Open Graph and Twitter metadata
    When Social sharing is tested
    Then Social preview metadata is configured

  Scenario: Headings reflect page topic
    Given Page heading structure
    When Headings are reviewed
    Then Headings reflect the page topic for search engines

  Scenario: No duplicate conflicting title tags
    Given Page title tags
    When Title tags are audited
    Then No duplicate or conflicting title tags exist
