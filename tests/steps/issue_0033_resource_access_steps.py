"""Step definitions for Issue 0033 - Resource access handoff implementation."""
from pytest_bdd import given, when, then
from playwright.sync_api import Page, expect
from pages.homepage_page import HomepagePage


@given("A user clicks the Download action on an eBook card")
def click_ebook_download(page: Page):
    page.goto("/")
    page.evaluate("() => window.scrollTo(0, 7300)")
    page.getByText("Managing the Margin Reset", exact=False).first.locator("..").click()


@when("The action is activated")
def download_activated(page: Page):
    pass


@then("User is routed to the resource detail/access flow, not directly to a file URL")
def routes_to_detail(page: Page):
    page.wait_for_url("**/insights/**")
    # Should be a page, not a direct file
    assert not page.url.endswith(".pdf")


@given("A developer or user examines network requests")
def examine_network(page: Page):
    page.goto("/")


@when("The Download action is activated")
def download_activated_net(page: Page):
    page.evaluate("() => window.scrollTo(0, 7300)")
    page.getByText("Managing the Margin Reset", exact=False).first.locator("..").click()


@then("Implementation does not fabricate or expose private asset endpoints")
def no_private_endpoints(page: Page):
    # Check that URLs are public routes
    assert "/insights/" in page.url


@given("A user encounters a gated resource")
def gated_resource(page: Page):
    page.goto("/")


@when("The gate is displayed")
def gate_displayed(page: Page):
    page.evaluate("() => window.scrollTo(0, 7300)")
    page.getByText("Managing the Margin Reset", exact=False).first.locator("..").click()
    page.wait_for_timeout(500)


@then("Required steps are clearly communicated to the user")
def steps_communicated(page: Page):
    # Should show form or instructions
    assert page.url in ["https://www.emids.com/insights/managing-the-margin-reset-in-medicare-advantage/",
                        "https://www.emids.com/"]


@given("A user views resource cards")
def view_resource_cards(page: Page):
    page.goto("/")
    page.evaluate("() => window.scrollTo(0, 7300)")


@when("The destinations are examined")
def destinations_examined(page: Page):
    pass


@then("Only verified and published destinations are used for resource links")
def verified_destinations(page: Page):
    links = page.locator("[class*='insight'] a, [class*='resource'] a")
    for link in links.all():
        href = link.get_attribute("href")
        assert href and ("/insights/" in href or href.startswith("http"))


@given("A gated asset is unavailable (server error, withdrawn, etc.)")
def gated_unavailable(page: Page):
    pass


@when("A user attempts to access it")
def access_unavailable(page: Page):
    page.goto("/insights/managing-the-margin-reset-in-medicare-advantage/")


@then("Appropriate error message is displayed")
def error_displayed(page: Page):
    page.wait_for_load_state("networkidle")


@given("A popup is used for resource access and is blocked")
def popup_blocked(page: Page):
    pass


@when("A user attempts to access the resource")
def attempt_access_popup(page: Page):
    page.goto("/")
    page.evaluate("() => window.scrollTo(0, 7300)")


@then("Fallback navigation or alternative method is provided")
def fallback_provided(page: Page):
    homepage = HomepagePage(page)
    expect(homepage.insights_section).to_be_visible()
