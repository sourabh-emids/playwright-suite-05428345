Feature: Hero media loading optimization

  Scenario: Text content available if media fails
    Given Hero media fails to load
    When Page renders
    Then Text content remains available and readable

  Scenario: Media dimensions reserved to avoid layout shift
    Given Hero media is configured
    When Page loads before media downloads
    Then Layout shift is prevented with reserved dimensions

  Scenario: Appropriately sized assets served
    Given User views Emids homepage
    When Media assets are requested
    Then Assets are served at appropriate sizes for viewport (srcset/sizes attributes present)

  Scenario: LCP asset not lazy-loaded
    Given Hero contains LCP asset
    When Performance is measured
    Then Principal LCP asset is not lazy-loaded

  Scenario: CDN timeout handling
    Given Media is hosted on CDN
    When CDN times out
    Then Text content remains accessible

  Scenario: Unsupported format handling
    Given Media uses unsupported format
    When Browser attempts to render
    Then Fallback or alternative is provided

  Scenario: Low-bandwidth connection handling
    Given User is on low-bandwidth connection
    When Page loads
    Then Media loads progressively without blocking text content
