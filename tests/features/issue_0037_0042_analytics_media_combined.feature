Feature: Google Tag Manager with consent governance
  # issue_0037

  Scenario: Core page works if GTM fails
    Given Google Tag Manager script fails to load
    When The page renders
    Then Core page content, navigation, and functionality remain intact

  Scenario: Non-essential tags do not run before required consent
    Given GTM is configured on the page
    When Consent has not been granted
    Then Non-essential marketing/analytics tags do not execute before consent

  Scenario: GTM does not block page rendering
    Given GTM is configured on the page
    When Page load performance is measured
    Then GTM script does not prevent or delay page content rendering

  Scenario: Analytics integration respects consent mode
    Given GTM and consent management are configured
    When Consent state changes
    Then Tag execution respects the updated consent state

---
Feature: Google Analytics with consent
  # issue_0038

  Scenario: Analytics initializes following consent
    Given Google Analytics is configured
    When Consent status is evaluated
    Then Analytics initialization follows the current consent status

  Scenario: Denial leaves page unaffected
    Given Analytics consent has been denied
    When The page renders and user interacts
    Then Page remains fully functional without analytics tracking

  Scenario: Events do not contain contact form field values
    Given A user submits the contact form
    When Analytics events are captured
    Then Event payloads do not include contact form field values

  Scenario: Statistics consent required for analytics
    Given Analytics events are configured
    When Consent categories are evaluated
    Then Statistics consent is required where applicable for analytics to function

---
Feature: Campaign attribution parameters safe handling
  # issue_0039

  Scenario: Supported attribution values preserved where permitted
    Given A user arrives via URL with UTM parameters or gclid
    When The landing page processes the request
    Then Supported attribution values (utm_source, utm_medium, utm_campaign, utm_content, utm_term, gclid, referrer) are associated with the session where permitted

  Scenario: Invalid values are ignored
    Given A user arrives via URL with malformed or oversized parameters
    When The page processes the request
    Then Invalid or oversized values are ignored without breaking the page

  Scenario: Parameter content never executed
    Given URL parameters are present in the query string
    When The page processes the request
    Then Parameter content is not executed as code

  Scenario: Length limits applied and values sanitized
    Given URL parameters are present
    When Attribution values are processed
    Then Length limits are enforced and values are sanitized

---
Feature: Marketo integration with consent
  # issue_0040

  Scenario: Marketing scripts gated by consent
    Given Marketo is configured
    When Marketing consent has not been granted
    Then Marketo scripts do not execute

  Scenario: Page functional when Marketo unavailable
    Given Marketo script fails or is blocked
    When The page renders
    Then Core page content and functionality remain independent of Marketo

  Scenario: Marketing consent required for Marketo
    Given Marketo integration is configured
    When Consent categories are evaluated
    Then Marketing consent is required where applicable for Marketo to function

---
Feature: LinkedIn marketing tags conditional
  # issue_0041

  Scenario: LinkedIn tag requires marketing consent
    Given LinkedIn insight/marketing tags are configured
    When Marketing consent has not been granted
    Then LinkedIn tag does not execute

  Scenario: Core page independent of LinkedIn tag
    Given LinkedIn tag fails to load or is blocked
    When The page renders
    Then Core content and navigation remain functional

---
Feature: ZoomInfo WebSights conditional
  # issue_0042

  Scenario: Visitor intelligence tooling loads conditionally
    Given ZoomInfo/WebSights is configured
    When Required consent has not been granted
    Then Visitor intelligence tooling does not load

  Scenario: Tooling failure does not affect content
    Given ZoomInfo/WebSights fails to load
    When The page renders and user interacts
    Then Content and navigation remain unaffected

  Scenario: Private identifiers not exposed in page copy
    Given ZoomInfo/WebSights configuration exists
    When The page source is reviewed
    Then Private account identifiers are not exposed in visible page copy

---
Feature: Wistia embeds conditional
  # issue_0043

  Scenario: No Wistia script when not configured
    Given No Wistia content is configured for the homepage variant
    When The page renders
    Then No Wistia player script is loaded unnecessarily

  Scenario: Wistia player accessible when configured
    Given Wistia video content is configured
    When The player renders
    Then Player has accessible title and controls

  Scenario: Wistia respects reduced motion and consent
    Given Wistia video is configured and user prefers reduced motion
    When The player renders
    Then Autoplay and continuous motion behaviors respect user preferences

---
Feature: YouTube embeds conditional
  # issue_0044

  Scenario: No YouTube resources when not configured
    Given No YouTube embed is configured for the homepage variant
    When The page renders
    Then No YouTube player resources are required or loaded

  Scenario: YouTube player accessible when configured
    Given YouTube video is configured
    When The player renders
    Then Player is keyboard accessible and has a title

  Scenario: No autoplay with sound by default
    Given YouTube video is configured
    When The player initializes
    Then Autoplay with sound is not enabled by default
