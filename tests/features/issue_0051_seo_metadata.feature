Feature: Implement SEO metadata and crawlable structure

  Scenario: Page has unique title
    Given User views page source or SEO tools
    When Checking title tag
    Then Unique <title> tag present describing page content

  Scenario: Meta description present and appropriate
    Given User checks meta description
    When Inspecting head content
    Then Meta description tag present with relevant summary

  Scenario: Canonical URL set
    Given User checks canonical tag
    When Inspecting head
    Then Canonical URL tag present pointing to canonical page URL

  Scenario: Primary text server-rendered for crawling
    Given Search engine crawler accesses page
    When Crawling page content
    Then Primary text content is in HTML, not JavaScript-dependent

  Scenario: Social preview metadata configured
    Given User checks Open Graph and Twitter Card tags
    When Inspecting head
    Then OG title, description, image and Twitter Card metadata present

  Scenario: Headings reflect page topic
    Given User analyzes heading structure
    When Checking H1 and subsequent headings
    Then Headings accurately describe page sections and topic

  Scenario: One canonical homepage URL
    Given Multiple URLs resolve to homepage
    When Checking canonical tags
    Then All variants point to single canonical URL

  Scenario: No duplicate conflicting title tags
    Given Code review
    when Checking head content
    Then Only one title tag present; no duplicates

  Scenario: OG image present for social sharing
    Given Social media preview test
    When Checking Open Graph image
    Then og:image tag present with valid image URL

  Scenario: Missing OG image handled
    Given OG image not configured
    When Page renders
    Then Fallback image used or social sharing uses default

  Scenario: Duplicate canonical detected
    Given Canonical misconfiguration
    When Checking canonical tags
    Then Single canonical per page; duplicates flagged in SEO audit

  Scenario: JS-only critical content avoided
    Given JavaScript required for critical content
    When Crawler without JS accesses page
    Then Critical content still renders server-side

  Scenario: Crawl 404 monitoring
    Given SEO monitoring tools
    When Checking crawl reports
    Then 404 errors captured and alerted; no PII in logs
