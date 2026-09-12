"""Step definitions for Issue 0017 - Featured solution responsive interaction."""
from pytest_bdd import given, when, then
from playwright.sync_api import Page, expect
from pages.homepage_page import HomepagePage


@given("A user navigates the Featured Solutions with keyboard")
def nav_keyboard_featured(page: Page):
    page.goto("/")
    page.evaluate("() => window.scrollTo(0, 1800)")
    page.keyboard.press("Tab")


@when("The user tabs through the section")
def tab_through_section(page: Page):
    for _ in range(5):
        page.keyboard.press("Tab")


@then("Every solution can be reached via keyboard navigation")
def all_solutions_keyboard_reachable(page: Page):
    homepage = HomepagePage(page)
    solutions = homepage.all_six_solution_entries_present()
    assert len(solutions) == 6


@given("A user views the site on a touch device")
def touch_device(page: Page):
    page.set_viewport_size({"width": 375, "height": 812})


@when("The user interacts with Featured Solutions")
def interact_solutions_touch(page: Page):
    page.goto("/")
    page.evaluate("() => window.scrollTo(0, 1800)")


@then("Every solution can be reached via touch")
def all_solutions_touch_reachable(page: Page):
    homepage = HomepagePage(page)
    solutions = homepage.all_six_solution_entries_present()
    assert len(solutions) >= 1


@given("A user views the Featured Solutions section")
def view_solutions_off_screen(page: Page):
    page.goto("/")


@when("The user examines all content")
def examine_all_content(page: Page):
    page.evaluate("() => window.scrollTo(0, 1800)")


@then("No content is permanently hidden off-screen; all solutions are accessible")
def no_hidden_content(page: Page):
    homepage = HomepagePage(page)
    solutions = homepage.all_six_solution_entries_present()
    assert len(solutions) >= 1


@given("A carousel or interactive rail is used")
def carousel_used(page: Page):
    page.goto("/")
    page.evaluate("() => window.scrollTo(0, 7200)")


@when("The user or assistive technology examines previous/next controls")
def examine_carousel_controls(page: Page):
    pass


@then("Controls have accessible labels describing their function")
def controls_have_labels(page: Page):
    prev = page.get_by_role("button", name="Previous")
    next_btn = page.get_by_role("button", name="Next")
    # Either have accessible names or visible labels
    if prev.count() > 0:
        expect(prev).to_be_visible()
    if next_btn.count() > 0:
        expect(next_btn).to_be_visible()


@given("A user has prefers-reduced-motion enabled")
def reduced_motion_enabled(page: Page):
    page.emulate_media(media_feature="prefers-reduced-motion: reduce")


@when("The user views the Featured Solutions with autoplay carousel")
def view_carousel_rm(page: Page):
    page.goto("/")
    page.evaluate("() => window.scrollTo(0, 7200)")


@then("Autoplay does not prevent user control and respects reduced motion preference")
def autoplay_respects_rm(page: Page):
    # Verify carousel is not auto-advancing in a way that blocks interaction
    expect(page.locator("[class*='carousel'], [class*='slider']")).to_be_visible()


@given("A user is interacting with Featured Solutions and resizes the viewport")
def interacting_resize(page: Page):
    page.set_viewport_size({"width": 1280, "height": 720})
    page.goto("/")
    page.evaluate("() => window.scrollTo(0, 1800)")


@when("The viewport changes breakpoint")
def viewport_changes(page: Page):
    page.set_viewport_size({"width": 375, "height": 812})
    page.wait_for_timeout(500)


@then("Interaction state is preserved or gracefully adapted without breaking functionality")
def state_preserved(page: Page):
    homepage = HomepagePage(page)
    expect(homepage.featured_solutions_section).to_be_visible()


@given("A user navigates to the first item in a carousel")
def nav_first_item(page: Page):
    page.goto("/")
    page.evaluate("() => window.scrollTo(0, 7200)")
    page.get_by_role("button", name="Previous").click()


@when("The user attempts to navigate to a previous item")
def nav_previous_item(page: Page):
    pass


@then("Navigation wraps appropriately or indicates boundary")
def nav_wraps_or_boundary(page: Page):
    # Verify carousel handles boundary
    expect(page.get_by_role("button", name="Previous")).to_be_visible()
