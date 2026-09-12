"""Step definitions for Issue 0005 - Insights navigation group implementation."""
from pytest_bdd import given, when, then
from playwright.sync_api import Page, expect
from pages.homepage_page import HomepagePage


@given("A user is viewing the Emids homepage desktop header")
def user_viewing_homepage_desktop(page: Page):
    page.set_viewport_size({"width": 1280, "height": 720})
    page.goto("/")


@when("The user activates the Insights navigation item")
def activate_insights(page: Page):
    homepage = HomepagePage(page)
    homepage.hover_solutions_nav()  # Navigate to hover area
    page.get_by_role("button", name="Insights").hover()
    page.wait_for_timeout(500)


@then("The menu opens displaying thought leadership, resources, and destinations")
def insights_menu_opens(page: Page):
    expect(page.getByText("Insights and Resources")).to_be_visible()
    expect(page.getByText("News & Events")).to_be_visible()


@given("A user has the Insights menu open at various viewport widths")
def insights_menu_open_various_widths(page: Page):
    pass


@when("The user views the menu at desktop, tablet, and mobile widths")
def view_menu_at_breakpoints(page: Page):
    # Desktop
    page.set_viewport_size({"width": 1280, "height": 720})
    page.goto("/")
    page.get_by_role("button", name="Insights").hover()
    page.wait_for_timeout(500)
    expect(page.getByText("Insights and Resources")).to_be_visible()
    
    # Tablet (close menu first)
    page.keyboard.press("Escape")
    page.set_viewport_size({"width": 768, "height": 1024})
    page.get_by_role("button", name="Insights").hover()
    page.wait_for_timeout(500)
    
    # Mobile
    page.keyboard.press("Escape")
    page.set_viewport_size({"width": 375, "height": 812})
    page.get_by_role("button", name="Insights").click()
    page.wait_for_timeout(500)


@then("Child links are readable and operable at all supported breakpoints")
def child_links_readable_operable(page: Page):
    expect(page.getByText("Insights Hub", exact=False)).to_be_visible()
    expect(page.getByText("Case Studies", exact=False)).to_be_visible()


@given("A user has the Insights menu open")
def insights_menu_open(page: Page):
    page.set_viewport_size({"width": 1280, "height": 720})
    page.goto("/")
    page.get_by_role("button", name="Insights").hover()
    page.wait_for_timeout(500)


@when("The user examines the menu groups")
def examine_insights_menu_groups(page: Page):
    pass


@then("No menu groups are empty; each has at least one destination")
def no_empty_menu_groups(page: Page):
    expect(page.getByText("Insights Hub", exact=False)).to_be_visible()
    expect(page.getByText("Case Studies", exact=False)).to_be_visible()
    expect(page.getByText("eBooks", exact=False)).to_be_visible()


@when("The user clicks on any Insights link")
def click_insights_link(page: Page):
    page.getByText("Insights Hub", exact=False).first.locator("..").click()


@then("The destination URL is canonical")
def insights_destination_canonical(page: Page):
    page.wait_for_load_state("networkidle")
    expect(page).to_have_url("**/insights/**")
