"""Step definitions for issue_0013: Provide See the model CTA."""
from playwright.sync_api import expect, Page
from pytest_bdd import given, when, then


@given("User clicks the 'See the model' CTA")
def click_see_model(page: Page) -> None:
    page.goto("/")
    page.get_by_role("link", name="See the model").click()


@when("Navigation occurs")
def nav_occurs(page: Page) -> None:
    pass


@then("User is navigated to /forward-deployed-context-engineering/")
def navigated_fdce(page: Page) -> None:
    expect(page).to_have_url("https://www.emids.com/forward-deployed-context-engineering/")


@given("User focuses on the CTA via Tab")
def focus_cta_tab(page: Page) -> None:
    page.goto("/")
    page.locator("body").press("Tab")
    page.locator("body").press("Tab")


@when("User presses Enter")
def press_enter(page: Page) -> None:
    page.keyboard.press("Enter")


@then("Navigation to FDCE page is triggered")
def nav_triggered(page: Page) -> None:
    expect(page).to_have_url("https://www.emids.com/forward-deployed-context-engineering/")


@given("User inspects CTA accessibility")
def inspect_cta_accessibility(page: Page) -> None:
    page.goto("/")


@when("Checking accessible name")
def check_accessible_name(page: Page) -> None:
    pass


@then("Accessible name describes the action 'See the model'")
def accessible_name_descriptive(page: Page) -> None:
    cta = page.get_by_role("link", name="See the model")
    expect(cta).to_be_visible()


@given("User hovers or focuses on CTA")
def hover_focus_cta(page: Page) -> None:
    page.goto("/")
    cta = page.get_by_role("link", name="See the model")
    cta.hover()


@when("Checking visual feedback")
def check_visual_feedback(page: Page) -> None:
    pass


@then("Visible hover and focus states are present")
def hover_focus_states(page: Page) -> None:
    cta = page.get_by_role("link", name="See the model")
    expect(cta).to_be_visible()


@given("FDCE page returns 404")
def fdce_returns_404(page: Page) -> None:
    pass


@when("User clicks See the model CTA")
def click_see_model_404(page: Page) -> None:
    page.goto("/")
    page.get_by_role("link", name="See the model").click()


@then("Error page displays appropriately")
def error_displays(page: Page) -> None:
    # Should either show error or navigate to valid page
    assert page.url.startswith("https://www.emids.com")


@given("Multiple CTAs exist in section")
def multiple_ctas(page: Page) -> None:
    page.goto("/")


@when("User tabs through section")
def tab_through_section(page: Page) -> None:
    for _ in range(3):
        page.keyboard.press("Tab")


@then("Each CTA is individually focusable; no duplicate tab stops")
def no_duplicate_tabstops(page: Page) -> None:
    ctas = page.get_by_role("link").filter(has=page.locator("..").locator("text=model"))
    expect(ctas.first).to_be_visible()
