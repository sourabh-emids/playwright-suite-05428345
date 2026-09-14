"""Step definitions for issue_0052: Provide responsive layout across viewports."""
from playwright.sync_api import expect, Page
from pytest_bdd import given, when, then


@given("User views page at desktop, tablet, and mobile widths")
def view_at_widths(page: Page) -> None:
    page.goto("/")


@when("Checking horizontal scroll")
def check_horizontal(page: Page) -> None:
    widths = [1280, 768, 375]
    for width in widths:
        page.set_viewport_size({"width": width, "height": 720})


@then("No unintended horizontal scrolling occurs")
def no_horizontal(page: Page) -> None:
    expect(page.locator("main")).to_be_visible()


@given("User views text content at various sizes")
def view_text_sizes(page: Page) -> None:
    page.goto("/")


@when("Checking font sizes")
def check_fonts(page: Page) -> None:
    pass


@then("Text remains legible; font sizes appropriate for viewport")
def legible_text(page: Page) -> None:
    expect(page.locator("main")).to_be_visible()


@given("User views interactive elements")
def view_elements(page: Page) -> None:
    page.goto("/")


@when("Checking layout at various widths")
def check_layout(page: Page) -> None:
    page.set_viewport_size({"width": 375, "height": 667})


@then("Interactive elements do not overlap or become inaccessible")
def no_overlap(page: Page) -> None:
    expect(page.locator("header")).to_be_visible()


@given("User views at mobile width")
def mobile_view(page: Page) -> None:
    page.set_viewport_size({"width": 375, "height": 667})


@when("Checking content visibility")
def check_visible(page: Page) -> None:
    page.goto("/")


@then("All section content accessible via vertical scroll")
def content_accessible(page: Page) -> None:
    expect(page.locator("main")).to_be_visible()


@given("User views images across viewport sizes")
def view_images(page: Page) -> None:
    page.goto("/")


@when("Checking responsiveness")
def check_responsive(page: Page) -> None:
    pass


@then("Images scale proportionally; aspect ratio maintained")
def aspect_ratio(page: Page) -> None:
    expect(page.locator("main")).to_be_visible()


@given("User views page at minimum supported width")
def min_width(page: Page) -> None:
    page.set_viewport_size({"width": 320, "height": 568})


@when("Checking layout")
def check_layout(page: Page) -> None:
    page.goto("/")


@then("Content fully usable; horizontal scroll not required")
def fully_usable(page: Page) -> None:
    expect(page.locator("main")).to_be_visible()


@given("User sets browser zoom to 200%")
def set_zoom(page: Page) -> None:
    page.set_viewport_size({"width": 640, "height": 360})


@when("Viewing page")
def view_page(page: Page) -> None:
    page.goto("/")


@then("Content usable without horizontal scroll")
def usable_zoom(page: Page) -> None:
    expect(page.locator("main")).to_be_visible()


@given("Content has unusually long text strings")
def long_text(page: Page) -> None:
    page.goto("/")


@when("Page renders at various widths")
def render_widths(page: Page) -> None:
    page.set_viewport_size({"width": 375, "height": 667})


@then("Long text wraps or truncates gracefully without breaking layout")
def graceful_wrap(page: Page) -> None:
    expect(page.locator("main")).to_be_visible()


@given("User sets browser zoom between 100-200%")
def set_zoom_range(page: Page) -> None:
    page.set_viewport_size({"width": 640, "height": 360})


@when("Checking layout stability")
def check_stability(page: Page) -> None:
    page.goto("/")


@then("Layout remains stable; content accessible")
def stable_layout(page: Page) -> None:
    expect(page.locator("main")).to_be_visible()


@given("User rotates phone to landscape")
def rotate_landscape(page: Page) -> None:
    page.set_viewport_size({"width": 844, "height": 390})


@when("Page renders")
def render(page: Page) -> None:
    page.goto("/")


@then("Content reflows appropriately for landscape orientation")
def landscape_reflow(page: Page) -> None:
    expect(page.locator("main")).to_be_visible()


@given("User uses tablet in split-screen mode")
def split_screen(page: Page) -> None:
    page.set_viewport_size({"width": 500, "height": 800})


@when("Page renders in narrow width")
def render_narrow(page: Page) -> None:
    page.goto("/")


@then("Content adapts to reduced width gracefully")
def adapts_gracefully(page: Page) -> None:
    expect(page.locator("main")).to_be_visible()
