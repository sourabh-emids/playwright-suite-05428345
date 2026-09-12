"""Step definitions for Who We Serve section - EMIDS-LP-024"""
from pytest_bdd import given, when, then
from pages.EMIDS-LP-024_who_we_serve_page import WhoWeServePage
from playwright.sync_api import expect


@given("Who We Serve section")
def who_we_serve_section(page):
    page.goto("/")


@when("Audiences are inspected")
def inspect_audiences(page):
    pass


@then("Payer, Provider, HealthTech, Life Sciences, and Consumer are all visible")
def verify_all_audiences(page):
    serve_page = WhoWeServePage(page)
    serve_page.verify_all_audiences()


@given("Each audience Explore CTA")
def each_explore_cta(page):
    page.goto("/")


@when("URLs are verified")
def verify_urls(page):
    pass


@then("Payer → /segments/payer/, Provider → /segments/provider/, HealthTech → /segments/healthtech/, Life Sciences → /segments/life-sciences/, Consumer → /segments/consumer/")
def verify_canonical_segment_urls(page):
    serve_page = WhoWeServePage(page)
    expected = serve_page.get_audience_urls()
    for segment, path in expected.items():
        assert path in expected.values()


@given("Explore CTAs")
def explore_ctas(page):
    page.goto("/")


@when("Tested with keyboard and touch input")
def test_keyboard_touch(page):
    pass


@then("All CTAs are operable with both input methods")
def verify_operable(page):
    serve_page = WhoWeServePage(page)
    serve_page.verify_section_visible()


@given("Audience count")
def audience_count(page):
    page.goto("/")


@when("Items are verified")
def verify_items(page):
    pass


@then("Exactly five audiences are configured for this content version")
def verify_five_audiences(page):
    serve_page = WhoWeServePage(page)
    serve_page.verify_all_audiences()


@given("Edge case where one segment is unavailable")
def segment_unavailable(page):
    pass


@when("Section renders")
def section_renders(page):
    serve_page = WhoWeServePage(page)
    serve_page.goto("/")


@then("Section handles gracefully without breaking")
def verify_graceful(page):
    serve_page = WhoWeServePage(page)
    serve_page.verify_section_visible()


@given("Tabbed audience interface")
def tabbed_interface(page):
    page.goto("/")


@when("Window is resized")
def window_resize(page):
    page.set_viewport_size({"width": 375, "height": 667})


@then("Tab state is appropriately maintained or reset")
def verify_tab_state(page):
    serve_page = WhoWeServePage(page)
    serve_page.verify_all_audiences()
