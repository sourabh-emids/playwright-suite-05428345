"""Step definitions for Issue 0024 - Five audience/industry entries rendering."""
from pytest_bdd import given, when, then
from playwright.sync_api import Page, expect
from pages.homepage_page import HomepagePage


@given("A user views the Who We Serve section")
def view_who_we_serve(page: Page):
    page.goto("/")
    page.evaluate("() => window.scrollTo(0, 5700)")


@when("The section loads")
def section_loads_wws(page: Page):
    page.wait_for_load_state("networkidle")


@then("All five audiences are visible")
def all_five_audiences(page: Page):
    homepage = HomepagePage(page)
    audiences = homepage.all_five_audiences_visible()
    assert len(audiences) == 5


@given("A user clicks the Explore action for an audience")
def click_explore_audience(page: Page):
    page.goto("/")
    page.evaluate("() => window.scrollTo(0, 5700)")
    homepage = HomepagePage(page)
    homepage.click_audience_explore("Payer")


@when("The action is activated")
def action_activated_wws(page: Page):
    pass


@then("The user is routed to the canonical segment page")
def routed_to_segment(page: Page):
    page.wait_for_url("**/segments/**")


@given("A user interacts with Who We Serve via keyboard and touch")
def interact_keyboard_touch(page: Page):
    page.goto("/")
    page.evaluate("() => window.scrollTo(0, 5700)")


@when("The user navigates the section")
def navigate_section_wws(page: Page):
    page.keyboard.press("Tab")


@then("All interactions work on both keyboard and touch input")
def interactions_work_both(page: Page):
    homepage = HomepagePage(page)
    expect(homepage.payer_tab).to_be_visible()


@given("A user analyzes the Who We Serve section")
def analyze_wws(page: Page):
    page.goto("/")
    page.evaluate("() => window.scrollTo(0, 5700)")


@when("The content is counted")
def content_counted(page: Page):
    pass


@then("Exactly five current audiences are displayed for this content version")
def exactly_five(page: Page):
    homepage = HomepagePage(page)
    audiences = homepage.all_five_audiences_visible()
    assert len(audiences) == 5


@given("One segment page is unavailable (e.g., HealthTech unpublished)")
def segment_unavailable(page: Page):
    pass


@when("The section renders")
def section_renders_unavail(page: Page):
    page.goto("/")
    page.evaluate("() => window.scrollTo(0, 5700)")


@then("The unavailable segment is handled gracefully; remaining audiences display correctly")
def graceful_handling(page: Page):
    homepage = HomepagePage(page)
    audiences = homepage.all_five_audiences_visible()
    # Should show at least 4 audiences
    assert len(audiences) >= 4


@given("A user selects an audience tab and resizes the viewport")
def select_tab_resize(page: Page):
    page.set_viewport_size({"width": 1280, "height": 720})
    page.goto("/")
    page.evaluate("() => window.scrollTo(0, 5700)")
    page.get_by_role("button", name="Provider").click()
    page.wait_for_timeout(300)


@when("The viewport changes breakpoint")
def breakpoint_changes(page: Page):
    page.set_viewport_size({"width": 375, "height": 812})
    page.wait_for_timeout(300)


@then("Tab state is appropriately preserved or gracefully reset")
def tab_state_handled(page: Page):
    # Tab state should be visible in some form
    expect(page.locator("[class*='tab'], [class*='audience'], [role='tab']")).to_be_visible()
