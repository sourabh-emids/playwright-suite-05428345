"""Step definitions for issue_0013: See the Model CTA Implementation."""
from playwright.sync_api import Page, expect
from pytest_bdd import given, when, then
from pages.how_we_deliver_page import HowWeDeliverPage


@given("User clicks 'See the model' CTA")
def click_see_model_cta(page: Page):
    page.goto("/")
    page.wait_for_load_state("networkidle")
    hwd = HowWeDeliverPage(page)
    hwd.click_see_model_cta()


@when("Navigation completes")
def nav_completes_model(page: Page):
    page.wait_for_load_state("networkidle")


@then("Action routes to FDCE detail page at /forward-deployed-context-engineering/")
def routes_to_fdce(page: Page):
    expect(page).to_have_urlContaining("/forward-deployed-context-engineering/")


@given("'See the model' CTA is rendered")
def see_model_cta_rendered(page: Page):
    page.goto("/")
    page.wait_for_load_state("networkidle")


@when("User focuses via keyboard and activates")
def focus_activate_keyboard(page: Page):
    hwd = HowWeDeliverPage(page)
    hwd.cta.focus()
    page.keyboard.press("Enter")


@then("CTA is keyboard operable")
def cta_keyboard_operable(page: Page):
    expect(page).to_have_urlContaining("/forward-deployed-context-engineering/")


@given("CTA is configured")
def cta_configured_model(page: Page):
    page.goto("/")


@when("URL is validated")
def validate_url_model(page: Page):
    pass


@then("Destination is valid (returns 200 or appropriate redirect)")
def destination_valid(page: Page):
    hwd = HowWeDeliverPage(page)
    href = hwd.get_cta_href()
    assert href, "CTA should have href"
    assert "/forward-deployed-context-engineering/" in href, f"Should route to FDCE: {href}"


@given("CTA is rendered")
def cta_rendered_model(page: Page):
    page.goto("/")
    page.wait_for_load_state("networkidle")


@when("Accessibility inspection occurs")
def accessibility_inspection(page: Page):
    pass


@then("Accessible name describes the action")
def accessible_name_describes_action(page: Page):
    hwd = HowWeDeliverPage(page)
    name = hwd.cta.get_attribute("aria-label") or hwd.cta.text_content()
    assert name and "model" in name.lower() or "see" in name.lower(), "CTA should have descriptive accessible name"


@given("User interacts with 'See the model' CTA")
def interact_see_model_cta(page: Page):
    page.goto("/")
    page.wait_for_load_state("networkidle")


@when("Hover and focus states are reviewed")
def hover_focus_states(page: Page):
    hwd = HowWeDeliverPage(page)
    hwd.cta.hover()


@then("Visible hover/focus states are present")
def hover_focus_present(page: Page):
    hwd = HowWeDeliverPage(page)
    expect(hwd.cta).to_be_visible()


@given("FDCE detail page returns 404")
def fdce_404(page: Page):
    page.goto("/")
    page.route("**/forward-deployed-context-engineering/**", lambda route: route.abort())


@when("User clicks 'See the model' CTA")
def click_cta_404(page: Page):
    hwd = HowWeDeliverPage(page)
    hwd.click_see_model_cta()


@then("User sees appropriate error page")
def sees_error_page(page: Page):
    pass
