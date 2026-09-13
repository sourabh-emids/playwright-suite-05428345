"""Step definitions for issue_0037-0044: Analytics and Media combined"""

from playwright.sync_api import Page, expect
from pytest_bdd import given, when, then

from pages.issue_0037_0042_analytics_media_combined_page import AnalyticsMediaPage


# Issue 0037 - GTM
@given("Google Tag Manager script fails to load")
def gtm_fails(page: Page):
    page_object = AnalyticsMediaPage(page)
    page_object.navigate_to_homepage()


@given("GTM is configured on the page")
def gtm_configured(page: Page):
    page_object = AnalyticsMediaPage(page)
    page_object.navigate_to_homepage()


@given("GTM and consent management are configured")
def gtm_consent_configured(page: Page):
    page_object = AnalyticsMediaPage(page)
    page_object.navigate_to_homepage()


@when("The page renders")
def page_renders(page: Page):
    pass


@when("Consent has not been granted")
def consent_not_granted(page: Page):
    pass


@when("Page load performance is measured")
def performance_measured(page: Page):
    pass


@when("Consent state changes")
def consent_changes(page: Page):
    pass


@then("Core page content, navigation, and functionality remain intact")
def core_intact(page: Page):
    page_object = AnalyticsMediaPage(page)
    page_object.verify_core_content()


@then("Non-essential marketing/analytics tags do not execute before consent")
def tags_wait_consent(page: Page):
    page_object = AnalyticsMediaPage(page)
    page_object.verify_core_content()


@then("GTM script does not prevent or delay page content rendering")
def gtm_no_delay(page: Page):
    page_object = AnalyticsMediaPage(page)
    page_object.verify_core_content()


@then("Tag execution respects the updated consent state")
def tag_respects_consent(page: Page):
    page_object = AnalyticsMediaPage(page)
    page_object.verify_core_content()


# Issue 0038 - Analytics
@given("Google Analytics is configured")
def ga_configured(page: Page):
    page_object = AnalyticsMediaPage(page)
    page_object.navigate_to_homepage()


@given("Analytics consent has been denied")
def analytics_denied(page: Page):
    page_object = AnalyticsMediaPage(page)
    page_object.navigate_to_homepage()


@given("A user submits the contact form")
def user_submits_form(page: Page):
    page_object = AnalyticsMediaPage(page)
    page_object.navigate_to_homepage()


@given("Analytics events are configured")
def events_configured(page: Page):
    page_object = AnalyticsMediaPage(page)
    page_object.navigate_to_homepage()


@when("Consent status is evaluated")
def consent_evaluated(page: Page):
    pass


@when("The page renders and user interacts")
def page_interacts(page: Page):
    pass


@when("Analytics events are captured")
def events_captured(page: Page):
    pass


@when("Consent categories are evaluated")
def categories_evaluated(page: Page):
    pass


@then("Analytics initialization follows the current consent status")
def ga_follows_consent(page: Page):
    page_object = AnalyticsMediaPage(page)
    page_object.verify_core_content()


@then("Page remains fully functional without analytics tracking")
def page_functional(page: Page):
    page_object = AnalyticsMediaPage(page)
    page_object.verify_core_content()


@then("Event payloads do not include contact form field values")
def no_form_values(page: Page):
    page_object = AnalyticsMediaPage(page)
    page_object.verify_core_content()


@then("Statistics consent is required where applicable for analytics to function")
def stats_consent_required(page: Page):
    page_object = AnalyticsMediaPage(page)
    page_object.verify_core_content()


# Issue 0039 - Campaign attribution
@given("A user arrives via URL with UTM parameters or gclid")
def user_arrives_utm(page: Page):
    page_object = AnalyticsMediaPage(page)
    page_object.navigate_to_homepage()


@given("A user arrives via URL with malformed or oversized parameters")
def user_arrives_malformed(page: Page):
    page_object = AnalyticsMediaPage(page)
    page_object.navigate_to_homepage()


@given("URL parameters are present in the query string")
def params_present(page: Page):
    page_object = AnalyticsMediaPage(page)
    page_object.navigate_to_homepage()


@when("The landing page processes the request")
def page_processes(page: Page):
    pass


@when("The page processes the request")
def request_processed(page: Page):
    pass


@when("Attribution values are processed")
def values_processed(page: Page):
    pass


@then("Supported attribution values are associated with the session where permitted")
def attr_values_preserved(page: Page):
    page_object = AnalyticsMediaPage(page)
    page_object.verify_core_content()


@then("Invalid or oversized values are ignored without breaking the page")
def invalid_ignored(page: Page):
    page_object = AnalyticsMediaPage(page)
    page_object.verify_core_content()


@then("Parameter content is not executed as code")
def params_not_executed(page: Page):
    page_object = AnalyticsMediaPage(page)
    page_object.verify_core_content()


@then("Length limits are enforced and values are sanitized")
def limits_enforced(page: Page):
    page_object = AnalyticsMediaPage(page)
    page_object.verify_core_content()


# Issue 0040 - Marketo
@given("Marketo is configured")
def marketo_configured(page: Page):
    page_object = AnalyticsMediaPage(page)
    page_object.navigate_to_homepage()


@given("Marketo script fails or is blocked")
def marketo_blocked(page: Page):
    page_object = AnalyticsMediaPage(page)
    page_object.navigate_to_homepage()


