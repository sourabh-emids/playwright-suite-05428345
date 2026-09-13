Feature: Implement SEO metadata and crawlable structure

  Scenario: Verify page has unique title
    Given Homepage renders
    When User or crawler inspects document title
    Then Page has a unique, descriptive title tag

  Scenario: Verify page has meta description
    Given Homepage renders
    When User or crawler inspects meta description
    Then Page has a unique meta description tag

  Scenario: Verify canonical URL set
    Given Homepage renders
    When User or crawler inspects canonical link
    Then Canonical URL is set to the primary homepage URL

  Scenario: Verify primary text is server-rendered
    Given Page loads with JavaScript
    When Crawler without JS support accesses page
    Then Primary text content is present in initial HTML response

  Scenario: Verify social preview metadata configured
    Given Homepage renders
    When User or tool inspects Open Graph and Twitter metadata
    Then Social preview metadata (og:image, og:title, og:description) is configured

  Scenario: Verify headings reflect page topic
    Given Page headings render
    When Crawler or user scans headings
    Then H1 and prominent headings reflect the homepage topic

  Scenario: Verify no duplicate conflicting titles
    Given Page renders
    When User inspects title elements
    Then No duplicate or conflicting title tags exist

  Scenario: Verify missing og:image handled
    Given Social metadata is configured but og:image is missing
    When Social platform scrapes page
    Then Fallback or graceful degradation; no broken image reference

  Scenario: Verify JS-only critical content avoided
    Given Critical content should not require JavaScript
    When Page renders without JS
    Then Primary content and navigation remain accessible
