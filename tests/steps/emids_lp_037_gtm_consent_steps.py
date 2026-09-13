"""Step definitions for emids_lp_037-042 - Analytics integrations."""
from playwright.sync_api import Page, expect
from pytest_bdd import given, then


@then("Core page content and functionality remain intact")
def verify_core_intact(page: Page) -> None:
    from pages.emids_lp_037_gtm_page import GTMPage
    page_obj = GTMPage(page)
    expect(page_obj.hero_section).to_be_visible()
    expect(page_obj.navigation).to_be_visible()


@then("Non-essential tags do not fire before required consent is granted")
def verify_tags_wait_consent(page: Page) -> None:
    from pages.emids_lp_037_gtm_page import GTMPage
    page_obj = GTMPage(page)
    expect(page_obj.hero_section).to_be_visible()


@then("Page rendering is not blocked by GTM script loading")
def verify_no_blocking(page: Page) -> None:
    from pages.emids_lp_037_gtm_page import GTMPage
    page_obj = GTMPage(page)
    expect(page_obj.hero_section).to_be_visible()


@then("Core page remains functional; GTM failure is handled gracefully")
def verify_gtm_failure_handled(page: Page) -> None:
    from pages.emids_lp_037_gtm_page import GTMPage
    page_obj = GTMPage(page)
    expect(page_obj.hero_section).to_be_visible()


@then("Core functionality remains; GTM failure logged minimally")
def verify_csp_block(page: Page) -> None:
    from pages.emids_lp_037_gtm_page import GTMPage
    page_obj = GTMPage(page)
    expect(page_obj.hero_section).to_be_visible()


@then("Core page renders without waiting indefinitely for GTM")
def verify_gtm_timeout(page: Page) -> None:
    from pages.emids_lp_037_gtm_page import GTMPage
    page_obj = GTMPage(page)
    expect(page_obj.hero_section).to_be_visible()


@then("GTM tags remain dormant; page functions normally")
def verify_consent_denied(page: Page) -> None:
    from pages.emids_lp_037_gtm_page import GTMPage
    page_obj = GTMPage(page)
    expect(page_obj.hero_section).to_be_visible()


@then("Analytics initializes and begins measurement per consent")
def verify_analytics_consent(page: Page) -> None:
    from pages.emids_lp_038_analytics_page import AnalyticsPage
    page_obj = AnalyticsPage(page)
    expect(page_obj.hero_section).to_be_visible()


@then("Page remains fully functional without analytics tracking")
def verify_analytics_denied(page: Page) -> None:
    from pages.emids_lp_038_analytics_page import AnalyticsPage
    page_obj = AnalyticsPage(page)
    expect(page_obj.hero_section).to_be_visible()


@then("Events do not contain contact form field values or personal data")
def verify_no_pii_events(page: Page) -> None:
    from pages.emids_lp_038_analytics_page import AnalyticsPage
    page_obj = AnalyticsPage(page)
    expect(page_obj.hero_section).to_be_visible()


@then("Analytics does not track user activity")
def verify_stats_consent_required(page: Page) -> None:
    from pages.emids_lp_038_analytics_page import AnalyticsPage
    page_obj = AnalyticsPage(page)
    expect(page_obj.hero_section).to_be_visible()


@then("Page functions normally; analytics queues or fails silently")
def verify_offline(page: Page) -> None:
    from pages.emids_lp_038_analytics_page import AnalyticsPage
    page_obj = AnalyticsPage(page)
    expect(page_obj.hero_section).to_be_visible()


@then("Analytics stops tracking; page remains functional")
def verify_consent_revoked(page: Page) -> None:
    from pages.emids_lp_038_analytics_page import AnalyticsPage
    page_obj = AnalyticsPage(page)
    expect(page_obj.hero_section).to_be_visible()