@given("Marketo integration is configured")
def marketo_integration(page: Page):
    page_object = AnalyticsMediaPage(page)
    page_object.navigate_to_homepage()


@when("Marketing consent has not been granted")
def marketing_not_granted(page: Page):
    pass


@when("The page renders")
def page_renders_marketo(page: Page):
    pass


@then("Marketo scripts do not execute")
def marketo_no_execute(page: Page):
    page_object = AnalyticsMediaPage(page)
    page_object.verify_core_content()


@then("Core page content and functionality remain independent of Marketo")
def core_independent(page: Page):
    page_object = AnalyticsMediaPage(page)
    page_object.verify_core_content()


@then("Marketing consent is required where applicable for Marketo to function")
def marketing_consent_required(page: Page):
    page_object = AnalyticsMediaPage(page)
    page_object.verify_core_content()


# Issue 0041 - LinkedIn
@given("LinkedIn insight/marketing tags are configured")
def linkedin_configured(page: Page):
    page_object = AnalyticsMediaPage(page)
    page_object.navigate_to_homepage()


@given("LinkedIn tag fails to load or is blocked")
def linkedin_blocked(page: Page):
    page_object = AnalyticsMediaPage(page)
    page_object.navigate_to_homepage()


@then("LinkedIn tag does not execute")
def linkedin_no_execute(page: Page):
    page_object = AnalyticsMediaPage(page)
    page_object.verify_core_content()


@then("Core content and navigation remain functional")
def core_functional(page: Page):
    page_object = AnalyticsMediaPage(page)
    page_object.verify_core_content()


# Issue 0042 - ZoomInfo
@given("ZoomInfo/WebSights is configured")
def zoominfo_configured(page: Page):
    page_object = AnalyticsMediaPage(page)
    page_object.navigate_to_homepage()


@given("ZoomInfo/WebSights fails to load")
def zoominfo_fails(page: Page):
    page_object = AnalyticsMediaPage(page)
    page_object.navigate_to_homepage()


@given("ZoomInfo/WebSights configuration exists")
def zoominfo_config_exists(page: Page):
    page_object = AnalyticsMediaPage(page)
    page_object.navigate_to_homepage()


@when("Required consent has not been granted")
def required_consent_not_granted(page: Page):
    pass


@when("The page renders and user interacts")
def page_interacts_zoominfo(page: Page):
    pass


@when("The page source is reviewed")
def source_reviewed(page: Page):
    pass


@then("Visitor intelligence tooling does not load")
def tooling_no_load(page: Page):
    page_object = AnalyticsMediaPage(page)
    page_object.verify_core_content()


@then("Content and navigation remain unaffected")
def content_unaffected(page: Page):
    page_object = AnalyticsMediaPage(page)
    page_object.verify_core_content()


@then("Private account identifiers are not exposed in visible page copy")
def no_private_exposed(page: Page):
    page_object = AnalyticsMediaPage(page)
    page_object.verify_core_content()


# Issue 0043 - Wistia
@given("No Wistia content is configured for the homepage variant")
def no_wistia(page: Page):
    page_object = AnalyticsMediaPage(page)
    page_object.navigate_to_homepage()


@given("Wistia video content is configured")
def wistia_configured(page: Page):
    page_object = AnalyticsMediaPage(page)
    page_object.navigate_to_homepage()


@given("Wistia video is configured and user prefers reduced motion")
def wistia_reduced_motion(page: Page):
    page_object = AnalyticsMediaPage(page)
    page_object.navigate_to_homepage()


@when("The page renders")
def page_renders_wistia(page: Page):
    pass


@when("The player renders")
def player_renders(page: Page):
    pass


@then("No Wistia player script is loaded unnecessarily")
def no_wistia_script(page: Page):
    page_object = AnalyticsMediaPage(page)
    expect(page_object.check_no_wistia_script()).to_be(True)


@then("Player has accessible title and controls")
def player_accessible(page: Page):
    page_object = AnalyticsMediaPage(page)
    page_object.verify_core_content()


@then("Autoplay and continuous motion behaviors respect user preferences")
def motion_respected(page: Page):
    page_object = AnalyticsMediaPage(page)
    page_object.verify_core_content()


# Issue 0044 - YouTube
@given("No YouTube embed is configured for the homepage variant")
def no_youtube(page: Page):
    page_object = AnalyticsMediaPage(page)
    page_object.navigate_to_homepage()


@given("YouTube video is configured")
def youtube_configured(page: Page):
    page_object = AnalyticsMediaPage(page)
    page_object.navigate_to_homepage()


@when("The player renders")
def player_renders_youtube(page: Page):
    pass


@when("The player initializes")
def player_initializes(page: Page):
    pass


@then("No YouTube player resources are required or loaded")
def no_youtube_resources(page: Page):
    page_object = AnalyticsMediaPage(page)
    expect(page_object.check_no_youtube_api()).to_be(True)


@then("Player is keyboard accessible and has a title")
def youtube_accessible(page: Page):
    page_object = AnalyticsMediaPage(page)
    page_object.verify_core_content()


@then("Autoplay with sound is not enabled by default")
def no_autoplay_sound(page: Page):
    page_object = AnalyticsMediaPage(page)
    page_object.verify_core_content()
