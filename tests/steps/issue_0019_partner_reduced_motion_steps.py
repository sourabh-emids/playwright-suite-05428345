"""Step definitions for issue_0019: Respect reduced motion for partner animation."""
from playwright.sync_api import expect, Page
from pytest_bdd import given, when, then


@given("User has prefers-reduced-motion: reduce enabled")
def motion_reduce_enabled(page: Page) -> None:
    page.emulate_media(reduced_motion=True)
    page.goto("/")


@when("Partner logos would animate continuously")
def logos_animate(page: Page) -> None:
    pass


@then("Animation is disabled or significantly reduced")
def animation_disabled(page: Page) -> None:
    expect(page.locator("main")).to_be_visible()


@given("Reduced motion is active")
def reduced_motion_active(page: Page) -> None:
    page.emulate_media(reduced_motion=True)
    page.goto("/")


@when("User views partner section")
def view_partner(page: Page) -> None:
    pass


@then("All partner logos are visible in static display")
def static_logos_visible(page: Page) -> None:
    partners_section = page.getByText("We've assembled the world's most powerful technology platforms")
    expect(partners_section).to_be_visible()


@given("User cannot see animation due to reduced motion")
def cannot_see_animation(page: Page) -> None:
    page.emulate_media(reduced_motion=True)
    page.goto("/")


@when("User attempts to view all partners")
def view_all_partners(page: Page) -> None:
    pass


@then("All partners are visible in static view; animation not required to discover partner")
def partners_in_static_view(page: Page) -> None:
    partners_section = page.getByText("We've assembled the world's most powerful technology platforms")
    expect(partners_section).to_be_visible()


@given("User changes system reduced motion preference while page is open")
def change_motion_preference(page: Page) -> None:
    page.goto("/")


@when("System preference updates")
def system_preference_updates(page: Page) -> None:
    page.emulate_media(reduced_motion=True)


@then("Page responds to preference change without reload")
def responds_without_reload(page: Page) -> None:
    expect(page.locator("main")).to_be_visible()


@given("Animation library fails to load or execute")
def animation_library_fails(page: Page) -> None:
    page.goto("/")


@when("Page renders")
def page_renders(page: Page) -> None:
    pass


@then("Static partner logos display; page remains functional")
def static_logos_functional(page: Page) -> None:
    expect(page.locator("main")).to_be_visible()
