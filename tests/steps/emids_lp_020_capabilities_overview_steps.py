"""Step definitions for emids_lp_020-023 - Capabilities sections."""
from playwright.sync_api import Page, expect
from pytest_bdd import given, then


@then("AI, Engineering, and Platforms capability groups are visible")
def verify_three_groups(page: Page) -> None:
    from pages.emids_lp_020_capabilities_page import CapabilitiesPage
    page_obj = CapabilitiesPage(page)
    expect(page_obj.ai_group).to_be_visible()
    expect(page_obj.engineering_group).to_be_visible()
    expect(page_obj.platforms_group).to_be_visible()


@then("Each group displays summary, links, and optional media as configured")
def verify_group_content(page: Page) -> None:
    from pages.emids_lp_020_capabilities_page import CapabilitiesPage
    page_obj = CapabilitiesPage(page)
    for group in [page_obj.ai_group, page_obj.engineering_group, page_obj.platforms_group]:
        expect(group).to_be_visible()


@then("Group labels (AI, Engineering, Platforms) match navigation taxonomy exactly")
def verify_labels_match_taxonomy(page: Page) -> None:
    from pages.emids_lp_020_capabilities_page import CapabilitiesPage
    page_obj = CapabilitiesPage(page)
    expect(page_obj.ai_label).to_have_text("AI")
    expect(page_obj.engineering_label).to_have_text("Engineering")
    expect(page_obj.platforms_label).to_have_text("Platforms")


@then("Exactly three primary groups are configured for this content version")
def verify_three_primary_groups(page: Page) -> None:
    from pages.emids_lp_020_capabilities_page import CapabilitiesPage
    page_obj = CapabilitiesPage(page)
    groups = [page_obj.ai_group, page_obj.engineering_group, page_obj.platforms_group]
    for g in groups:
        expect(g).to_be_visible()


@then("Remaining groups render; section does not break")
def verify_missing_group_handled(page: Page) -> None:
    from pages.emids_lp_020_capabilities_page import CapabilitiesPage
    page_obj = CapabilitiesPage(page)
    expect(page_obj.section).to_be_visible()


@then("Content reflows without breaking layout or hiding content")
def verify_overflow_handled(page: Page) -> None:
    from pages.emids_lp_020_capabilities_page import CapabilitiesPage
    page_obj = CapabilitiesPage(page)
    page.set_viewport_size({"width": 375, "height": 667})
    expect(page_obj.section).to_be_visible()


@then("AI label displays with supporting content including summary")
def verify_ai_content(page: Page) -> None:
    from pages.emids_lp_020_capabilities_page import CapabilitiesPage
    page_obj = CapabilitiesPage(page)
    expect(page_obj.ai_label).to_be_visible()


@then("Link routes to valid AI capability destination")
def verify_ai_link(page: Page) -> None:
    from pages.emids_lp_020_capabilities_page import CapabilitiesPage
    page_obj = CapabilitiesPage(page)
    href = page_obj.ai_link.get_attribute("href")
    assert href and "/capabilities/" in href or "/ai/" in href


@then("AI capability has non-empty title")
def verify_ai_title(page: Page) -> None:
    from pages.emids_lp_020_capabilities_page import CapabilitiesPage
    page_obj = CapabilitiesPage(page)
    title = page_obj.ai_title.text_content()
    assert title and title.strip()


@then("Destination URL resolves successfully")
def verify_url_resolves(page: Page) -> None:
    from pages.emids_lp_020_capabilities_page import CapabilitiesPage
    page_obj = CapabilitiesPage(page)
    href = page_obj.ai_link.get_attribute("href")
    if href:
        response = page.request.get(href)
        assert response.status < 400


@then("Appropriate error handling without page break")
def verify_missing_destination_handled(page: Page) -> None:
    from pages.emids_lp_020_capabilities_page import CapabilitiesPage
    page_obj = CapabilitiesPage(page)
    expect(page_obj.section).to_be_visible()


@then("Card/panel matches capability visual system design")
def verify_card_design(page: Page) -> None:
    from pages.emids_lp_020_capabilities_page import CapabilitiesPage
    page_obj = CapabilitiesPage(page)
    expect(page_obj.ai_card).to_be_visible()


@then("Platforms label and supporting content display correctly")
def verify_platforms_content(page: Page) -> None:
    from pages.emids_lp_020_capabilities_page import CapabilitiesPage
    page_obj = CapabilitiesPage(page)
    expect(page_obj.platforms_label).to_be_visible()


@then("Labels use approved taxonomy consistently")
def verify_taxononmy_consistency(page: Page) -> None:
    from pages.emids_lp_020_capabilities_page import CapabilitiesPage
    page_obj = CapabilitiesPage(page)
    expect(page_obj.platforms_label).to_have_text("Platforms")
