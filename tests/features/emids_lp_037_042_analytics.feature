"""Feature: Analytics and marketing integration (emids_lp_037-042)."""
Feature: Analytics and marketing integration

    @emids_lp_037 @analytics
    Scenario: Core page works if GTM fails
        Given GTM fails to load
        When Page renders
        Then Core page content renders
        And Site remains functional

    @emids_lp_037 @analytics
    Scenario: Non-essential tags blocked before consent
        Given User has not provided analytics consent
        When GTM container loads
        Then Non-essential tags do not execute before required consent

    @emids_lp_037 @analytics @performance
    Scenario: GTM does not block rendering
        Given GTM script loads
        When Page performance is measured
        Then Page render is not blocked by GTM
        And Scripts are non-blocking

    @emids_lp_038 @analytics
    Scenario: Analytics initialization follows consent
        Given User provides analytics consent
        When Analytics initializes
        Then GA tracking begins after valid consent obtained

    @emids_lp_038 @analytics
    Scenario: Denial leaves page functional
        Given User denies analytics consent
        When Page renders and user interacts
        Then Page remains fully functional
        And No degraded experience

    @emids_lp_038 @analytics
    Scenario: Events do not contain contact form values
        Given User submits contact form
        When Analytics event fires
        Then Event payload does not contain form field values
        And No PII logged

    @emids_lp_039 @analytics
    Scenario: Supported attribution values preserved when permitted
        Given User arrives via UTM parameters
        When Page renders
        Then UTM values (source, medium, campaign, content, term) are captured

    @emids_lp_039 @analytics @security
    Scenario: Invalid values ignored
        Given URL contains malformed UTM parameters
        When Page processes attribution
        Then Invalid values are ignored
        And No execution of parameter content

    @emids_lp_039 @analytics @security
    Scenario: Parameter content not executed
        Given URL contains potentially malicious parameter
        When Page processes parameters
        Then Parameter values are sanitized
        And No XSS or execution

    @emids_lp_040 @analytics @marketing
    Scenario: Marketing scripts gated by consent
        Given User has not provided marketing consent
        When Marketo scripts load
        Then Marketing scripts do not execute
        And Page functions normally

    @emids_lp_040 @analytics @marketing
    Scenario: Page functional when Marketo unavailable
        Given Marketo fails or is blocked
        When Page loads
        Then Core page remains functional
        And No dependency on Marketo for content

    @emids_lp_041 @analytics @marketing
    Scenario: LinkedIn tag blocked before marketing consent
        Given User has not provided marketing consent
        When LinkedIn tag loads
        Then Tag does not execute
        And Page functions normally

    @emids_lp_041 @analytics @marketing
    Scenario: Core page independent of LinkedIn tag
        Given LinkedIn tag fails or unavailable
        When Page renders
        Then Core content and functionality remain intact

    @emids_lp_042 @analytics
    Scenario: Tooling loads conditionally
        Given ZoomInfo/WebSights enabled and permitted by consent
        When Page loads
        Then Tooling loads and functions
        And No impact on content

    @emids_lp_042 @analytics
    Scenario: Failure does not affect content or navigation
        Given ZoomInfo/WebSights fails
        When Page renders
        Then Content and navigation remain functional
        And Graceful degradation
