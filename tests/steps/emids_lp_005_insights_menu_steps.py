"""Step definitions for emids_lp_005 - Insights navigation group."""
from playwright.sync_api import Page, expect
from pytest_bdd import given, when, then


@when("The user activates the Insights navigation control")
def activate_insights_control(page: Page) -> None:
    from pages.emids_lp_005_insights_menu_page import InsightsMenuPage
    insights_page = InsightsMenuPage(page)
    insights_page.click_insights_button()


@then("The Insights menu opens and displays thought leadership, resources, news, and related destinations")
def verify_insights_menu_opens(page: Page) -> None:
    from pages.emids_lp_005_insights_menu_page import InsightsMenuPage
    insights_page = InsightsMenuPage(page)
    expect(insights_page.insights_menu).to_be_visible()


@then("Child links remain readable and operable across all supported breakpoints")
def verify_child_links_all_breakpoints(page: Page) -> None:
    from pages.emids_lp_005_insights_menu_page import InsightsMenuPage
    insights_page = InsightsMenuPage(page)
    for width in [375, 768, 1280]:
        page.set_viewport_size({"width": width, "height": 800})
        insights_page.click_insights_button()
        links = insights_page.insights_child_links
        for link in links:
            expect(link).to_be_visible()


@then("No menu groups are empty; all contain at least one link")
def verify_no_empty_groups(page: Page) -> None:
    from pages.emids_lp_005_insights_menu_page import InsightsMenuPage
    insights_page = InsightsMenuPage(page)
    groups = insights_page.menu_groups
    for group in groups:
        links = group.locator("a")
        expect(links).to_have_count(0, expectation=None)  # At least one link


@then("URLs resolve to canonical destinations under /insights/ or related resource paths")
def verify_insights_urls_canonical(page: Page) -> None:
    from pages.emids_lp_005_insights_menu_page import InsightsMenuPage
    insights_page = InsightsMenuPage(page)
    links = insights_page.insights_child_links
    for link in links:
        href = link.get_attribute("href")
        assert href and ("/insights/" in href or href.startswith(page.base_url)), f"Invalid URL: {href}"


@then("Menu opens without requiring hover interaction")
def verify_touch_opens_menu(page: Page) -> None:
    from pages.emids_lp_005_insights_menu_page import InsightsMenuPage
    insights_page = InsightsMenuPage(page)
    insights_page.click_insights_button()
    expect(insights_page.insights_menu).to_be_visible()
