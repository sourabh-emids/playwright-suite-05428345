"""Feature file for Issue 0051 - SEO metadata and crawlable structure."""
Feature: SEO metadata and crawlable structure

  Scenario: Page has unique title
    Given A search engine or user examines the page
    When Page title is retrieved
    Then Title is unique to this page and descriptive

  Scenario: Page has meta description
    Given A search engine retrieves meta description
    When Metadata is analyzed
    Then Meta description is present and relevant to page content

  Scenario: Canonical URL is set
    Given A search engine or user examines canonical tag
    When Canonical URL is retrieved
    Then Canonical URL is set to the primary homepage URL

  Scenario: Primary text server-rendered and crawlable
    Given A search engine crawler indexes the page
    When Page content is fetched
    Then Primary text is server-rendered and crawlable

  Scenario: Social preview metadata configured
    Given A user or crawler examines Open Graph/Twitter metadata
    When Social sharing tags are checked
    Then Social preview metadata is configured (ogImage, og:title, og:description)

  Scenario: Headings reflect page topic
    Given A search engine analyzes heading structure
    When Headings are examined
    Then Headings accurately reflect the page topic

  Scenario: No duplicate canonical conflicts
    Given A crawler examines the page
    When Canonical tags are found
    Then No conflicting duplicate canonical tags exist

  Scenario: Missing og:image handling
    Given Social image is not configured
    When Page is shared on social media
    Then Fallback image or graceful degradation occurs