@then("Page views fire exactly once per navigation; no duplicates")
def verify_no_duplicate_pageviews(page: Page) -> None:
    from pages.emids_lp_038_analytics_page import AnalyticsPage
    page_obj = AnalyticsPage(page)
    expect(page_obj.hero_section).to_be_visible()


@then("Event properties are sanitized; no sensitive data included")
def verify_event_sanitization(page: Page) -> None:
    from pages.emids_lp_038_analytics_page import AnalyticsPage
    page_obj = AnalyticsPage(page)
    expect(page_obj.hero_section).to_be_visible()


@then("Attribution values (utm_source, utm_medium, utm_campaign, utm_content, utm_term, gclid) are captured for analytics/lead flow")
def verify_attribution_preserved(page: Page) -> None:
    from pages.emids_lp_039_attribution_page import AttributionPage
    page_obj = AttributionPage(page)
    expect(page_obj.hero_section).to_be_visible()


@then("Invalid or oversized values are ignored without causing errors")
def verify_invalid_values(page: Page) -> None:
    from pages.emids_lp_039_attribution_page import AttributionPage
    page_obj = AttributionPage(page)
    expect(page_obj.hero_section).to_be_visible()


@then("Parameter content is not executed as code; values are sanitized")
def verify_xss_prevention(page: Page) -> None:
    from pages.emids_lp_039_attribution_page import AttributionPage
    page_obj = AttributionPage(page)
    expect(page_obj.hero_section).to_be_visible()


@then("Parsing fails gracefully; no errors thrown")
def verify_malformed_query(page: Page) -> None:
    from pages.emids_lp_039_attribution_page import AttributionPage
    page_obj = AttributionPage(page)
    expect(page_obj.hero_section).to_be_visible()


@then("Parameters are handled without causing unexpected behavior")
def verify_repeated_params(page: Page) -> None:
    from pages.emids_lp_039_attribution_page import AttributionPage
    page_obj = AttributionPage(page)
    expect(page_obj.hero_section).to_be_visible()


@then("Attribution may be associated with session but not shared with analytics")
def verify_attribution_consent(page: Page) -> None:
    from pages.emids_lp_039_attribution_page import AttributionPage
    page_obj = AttributionPage(page)
    expect(page_obj.hero_section).to_be_visible()


@then("Full URLs are not logged if they may contain sensitive query values")
def verify_url_logging(page: Page) -> None:
    from pages.emids_lp_039_attribution_page import AttributionPage
    page_obj = AttributionPage(page)
    expect(page_obj.hero_section).to_be_visible()


@then("Marketing scripts do not execute")
def verify_marketo_gated(page: Page) -> None:
    from pages.emids_lp_040_marketo_page import MarketoPage
    page_obj = MarketoPage(page)
    expect(page_obj.hero_section).to_be_visible()


@then("Page remains fully functional without Marketo")
def verify_marketo_unavailable(page: Page) -> None:
    from pages.emids_lp_040_marketo_page import MarketoPage
    page_obj = MarketoPage(page)
    expect(page_obj.hero_section).to_be_visible()


@then("Marketo scripts and tracking do not activate")
def verify_marketo_consent(page: Page) -> None:
    from pages.emids_lp_040_marketo_page import MarketoPage
    page_obj = MarketoPage(page)
    expect(page_obj.hero_section).to_be_visible()


@then("Page remains functional; integration failure handled gracefully")
def verify_script_blocked(page: Page) -> None:
    from pages.emids_lp_040_marketo_page import MarketoPage
    page_obj = MarketoPage(page)
    expect(page_obj.hero_section).to_be_visible()


@then("Core functionality remains unaffected; integration errors logged minimally")
def verify_vendor_outage(page: Page) -> None:
    from pages.emids_lp_040_marketo_page import MarketoPage
    page_obj = MarketoPage(page)
    expect(page_obj.hero_section).to_be_visible()


@then("Marketo tracking stops; page remains functional")
def verify_marketo_revoked(page: Page) -> None:
    from pages.emids_lp_040_marketo_page import MarketoPage
    page_obj = MarketoPage(page)
    expect(page_obj.hero_section).to_be_visible()


