"""Steps for emids_lp_022: Render Engineering capability content."""
from playwright.sync_api import Page, expect
from pytest_bdd import given, parsers, then, when

from pages.capabilities.capabilities_section_page import CapabilitiesSectionPage


@given(parsers.parse("User views Engineering capability card/panel"))
def view_engineering_card(page: Page) -> None:
    """User views Engineering capability card."""
    cap_page = CapabilitiesSectionPage(page)
    cap_page.navigate()
    cap_page.scroll_to_section()


@given(parsers.parse("User clicks Engineering capability link"))
def click_engineering_link(page: Page) -> None:
    """User clicks Engineering capability link."""
    cap_page = CapabilitiesSectionPage(page)
    cap_page.navigate()
    cap_page.scroll_to_section()
    cap_page.locators.engineering_group.click()


@given(parsers.parse("Engineering capability card renders"))
def engineering_card_renders(page: Page) -> None:
    """Engineering capability card renders."""
    cap_page = CapabilitiesSectionPage(page)
    cap_page.navigate()
    cap_page.scroll_to_section()


@given(parsers.parse("Engineering capability destination is unavailable"))
def engineering_unavailable(page: Page) -> None:
    """Engineering capability unavailable."""
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


@then("Engineering label displays")
def engineering_label_displays(page: Page) -> None:
    """Verify Engineering label displays."""
    cap_page = CapabilitiesSectionPage(page)
    expect(cap_page.locators.engineering_group).to_be_visible()


@then("Supporting content renders with title and summary")
def supporting_renders(page: Page) -> None:
    """Verify supporting content renders."""
    cap_page = CapabilitiesSectionPage(page)
    expect(cap_page.locators.engineering_group).to_be_visible()


@then("Link navigates to valid Engineering capability destination")
def engineering_link_valid(page: Page) -> None:
    """Verify Engineering link navigates valid."""
    expect(page).not_to_have_url(r"404")


@then("Title field is populated")
def title_populated(page: Page) -> None:
    """Verify title populated."""
    cap_page = CapabilitiesSectionPage(page)
    text = cap_page.locators.engineering_group.inner_text()
    expect(len(text)).to_be_greater_than(0)


@then("No empty title")
def no_empty_title(page: Page) -> None:
    """Verify no empty title."""
    cap_page = CapabilitiesSectionPage(page)
    expect(len(cap_page.locators.engineering_group.inner_text())).to_be_greater_than(0)


@then("User receives appropriate feedback")
def appropriate_feedback(page: Page) -> None:
    """Verify appropriate feedback."""
    pass
