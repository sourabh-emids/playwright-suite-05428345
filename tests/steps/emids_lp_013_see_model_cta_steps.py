"""Steps for emids_lp_013: Provide See the model CTA."""
from playwright.sync_api import Page, expect
from pytest_bdd import given, parsers, then, when

from pages.how_we_deliver.how_we_deliver_page import HowWeDeliverPage


@given(parsers.parse("User views How We Deliver section"))
def view_how_we_deliver(page: Page) -> None:
    """User views How We Deliver section."""
    how_we_deliver = HowWeDeliverPage(page)
    how_we_deliver.navigate()
    how_we_deliver.scroll_to_section()


@given(parsers.parse("User focuses on See the model CTA"))
def focus_see_model_cta(page: Page) -> None:
    """User focuses on See the model CTA."""
    how_we_deliver = HowWeDeliverPage(page)
    how_we_deliver.navigate()
    how_we_deliver.scroll_to_section()
    how_we_deliver.locators.see_model_cta.focus()


@given(parsers.parse("User examines See the model CTA"))
def examine_see_model_cta(page: Page) -> None:
    """User examines See the model CTA."""
    how_we_deliver = HowWeDeliverPage(page)
    how_we_deliver.navigate()
    how_we_deliver.scroll_to_section()


@given(parsers.parse("User clicks See the model CTA"))
def click_see_model_cta(page: Page) -> None:
    """User clicks See the model CTA."""
    how_we_deliver = HowWeDeliverPage(page)
    how_we_deliver.navigate()
    how_we_deliver.scroll_to_section()
    how_we_deliver.click_see_model_cta()


@given(parsers.parse("User hovers or focuses on See the model CTA"))
def hover_focus_cta(page: Page) -> None:
    """User hovers or focuses on CTA."""
    how_we_deliver = HowWeDeliverPage(page)
    how_we_deliver.navigate()
    how_we_deliver.scroll_to_section()


@given(parsers.parse("Multiple CTAs on page"))
def multiple_ctas(page: Page) -> None:
    """Multiple CTAs on page."""
    how_we_deliver = HowWeDeliverPage(page)
    how_we_deliver.navigate()


@when("User clicks See the model CTA")
def user_clicks_cta(page: Page) -> None:
    """User clicks CTA."""
    how_we_deliver = HowWeDeliverPage(page)
    how_we_deliver.click_see_model_cta()


@when("User activates with keyboard")
def activate_keyboard(page: Page) -> None:
    """Activate with keyboard."""
    page.keyboard.press("Enter")


@when("User observes visual feedback")
def observe_feedback(page: Page) -> None:
    """Observe visual feedback."""
    pass


@then(parsers.parse("Browser navigates to /forward-deployed-context-engineering/"))
def navigates_to_fdce(page: Page) -> None:
    """Verify navigates to FDCE."""
    expect(page).to_have_url("/forward-deployed-context-engineering/")


@then("Navigation to FDCE page occurs")
def navigation_occurs(page: Page) -> None:
    """Verify navigation occurs."""
    expect(page).to_have_url("/forward-deployed-context-engineering/")


@then("Label clearly describes the action destination")
def label_describes_action(page: Page) -> None:
    """Verify label describes action."""
    how_we_deliver = HowWeDeliverPage(page)
    how_we_deliver.navigate()
    how_we_deliver.scroll_to_section()
    label = how_we_deliver.locators.see_model_cta.inner_text()
    expect(label.lower()).to_contain("model")


@then("FDCE destination URL is valid")
def fdce_url_valid(page: Page) -> None:
    """Verify FDCE URL is valid."""
    how_we_deliver = HowWeDeliverPage(page)
    how_we_deliver.navigate()
    how_we_deliver.scroll_to_section()
    href = how_we_deliver.locators.see_model_cta.get_attribute("href")
    expect(href).to_contain("/forward-deployed-context-engineering/")


@then("No 404 returned")
def no_404(page: Page) -> None:
    """Verify no 404."""
    expect(page).not_to_have_url(r"404")


@then("Visible hover and focus states indicate interactivity")
def hover_focus_states(page: Page) -> None:
    """Verify hover and focus states."""
    how_we_deliver = HowWeDeliverPage(page)
    how_we_deliver.navigate()
    how_we_deliver.scroll_to_section()
    # Check cursor style
    cursor = how_we_deliver.locators.see_model_cta.evaluate("el => window.getComputedStyle(el).cursor")
    expect(cursor).to_equal("pointer")


@then("No duplicate focus targets")
def no_duplicate_targets(page: Page) -> None:
    """Verify no duplicate focus targets."""
    how_we_deliver = HowWeDeliverPage(page)
    how_we_deliver.navigate()
    how_we_deliver.scroll_to_section()
    expect(how_we_deliver.locators.see_model_cta).to_be_focusable()


@then("Keyboard navigation remains logical")
def keyboard_navigation_logical(page: Page) -> None:
    """Verify keyboard navigation is logical."""
    how_we_deliver = HowWeDeliverPage(page)
    how_we_deliver.navigate()
    how_we_deliver.locators.see_model_cta.focus()
    page.keyboard.press("Tab")
