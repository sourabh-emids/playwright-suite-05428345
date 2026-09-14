Feature: Optimize hero media loading

  Scenario: Text content available if media fails
    Given Hero media fails to load
    When Page renders
    Then Text content remains visible and readable; layout is not broken

  Scenario: Media dimensions reserved to avoid layout shift
    Given Hero contains image or video
    When Before media loads
    Then Placeholder space is reserved using width/height attributes or aspect-ratio CSS

  Scenario: Appropriately sized assets served
    Given User views hero on different viewport sizes
    When Media assets are requested
    Then Responsive images use srcset/sizes or responsive video containers

  Scenario: LCP asset not lazy-loaded harmfully
    Given Hero media is the LCP element
    When Page loads
    Then Hero media loads eagerly; no lazy loading that would harm LCP score

  Scenario: Media loads progressively without moving text
    Given Hero media is loading
    When Monitoring layout stability
    Then Primary text does not shift position as media loads

  Scenario: CDN timeout handled gracefully
    Given Media CDN is slow or times out
    When Page attempts to load media
    Then Text content remains accessible; error is logged

  Scenario: Unsupported media format handled
    Given Media format is not supported by browser
    When Browser attempts to render
    Then Fallback or error state displays; page remains functional

  Scenario: Low-bandwidth media loading
    Given User is on slow network connection
    When Page loads
    Then Text renders first; media loads progressively or shows low-quality fallback
