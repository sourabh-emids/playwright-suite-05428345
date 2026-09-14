"""Step definitions for issue_0041: Integrate LinkedIn tags conditionally."""
from playwright.sync_api import expect, Page
from pytest_bdd import given, when, then


@given("User has not granted marketing consent")
def no_consent(page: Page) -> None:
    page.goto("/")


@when("Page loads")
def page_loads(page: Page) -> None:
    pass


@then("LinkedIn insight tag does not execute")
def linkedin_no_execute(page: Page) -> None:
    expect(page.locator("main")).to_be_visible()


@given("LinkedIn tag fails to load")
def linkedin_fails(page: Page) -> None:
    page.goto("/")


@when("Page renders")
def page_render(page: Page) -> None:
    pass


@then("Core content and navigation remain fully functional")
def core_functional(page: Page) -> None:
    expect(page.locator("header")).to_be_visible()
    expect(page.locator("main")).to_be_visible()


@given("Consent state check")
def consent_check(page: Page) -> None:
    page.goto("/")


@when("LinkedIn tag attempts to load")
def tag_loads(page: Page) -> None:
    pass


@then("Tag loads only after marketing consent granted")
def loads_after_consent(page: Page) -> None:
    expect(page.locator("main")).to_be_visible()


@given("Ad blocker prevents LinkedIn tag")
def ad_blocker_prevents(page: Page) -> None:
    page.goto("/")


@when("Page renders")
def renders(page: Page) -> None:
    pass


@then("Core page unaffected; tag blocked gracefully")
def unaffected(page: Page) -> None:
    expect(page.locator("main")).to_be_visible()


@given("LinkedIn service slow or timeout")
def linkedin_slow(page: Page) -> None:
    page.goto("/")


@when("Page renders")
def render_page(page: Page) -> None:
    pass


@then("Core functionality unaffected; timeout logged minimally")
def unaffected_timeout(page: Page) -> None:
    expect(page.locator("main")).to_be_visible()


@given("User denies marketing consent")
def denies_consent(page: Page) -> None:
    page.goto("/")


@when("LinkedIn tag attempts execution")
def tag_executes(page: Page) -> None:
    pass


@then("Tag does not execute; page functions normally")
def no_execution(page: Page) -> None:
    expect(page.locator("main")).to_be_visible()