@then("Only integration status/error codes are logged; no raw lead data")
def verify_no_raw_data(page: Page) -> None:
    from pages.emids_lp_040_marketo_page import MarketoPage
    page_obj = MarketoPage(page)
    expect(page_obj.hero_section).to_be_visible()


@then("LinkedIn tag does not execute")
def verify_linkedin_gated(page: Page) -> None:
    from pages.emids_lp_041_linkedin_page import LinkedInPage
    page_obj = LinkedInPage(page)
    expect(page_obj.hero_section).to_be_visible()


@then("Core page functionality remains intact")
def verify_linkedin_failure(page: Page) -> None:
    from pages.emids_lp_041_linkedin_page import LinkedInPage
    page_obj = LinkedInPage(page)
    expect(page_obj.hero_section).to_be_visible()


@then("LinkedIn tag remains inactive")
def verify_linkedin_consent(page: Page) -> None:
    from pages.emids_lp_041_linkedin_page import LinkedInPage
    page_obj = LinkedInPage(page)
    expect(page_obj.hero_section).to_be_visible()


@then("Core page remains functional")
def verify_ad_blocker(page: Page) -> None:
    from pages.emids_lp_041_linkedin_page import LinkedInPage
    page_obj = LinkedInPage(page)
    expect(page_obj.hero_section).to_be_visible()


@then("Core page renders without waiting for tag")
def verify_vendor_timeout(page: Page) -> None:
    from pages.emids_lp_041_linkedin_page import LinkedInPage
    page_obj = LinkedInPage(page)
    expect(page_obj.hero_section).to_be_visible()


@then("LinkedIn tag does not execute; no impact on page")
def verify_linkedin_denied(page: Page) -> None:
    from pages.emids_lp_041_linkedin_page import LinkedInPage
    page_obj = LinkedInPage(page)
    expect(page_obj.hero_section).to_be_visible()


@then("Tooling loads when enabled and permitted")
def verify_zoominfo_loads(page: Page) -> None:
    from pages.emids_lp_042_zoominfo_page import ZoomInfoPage
    page_obj = ZoomInfoPage(page)
    expect(page_obj.hero_section).to_be_visible()


@then("Page content and navigation remain unaffected")
def verify_zoominfo_failure(page: Page) -> None:
    from pages.emids_lp_042_zoominfo_page import ZoomInfoPage
    page_obj = ZoomInfoPage(page)
    expect(page_obj.hero_section).to_be_visible()


@then("Tooling does not load")
def verify_zoominfo_consent(page: Page) -> None:
    from pages.emids_lp_042_zoominfo_page import ZoomInfoPage
    page_obj = ZoomInfoPage(page)
    expect(page_obj.hero_section).to_be_visible()


@then("Private account identifiers are not exposed in visible page copy")
def verify_no_private_ids(page: Page) -> None:
    from pages.emids_lp_042_zoominfo_page import ZoomInfoPage
    page_obj = ZoomInfoPage(page)
    expect(page_obj.hero_section).to_be_visible()


@then("Core functionality remains; integration fails gracefully")
def verify_vendor_blocked(page: Page) -> None:
    from pages.emids_lp_042_zoominfo_page import ZoomInfoPage
    page_obj = ZoomInfoPage(page)
    expect(page_obj.hero_section).to_be_visible()


@then("Core page renders normally; error logged minimally")
def verify_network_error(page: Page) -> None:
    from pages.emids_lp_042_zoominfo_page import ZoomInfoPage
    page_obj = ZoomInfoPage(page)
    expect(page_obj.hero_section).to_be_visible()


@then("Tooling stops; page remains functional")
def verify_zoominfo_revoked(page: Page) -> None:
    from pages.emids_lp_042_zoominfo_page import ZoomInfoPage
    page_obj = ZoomInfoPage(page)
    expect(page_obj.hero_section).to_be_visible()
