"""Feature file for Issue 0011 - Hero media loading optimization."""
Feature: Hero media loading optimization

  Scenario: Text content available when media fails
    Given The hero media fails to load
    When The page renders
    Then Text content remains available and readable

  Scenario: Media dimensions reserved to avoid layout shift
    Given A user loads the page
    When The page initially renders before media loads
    Then Image/video dimensions are reserved to avoid layout shift (CLS)

  Scenario: Appropriately sized assets served
    Given A user loads the page on a mobile device
    When Media assets are requested
    Then Appropriately sized assets (via srcset/sizes where applicable) are served

  Scenario: Hero LCP asset not lazy-loaded
    Given A user loads the page
    When The LCP (Largest Contentful Paint) asset loads
    Then The principal hero LCP asset is not lazy-loaded in a way that harms LCP score

  Scenario: Media poster/alt provided
    Given A user views the hero media
    When The media element is examined
    Then Poster and alt attributes are appropriately set

  Scenario: CDN timeout handling
    Given The CDN serving hero media times out
    When The page loads
    Then Text content remains available without blocking rendering
