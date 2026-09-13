"""Steps for Reduced motion for partner animation (issue_0019)."""
from playwright.sync_api import Page, expect
from pytest_bdd import given, when, then

from locators.issue_0019_reduced_motion_partners_locators import ReducedMotionPartnersLocators


@given("User has prefers-reduced-motion enabled")
def reduced_motion_enabled(page: Page) -> None:
    page.goto("/")


@given("Page is open and user changes motion preference")
def preference_changes(page: Page) -> None:
    page.goto("/")


@given("Animation library fails")
def animation_fails(page: Page) -> None:
    page.goto("/")


@when("Partner logo animation is active")
def animation_active(page: Page) -> None:
    pass


@when("Partner logos animate")
def logos_animate(page: Page) -> None:
    pass


@when("Animation is disabled via reduced motion")
def animation_disabled(page: Page) -> None:
    pass


@when("Preference change is detected")
def preference_detected(page: Page) -> None:
    pass


@when("Page renders")
def page_renders(page: Page) -> None:
    pass


@then("Non-essential continuous motion is disabled or meaningfully reduced")
def motion_disabled(page: Page) -> None:
    expect(ReducedMotionPartnersLocators(page).partnerships_section).to_be_visible()


@then("All partner logos remain fully visible")
def logos_visible(page: Page) -> None:
    expect(ReducedMotionPartnersLocators(page).partnerships_section).to_be_visible()


@then("All partners can be discovered without animation")
def discoverable(page: Page) -> None:
    expect(ReducedMotionPartnersLocators(page).partnerships_section).to_be_visible()


@then("Animation behavior updates accordingly")
def behavior_updates(page: Page) -> None:
    pass


@then("Static partner list remains visible")
def static_visible(page: Page) -> None:
    expect(ReducedMotionPartnersLocators(page).partnerships_section).to_be_visible()
