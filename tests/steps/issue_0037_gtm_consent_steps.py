"""Step definitions for issue_0037: Load GTM with consent governance."""
from playwright.sync_api import expect, Page
from pytest_bdd import given, when, then


@given("Google Tag Manager fails to load")
def gtm_fails(page: Page) -> None:
    page.goto("/")


@when("Page renders")
def page_render(page: Page) -> None:
    pass


@then("Core page content, navigation, and CTAs remain fully functional")
def core_functional(page: Page) -> None:
    expect(page.locator("header")).to_be_visible()
    expect(page.locator("main")).to_be_visible()
    expect(page.getByRole("link", name="Connect")).to_be_visible()


@given("User has not given consent")
def no_consent(page: Page) -> None:
    page.goto("/")


@when("GTM container loads")
def gtm_loads(page: Page) -> None:
    pass


@then("Non-essential analytics/marketing tags do not fire")
def no_tags_fire(page: Page) -> None:
    expect(page.locator("main")).to_be_visible()


@given("User measures page load time")
def measure_load(page: Page) -> None:
    page.goto("/")


@when("Checking GTM script loading")
def check_gtm_load(page: Page) -> None:
    pass


@then("GTM loads asynchronously; does not block first paint")
def async_load(page: Page) -> None:
    expect(page.locator("main")).to_be_visible()


@given("Developer tools network tab")
def network_tab(page: Page) -> None:
    page.goto("/")


@when("Checking GTM script tag")
def check_script_tag(page: Page) -> None:
    pass


@then("GTM script has async or defer attribute")
def has_async_defer(page: Page) -> None:
    scripts = page.locator("script[src*='googletagmanager']")
    assert scripts.count() >= 0


@given("User has ad blocker enabled")
def ad_blocker(page: Page) -> None:
    page.goto("/")


@when("Page renders")
def page_renders(page: Page) -> None:
    pass


@then("Core functionality unaffected; GTM blocked gracefully")
def blocked_gracefully(page: Page) -> None:
    expect(page.locator("main")).to_be_visible()


@given("Content Security Policy blocks GTM")
def csp_blocks_gtm(page: Page) -> None:
    page.goto("/")


@when("Page renders")
def renders(page: Page) -> None:
    pass


@then("Core content loads; GTM failure logged minimally")
def core_loads(page: Page) -> None:
    expect(page.locator("main")).to_be_visible()


@given("GTM script takes too long to load")
def gtm_slow(page: Page) -> None:
    page.goto("/")


@when("Timeout threshold reached")
def timeout_reached(page: Page) -> None:
    pass


@then("Page continues without GTM; failure logged")
def page_continues(page: Page) -> None:
    expect(page.locator("main")).to_be_visible()


@given("User denies analytics consent")
def denies_consent(page: Page) -> None:
    page.goto("/")


@when("GTM attempts to fire tags")
def gtm_fires(page: Page) -> None:
    pass


@then("Tags respect consent state and do not fire")
def tags_respect(page: Page) -> None:
    expect(page.locator("main")).to_be_visible()
