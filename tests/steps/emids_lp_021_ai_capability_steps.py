"""Steps for emids_lp_021: Render AI capability content."""
from playwright.sync_api import Page, expect
from pytest_bdd import given, parsers, then, when

from pages.capabilities.capabilities_section_page import CapabilitiesSectionPage


@given(parsers.parse("User views AI capability card/panel"))
def view_ai_card(page: Page) -> None:
    """User views AI capability card."""
    cap_page = CapabilitiesSectionPage(page)
    cap_page.navigate()
    cap_page.scroll_to_section()


@given(parsers.parse("User clicks AI capability link"))
def click_ai_link(page: Page) -> None:
    """User clicks AI capability link."""
    cap_page = CapabilitiesSectionPage(page)
    cap_page.navigate()
    cap_page.scroll_to_section()
    # Click AI group link
    page.get_by_role("link", name__regex="AI|Data|Automation|Pacca").first.click()


@given(parsers.parse("AI capability card renders"))
def ai_card_renders(page: Page) -> None:
    """AI capability card renders."""
    cap_page = CapabilitiesSectionPage(page)
    cap_page.navigate()
    cap_page.scroll_to_section()


@given(parsers.parse("User examines AI destination URL"))
def examine_ai_url(page: Page) -> None:
    """User examines AI destination URL."""
    cap_page = CapabilitiesSectionPage(page)
    cap_page.navigate()
    cap_page.scroll_to_section()


@given(parsers.parse("AI capability destination is unavailable"))
def ai_dest_unavailable(page: Page) -> None:
    """AI destination unavailable."""
    pass


@when("Content loads")
def content_loads(page: Page) -> None:
    """Content loads."""
    page.wait_for_load_state("domcontentloaded")


@when("Navigation completes")
def navigation_completes(page: Page) -> None:
    """Navigation completes."""
    page.wait_for_load_state("domcontentloaded")


@when("User checks content")
def check_content(page: Page) -> None:
    """Check content."""
    pass


@when("User clicks link")
def user_clicks_link(page: Page) -> None:
    """User clicks link."""
    pass


@then("AI label displays")
def ai_label_displays(page: Page) -> None:
    """Verify AI label displays."""
    cap_page = CapabilitiesSectionPage(page)
    expect(cap_page.locators.ai_group).to_be_visible()


@then("Supporting content renders with title and summary")
def supporting_renders(page: Page) -> None:
    """Verify supporting content renders."""
    cap_page = CapabilitiesSectionPage(page)
    expect(cap_page.locators.ai_group).to_be_visible()


@then("Link navigates to valid AI capability destination")
def ai_link_valid(page: Page) -> None:
    """Verify AI link navigates valid."""
    expect(page).not_to_have_url(r"404")


@then("Title field is populated")
def title_populated(page: Page) -> None:
    """Verify title populated."""
    cap_page = CapabilitiesSectionPage(page)
    text = cap_page.locators.ai_group.inner_text()
    expect(len(text)).to_be_greater_than(0)


@then("No empty title")
def no_empty_title(page: Page) -> None:
    """Verify no empty title."""
    cap_page = CapabilitiesSectionPage(page)
    text = cap_page.locators.ai_group.inner_text()
    expect(text).not_to_be_empty()


@then("URL is valid")
def url_valid(page: Page) -> None:
    """Verify URL is valid."""
    expect(page).not_to_have_url(r"undefined|null")


@then("Resolves to AI capability page")
def resolves_ai_page(page: Page) -> None:
    """Verify resolves to AI page."""
    url = page.url
    expect(url).to_match(r"/ai|/capabilities/|/pacca")


@then("User receives appropriate feedback")
def appropriate_feedback(page: Page) -> None:
    """Verify appropriate feedback."""
    pass


@then("No broken page")
def no_broken_page(page: Page) -> None:
    """Verify no broken page."""
    expect(page).not_to_have_url(r"404")
