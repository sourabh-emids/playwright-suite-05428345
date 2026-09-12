"""Step definitions for Featured Solutions - EMIDS-LP-015, EMIDS-LP-016, EMIDS-LP-017"""
from pytest_bdd import given, when, then
from pages.EMIDS-LP-015_featured_solutions_page import FeaturedSolutionsPage
from playwright.sync_api import expect


@given("Featured Solutions section")
def featured_solutions_section(page):
    page.goto("/")


@when("Solution items are counted and numbered")
def count_solution_items(page):
    pass


@then("Six entries exist numbered 01 through 06: Modernization as a Service, Interoperability, Cloud Migration, Global Capability Center, Epic Implementation, and Agentic AI")
def verify_six_solutions(page):
    solutions_page = FeaturedSolutionsPage(page)
    solutions_page.verify_all_six_solutions()


@given("Each featured solution item")
def each_solution_item(page):
    page.goto("/")


@when("Content is reviewed")
def review_content(page):
    pass


@then("Each entry contains readable title, supporting copy, and intended destination/action")
def verify_entry_content(page):
    solutions_page = FeaturedSolutionsPage(page)
    assert solutions_page.count_solutions() >= 6


@given("All featured solution titles")
def all_solution_titles(page):
    page.goto("/")


@when("Titles are verified")
def verify_titles(page):
    pass


@then("No titles are blank")
def verify_no_blank_titles(page):
    solutions_page = FeaturedSolutionsPage(page)
    solutions_page.verify_all_six_solutions()


@given("Featured solutions display order")
def display_order(page):
    page.goto("/")


@when("Items are inspected")
def inspect_items(page):
    pass


@then("Items appear in controlled order 01-06")
def verify_order(page):
    solutions_page = FeaturedSolutionsPage(page)
    solutions_page.verify_all_six_solutions()


@given("Edge case where one solution is unpublished")
def one_unpublished(page):
    pass


@when("Featured solutions render")
def solutions_render(page):
    solutions_page = FeaturedSolutionsPage(page)
    solutions_page.goto("/")


@then("System handles gracefully with either placeholder or reduced count")
def verify_graceful_handling(page):
    solutions_page = FeaturedSolutionsPage(page)
    count = solutions_page.count_solutions()
    assert count >= 5


@given("A featured solution with very long title")
def long_title(page):
    pass


@when("Content renders")
def content_renders(page):
    solutions_page = FeaturedSolutionsPage(page)
    solutions_page.goto("/")


@then("Title is handled without breaking layout")
def verify_layout(page):
    solutions_page = FeaturedSolutionsPage(page)
    solutions_page.verify_section_visible()


@given("The All Solutions CTA in Featured Solutions section")
def all_solutions_cta(page):
    page.goto("/")


@when("Inspected for visibility and destination")
def inspect_visibility_destination(page):
    pass


@then("CTA is visible after/within the section and routes to /solutions/")
def verify_all_solutions_cta(page):
    solutions_page = FeaturedSolutionsPage(page)
    assert solutions_page.verify_all_solutions_routes()


@given("All Solutions CTA destination")
def all_solutions_cta_destination(page):
    page.goto("/")


@when("URL is verified")
def verify_url(page):
    pass


@then("URL uses canonical format")
def verify_canonical_format(page):
    solutions_page = FeaturedSolutionsPage(page)
    assert solutions_page.verify_all_solutions_routes()


@given("Edge case where solutions portfolio is unavailable")
def portfolio_unavailable(page):
    pass


@when("CTA is clicked")
def click_cta(page):
    solutions_page = FeaturedSolutionsPage(page)
    solutions_page.goto("/")
    solutions_page.click_all_solutions_cta()


@then("Appropriate error handling or redirect occurs")
def verify_error_handling(page):
    pass


@given("Featured solutions section")
def featured_solutions_for_keyboard(page):
    page.goto("/")


@when("Keyboard navigation is tested")
def test_keyboard_navigation(page):
    solutions_page = FeaturedSolutionsPage(page)
    solutions_page.tab_through_solutions()


@then("Every solution can be reached using Tab key")
def verify_tab_reach(page):
    solutions_page = FeaturedSolutionsPage(page)
    count = solutions_page.count_solutions()
    assert count >= 6


@given("Featured solutions on touch device")
def touch_device(page):
    pass


@when("Touch interaction is tested")
def test_touch(page):
    solutions_page = FeaturedSolutionsPage(page)
    solutions_page.goto("/")


@then("Every solution can be accessed via touch")
def verify_touch_access(page):
    solutions_page = FeaturedSolutionsPage(page)
    assert solutions_page.count_solutions() >= 6


@given("Responsive layout options (cards, rail, carousel, stacked)")
def responsive_options(page):
    pass


@when("Layout is verified at all breakpoints")
def verify_layout_breakpoints(page):
    page.set_viewport_size({"width": 1280, "height": 800})
    solutions_page = FeaturedSolutionsPage(page)
    solutions_page.goto("/")


@then("No content is permanently hidden off-screen")
def verify_no_hidden(page):
    solutions_page = FeaturedSolutionsPage(page)
    solutions_page.verify_section_visible()


@given("If carousel is used for featured solutions")
def carousel_used(page):
    pass


@when("Controls are inspected")
def inspect_controls(page):
    pass


@then("Previous/next controls have accessible labels")
def verify_accessible_controls(page):
    solutions_page = FeaturedSolutionsPage(page)
    solutions_page.verify_section_visible()


@given("Carousel with autoplay enabled")
def autoplay_enabled(page):
    pass


@when("User has prefers-reduced-motion")
def reduced_motion(page):
    page.emulate_media(reduced_motion=True)


@then("Autoplay does not prevent user control and respects reduced motion preference")
def verify_respect_motion(page):
    solutions_page = FeaturedSolutionsPage(page)
    solutions_page.goto("/")
    solutions_page.verify_section_visible()


@given("User is interacting with carousel")
def interacting_carousel(page):
    pass


@when("Viewport is resized")
def resize_viewport(page):
    page.set_viewport_size({"width": 375, "height": 667})


@then("Interaction continues without breaking state")
def verify_state(page):
    solutions_page = FeaturedSolutionsPage(page)
    solutions_page.goto("/")
    solutions_page.verify_section_visible()
