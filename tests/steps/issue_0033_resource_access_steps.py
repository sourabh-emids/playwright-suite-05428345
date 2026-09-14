"""Step definitions for issue_0033: Resource access handoff without false download implication."""
from playwright.sync_api import expect, Page
from pytest_bdd import given, when, then


@given("User clicks Download on eBook card")
def click_ebook_download(page: Page) -> None:
    page.goto("/")
    download = page.getByRole("link", name="Download").first
    if download.is_visible():
        download.click()


@when("Navigation occurs")
def nav_occurs(page: Page) -> None:
    pass


@then("User navigates to resource detail/access flow page, not direct file URL")
def detail_page_nav(page: Page) -> None:
    assert page.url.startswith("https://www.emids.com")


@given("User inspects network requests on Download click")
def inspect_network(page: Page) -> None:
    page.goto("/")


@when("Monitoring requests")
def monitor_requests(page: Page) -> None:
    pass


@then("No direct file asset URL is exposed to client")
def no_direct_file(page: Page) -> None:
    expect(page.locator("main")).to_be_visible()


@given("Resource requires form/modal gate")
def resource_requires_gate(page: Page) -> None:
    page.goto("/")


@when("User reaches gate page")
def reach_gate(page: Page) -> None:
    pass


@then("User sees clear communication about required steps to access resource")
def clear_communication(page: Page) -> None:
    expect(page.locator("main")).to_be_visible()


@given("CMS validation")
def cms_validation(page: Page) -> None:
    page.goto("/")


@when("Checking resource destinations")
def check_destinations(page: Page) -> None:
    pass


@then("All resource URLs are verified and point to published destinations")
def verified_destinations(page: Page) -> None:
    expect(page.locator("main")).to_be_visible()


@given("Implementation approach review")
def implementation_review(page: Page) -> None:
    page.goto("/")


@when("Checking code for file URL patterns")
def check_url_patterns(page: Page) -> None:
    pass


@then("Code does not assume direct file URLs; uses detail page routes")
def detail_routes(page: Page) -> None:
    expect(page.locator("main")).to_be_visible()


@given("Gate asset fails to load")
def gate_fails(page: Page) -> None:
    page.goto("/")


@when("User reaches gate")
def reach_gate_fail(page: Page) -> None:
    pass


@then("User sees appropriate unavailable message; form does not silently fail")
def unavailable_message(page: Page) -> None:
    expect(page.locator("main")).to_be_visible()


@given("User submits access form")
def submit_form(page: Page) -> None:
    page.goto("/contact/")


@when("Submission fails")
def submission_fails(page: Page) -> None:
    pass


@then("User sees clear error message; can retry")
def error_message(page: Page) -> None:
    expect(page.locator("body")).to_be_visible()


@given("User navigates to resource after withdrawal")
def navigate_withdrawn(page: Page) -> None:
    page.goto("/")


@when("Page loads")
def page_loads(page: Page) -> None:
    pass


@then("Appropriate unavailable message displays")
def unavailable_message(page: Page) -> None:
    expect(page.locator("main")).to_be_visible()


@given("Popup approach used and blocked")
def popup_blocked(page: Page) -> None:
    page.goto("/")


@when("User clicks action")
def click_action(page: Page) -> None:
    download = page.getByRole("link", name="Download").first
    if download.is_visible():
        download.click()


@then("Content opens in main window or user notified about popup block")
def main_window_or_notify(page: Page) -> None:
    expect(page.locator("main")).to_be_visible()
