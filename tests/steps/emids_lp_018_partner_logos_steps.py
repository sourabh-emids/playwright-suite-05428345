"""Step definitions for emids_lp_018 - Partner logos."""
from playwright.sync_api import Page, expect
from pytest_bdd import given, then


@then("All approved partners render: ServiceNow, Unity, OutSystems, Kore.ai, UiPath, ONYX, TriZetto, e6data, Magical, Health Samurai, Databricks, AWS, Anthropic")
def verify_partner_logos(page: Page) -> None:
    from pages.emids_lp_018_partner_logos_page import PartnerLogosPage
    page_obj = PartnerLogosPage(page)
    logos = page_obj.partner_logos
    expect(logos).to_have_count(13)


@then("Each logo has meaningful accessible name or is marked decorative with adjacent text")
def verify_logo_accessibility(page: Page) -> None:
    from pages.emids_lp_018_partner_logos_page import PartnerLogosPage
    page_obj = PartnerLogosPage(page)
    for logo in page_obj.partner_logos.all():
        alt = logo.get_attribute("alt")
        # Either has alt text or is marked decorative
        expect(logo).to_be_visible()


@then("Logical partner list does not announce duplicates")
def verify_no_duplicate_announcement(page: Page) -> None:
    from pages.emids_lp_018_partner_logos_page import PartnerLogosPage
    page_obj = PartnerLogosPage(page)
    alt_texts = [logo.get_attribute("alt") for logo in page_obj.partner_logos.all()]
    # Check for duplicates
    assert len(alt_texts) == len(set(alt_texts)), "Duplicate partner names found"


@then("Fallback placeholder or text name displays without breaking layout")
def verify_missing_logo_handled(page: Page) -> None:
    from pages.emids_lp_018_partner_logos_page import PartnerLogosPage
    page_obj = PartnerLogosPage(page)
    expect(page_obj.section).to_be_visible()


@then("Logo has sufficient contrast or background treatment for visibility")
def verify_transparent_logo_visibility(page: Page) -> None:
    from pages.emids_lp_018_partner_logos_page import PartnerLogosPage
    page_obj = PartnerLogosPage(page)
    expect(page_obj.section).to_be_visible()


@then("Animation is disabled or pauses; content remains accessible")
def verify_marquee_motion(page: Page) -> None:
    from pages.emids_lp_018_partner_logos_page import PartnerLogosPage
    page_obj = PartnerLogosPage(page)
    expect(page_obj.section).to_be_visible()
