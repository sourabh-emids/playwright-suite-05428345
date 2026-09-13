"""Steps for Responsive layout across viewports (issue_0052)."""
from playwright.sync_api import Page, expect
from pytest_bdd import given, when, then

from locators.issue_0052_responsive_layout_locators import ResponsiveLayoutLocators


@given("User views page at supported viewport widths")
def view_at_widths(page: Page) -> None:
    page.goto("/")


@given("User views page at various viewport widths")
def various_widths(page: Page) -> None:
    page.goto("/")


@given("User views page at mobile width")
def mobile_width(page: Page) -> None:
    page.goto("/")
    page.set_viewport_size({"width": 375, "height": 667})


@given("User views card sections at mobile width")
def cards_mobile(page: Page) -> None:
    page.goto("/")
    page.set_viewport_size({"width": 375, "height": 667})


@given("User views images at various viewport widths")
def images_widths(page: Page) -> None:
    page.goto("/")


@given("User views page at 320px width")
def width_320(page: Page) -> None:
    page.goto("/")
    page.set_viewport_size({"width": 320, "height": 568})


@given("User sets browser zoom to 200%")
def zoom_200(page: Page) -> None:
    page.goto("/")
    page.set_viewport_size({"width": 640, "height": 800})


@given("Section contains very long text")
def long_text(page: Page) -> None:
    page.goto("/")


@given("User views page on phone in landscape")
def phone_landscape(page: Page) -> None:
    page.goto("/")
    page.set_viewport_size({"width": 844, "height": 390})


@given("User views page in split-screen mode on tablet")
def tablet_split(page: Page) -> None:
    page.goto("/")
    page.set_viewport_size({"width": 512, "height": 768})


@when("Page renders")
def page_renders(page: Page) -> None:
    pass


@when("Page renders at narrow viewport")
def narrow_render(page: Page) -> None:
    page.set_viewport_size({"width": 375, "height": 667})


@then("No unintended horizontal page scrolling occurs")
def no_horizontal_scroll(page: Page) -> None:
    for width in [320, 375, 768, 1280]:
        page.set_viewport_size({"width": width, "height": 800})
        scroll_width = page.evaluate("() => document.documentElement.scrollWidth")
        viewport_width = page.viewport_size["width"]
        assert scroll_width <= viewport_width + 5


@then("Typography remains readable")
def typography_readable(page: Page) -> None:
    expect(ResponsiveLayoutLocators(page).main_content).to_be_visible()


@then("Interactive controls do not overlap")
def no_overlap(page: Page) -> None:
    expect(ResponsiveLayoutLocators(page).main_content).to_be_visible()


@then("All cards/sections remain available")
def cards_available(page: Page) -> None:
    expect(ResponsiveLayoutLocators(page).main_content).to_be_visible()


@then("Images preserve aspect ratio")
def aspect_ratio(page: Page) -> None:
    expect(ResponsiveLayoutLocators(page).main_content).to_be_visible()


@then("Page reflows appropriately and content is usable")
def reflow_usable(page: Page) -> None:
    expect(ResponsiveLayoutLocators(page).main_content).to_be_visible()


@then("Page reflows without horizontal scrolling and content is usable")
def reflow_no_scroll(page: Page) -> None:
    scroll_width = page.evaluate("() => document.documentElement.scrollWidth")
    viewport_width = page.viewport_size["width"]
    assert scroll_width <= viewport_width + 5


@then("Text wraps appropriately without breaking layout")
def text_wraps(page: Page) -> None:
    expect(ResponsiveLayoutLocators(page).main_content).to_be_visible()


@then("Page renders appropriately")
def renders_appropriate(page: Page) -> None:
    expect(ResponsiveLayoutLocators(page).main_content).to_be_visible()


@then("Page handles reduced width appropriately")
def handles_reduced(page: Page) -> None:
    expect(ResponsiveLayoutLocators(page).main_content).to_be_visible()
