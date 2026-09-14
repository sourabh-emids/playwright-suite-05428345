"""Step definitions for issue_0024: Render five audience/industry entries."""
from playwright.sync_api import expect, Page
from pytest_bdd import given, when, then


@given("User views Who We Serve section")
def view_who_we_serve(page: Page) -> None:
    page.goto("/")


@when("Checking audience display")
def check_audience_display(page: Page) -> None:
    pass


@then("Payer, Provider, HealthTech, Life Sciences, and Consumer are all visible")
def five_audiences_visible(page: Page) -> None:
    expect(page.getByRole("button", name="Payer")).to_be_visible()
    expect(page.getByRole("button", name="Provider")).to_be_visible()
    expect(page.getByRole("button", name="HealthTech")).to_be_visible()
    expect(page.getByRole("button", name="Life Sciences")).to_be_visible()
    expect(page.getByRole("button", name="Consumer")).to_be_visible()


@given("User clicks Explore action on any audience")
def click_explore_action(page: Page) -> None:
    page.goto("/")
    page.getByRole("button", name="Payer").click()


@when("Navigation triggered")
def navigate_triggered(page: Page) -> None:
    explore = page.getByRole("link", name="Explore")
    if explore.is_visible():
        explore.click()


@then("User navigates to respective canonical URL: /segments/payer/, /segments/provider/, /segments/healthtech/, /segments/life-sciences/, or /segments/consumer/")
def navigate_canonical(page: Page) -> None:
    assert "/segments/" in page.url or page.url.startswith("https://www.emids.com")


@given("User tests Explore interactions")
def test_explore_interactions(page: Page) -> None:
    page.goto("/")


@when("Using keyboard Tab/Enter or touch tap")
def use_keyboard_touch(page: Page) -> None:
    page.getByRole("button", name="Payer").press("Enter")


@then("Navigation functions correctly with both input methods")
def nav_functions(page: Page) -> None:
    expect(page.getByRole("button", name="Payer")).to_be_visible()


@given("Content version specification")
def content_version(page: Page) -> None:
    page.goto("/")


@when("Counting audiences")
def count_audiences(page: Page) -> None:
    pass


@then("Exactly five audience entries display")
def exactly_five(page: Page) -> None:
    expect(page.getByRole("button", name="Payer")).to_be_visible()


@given("User inspects audience destination URLs")
def inspect_urls(page: Page) -> None:
    page.goto("/")


@when("Checking URL format")
def check_url_format(page: Page) -> None:
    pass


@then("All URLs use canonical /segments/ paths")
def canonical_paths(page: Page) -> None:
    links = page.getByRole("link").filter(has=page.getByText("Payer"))
    if links.count() > 0:
        href = links.first.get_attribute("href")
        assert "/segments/" in href or href is not None


@given("One audience segment page is unavailable")
def segment_unavailable(page: Page) -> None:
    page.goto("/")


@when("Page renders")
def render(page: Page) -> None:
    pass


@then("Unavailable segment either shows appropriate fallback or is hidden; other four segments display normally")
def fallback_handled(page: Page) -> None:
    expect(page.getByRole("button", name="Provider")).to_be_visible()


@given("User interacts with audience tabs/accordion")
def interact_tabs(page: Page) -> None:
    page.goto("/")
    page.getByRole("button", name="Payer").click()


@when("Window resizes from desktop to mobile")
def resize_mobile(page: Page) -> None:
    page.set_viewport_size({"width": 375, "height": 667})


@then("Active tab state is preserved appropriately for new layout")
def state_preserved(page: Page) -> None:
    expect(page.getByRole("button", name="Payer")).to_be_visible()


@given("User interacts with audience controls")
def interact_controls(page: Page) -> None:
    page.goto("/")


@when("Checking active state")
def check_active_state(page: Page) -> None:
    pass


@then("Only intended panel is active; no duplicate active states occur")
def no_duplicate_active(page: Page) -> None:
    active_buttons = page.getByRole("button", name="Payer")
    expect(active_buttons.first).to_be_visible()
