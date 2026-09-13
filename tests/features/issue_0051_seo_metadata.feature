Feature: SEO metadata and crawlable structure

  Scenario: Page has unique title
    Given User views page source
    When Page loads
    Then Page has a unique title element

  Scenario: Page has meta description
    Given User views page source
    When Page loads
    Then Page has meta description element

  Scenario: Canonical URL set
    Given User views page source
    When Page loads
    Then Canonical URL is set to the primary page URL

  Scenario: Primary text server-rendered
    Given User or crawler views page
    When Page loads without JavaScript
    Then Primary text content is server-rendered and crawlable

  Scenario: Social preview metadata configured
    Given User views page source
    When Page loads
    Then Open Graph and Twitter Card metadata is configured

  Scenario: Headings reflect page topic
    Given User views page headings
    When Page loads
    Then H1 reflects page topic and matches title

  Scenario: One canonical homepage URL
    Given User views page source
    When Canonical URLs are compared
    Then Only one canonical homepage URL exists

  Scenario: No duplicate conflicting titles
    Given User views page source
    When Title tags are compared
    Then No duplicate or conflicting title tags exist

  Scenario: Missing social image handling
    Given OG image is missing
    When Social share occurs
    Then Fallback image or appropriate default displays

  Scenario: JS-only content prevention
    Given Critical content is managed
    When Page renders
    Then Critical content is not JavaScript-only
