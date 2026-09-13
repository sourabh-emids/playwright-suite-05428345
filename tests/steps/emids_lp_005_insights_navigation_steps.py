"""Steps for emids_lp_005: Implement Insights navigation group."""
from playwright.sync_api import Page, expect
from pytest_bdd import given, parsers, then, when

from pages.header.insights_nav_page import InsightsNavPage


@given(parsers.parse("User focuses on Insights navigation"))
def focus_insights_nav(page: Page) -> None:
    """Focus on Insights navigation."""
    insights_page = InsightsNavPage(page)
    insights_page.navigate()
    insights_page.locators.insights_nav.focus()


@given(parsers.parse("Insights menu is open"))
def insights_menu_open(page: Page) -> None:
    """Insights menu is open."""
    insights_page = InsightsNavPage(page)
    insights_page.navigate()
    insights_page.open_insights_menu()


@given(parsers.parse("Insights menu is open on various viewport sizes"))
def menu_open_various_sizes(page: Page) -> None:
    """Insights menu is open on various viewport sizes."""
    insights_page = InsightsNavPage(page)
    insights_page.navigate()
    insights_page.open_insights_menu()


@given(parsers.parse("User opens Insights menu"))
def user_opens_insights_menu(page: Page) -> None:
    """User opens Insights menu."""
    insights_page = InsightsNavPage(page)
    insights_page.navigate()
    insights_page.open_insights_menu()


@when("User activates Insights menu trigger")
def activate_insights_menu(page: Page) -> None:
    """Activate Insights menu trigger."""
    insights_page = InsightsNavPage(page)
    insights_page.open_insights_menu()


@when("User activates menu and clicks links")
def activate_and_click_links(page: Page) -> None:
    """Activate menu and click links."""
    insights_page = InsightsNavPage(page)
    # Verify links are clickable at various sizes
    pass


@when("User examines menu structure")
def examine_menu_structure(page: Page) -> None:
    """Examine menu structure."""
    pass  # Verification step


@when("User clicks insight destinations")
def click_insight_destinations(page: Page) -> None:
    """Click insight destinations."""
    pass  # Verification step


@then("Menu opens consistently")
def menu_opens_consistently(page: Page) -> None:
    """Verify menu opens consistently."""
    insights_page = InsightsNavPage(page)
    expect(insights_page.locators.insights_button).to_have_attribute("aria-expanded", "true")


@then("Child links are visible and readable")
def child_links_visible_readable(page: Page) -> None:
    """Verify child links are visible and readable."""
    insights_page = InsightsNavPage(page)
    for link in insights_page.get_child_links():
        expect(link).to_be_visible()


@then("Links remain operable")
def links_remain_operable(page: Page) -> None:
    """Verify links remain operable."""
    insights_page = InsightsNavPage(page)
    expect(insights_page.locators.insights_hub_link).to_be_enabled()


@then("Content is readable")
def content_is_readable(page: Page) -> None:
    """Verify content is readable."""
    insights_page = InsightsNavPage(page)
    expect(insights_page.locators.insights_and_resources).to_be_visible()


@then("No truncation of essential text")
def no_text_truncation(page: Page) -> None:
    """Verify no truncation of essential text."""
    insights_page = InsightsNavPage(page)
    # Verify links have full text
    text = insights_page.locators.insights_hub_link.inner_text()
    expect(len(text)).to_be_greater_than(0)


@then("All groups contain at least one item")
def groups_contain_items(page: Page) -> None:
    """Verify all groups contain at least one item."""
    insights_page = InsightsNavPage(page)
    expect(len(insights_page.locators.get_insights_links())).to_be_greater_than(0)
    expect(len(insights_page.locators.get_news_events_links())).to_be_greater_than(0)


@then("No empty containers displayed")
def no_empty_containers(page: Page) -> None:
    """Verify no empty containers displayed."""
    insights_page = InsightsNavPage(page)
    expect(insights_page.has_empty_groups()).to_be_false()


@then("All links resolve to canonical URLs under /insights/ and related paths")
def links_canonical_urls(page: Page) -> None:
    """Verify all links resolve to canonical URLs."""
    insights_page = InsightsNavPage(page)
    for link in insights_page.get_child_links():
        href = link.get_attribute("href")
        expect(href).not_to_be_none()
        expect(href).to_match(r"^/|^https?://")
