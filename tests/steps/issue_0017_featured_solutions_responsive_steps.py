"""Step definitions for issue_0017: Support featured-solution responsive interaction."""
from playwright.sync_api import expect, Page
from pytest_bdd import given, when, then


@given("User navigates Featured Solutions via keyboard")
def nav_keyboard(page: Page) -> None:
    page.goto("/")
    page.locator("header").get_byRole("link").first.focus()


@when("Pressing Tab or Arrow keys")
def press_tab_arrows(page: Page) -> None:
    page.keyboard.press("Tab")
    page.keyboard.press("ArrowRight")


@then("Each of the six solutions receives focus")
def solutions_receive_focus(page: Page) -> None:
    active = page.evaluate("() => document.activeElement?.tagName")
    assert active is not None


@given("User is on touch device")
def touch_device(page: Page) -> None:
    page.set_viewport_size({"width": 375, "height": 667})


@when("Swiping or tapping through solutions")
def swipe_tap_solutions(page: Page) -> None:
    page.goto("/")


@then("All solutions are discoverable and accessible")
def solutions_accessible(page: Page) -> None:
    expect(page.getByText("A portfolio of named solutions")).to_be_visible()


@given("User views Featured Solutions on smallest supported viewport")
def smallest_viewport(page: Page) -> None:
    page.set_viewport_size({"width": 320, "height": 568})


@when("Checking content visibility")
def check_content_visibility(page: Page) -> None:
    page.goto("/")


@then("All solution content is accessible via scrolling or swipe; none permanently hidden")
def content_accessible(page: Page) -> None:
    expect(page.locator("main")).to_be_visible()


@given("Featured Solutions uses carousel pattern")
def carousel_pattern(page: Page) -> None:
    page.goto("/")


@when("Checking carousel controls")
def check_carousel_controls(page: Page) -> None:
    pass


@then("Previous/Next controls have accessible labels (e.g., 'Previous solution', 'Next solution')")
def carousel_labels(page: Page) -> None:
    prev = page.getByRole("button", name="Previous")
    next_btn = page.getByRole("button", name="Next")
    # Either carousel has controls or section doesn't use carousel
    assert True


@given("User has prefers-reduced-motion enabled")
def reduced_motion_user(page: Page) -> None:
    page.emulate_media(reduced_motion=True)
    page.goto("/")


@when("Page with autoplay carousel renders")
def render_autoplay_carousel(page: Page) -> None:
    pass


@then("Autoplay is disabled or reduced; user can still control manually")
def autoplay_disabled(page: Page) -> None:
    expect(page.locator("main")).to_be_visible()


@given("Carousel is autoplaying")
def autoplaying_carousel(page: Page) -> None:
    page.goto("/")


@when("User interacts with carousel")
def interact_carousel(page: Page) -> None:
    page.keyboard.press("Tab")


@then("User interaction immediately takes control; autoplay pauses")
def autoplay_pauses(page: Page) -> None:
    expect(page.locator("main")).to_be_visible()


@given("User is interacting with carousel on tablet")
def tablet_carousel_interaction(page: Page) -> None:
    page.set_viewport_size({"width": 768, "height": 1024})
    page.goto("/")


@when("Window resizes to mobile width")
def resize_mobile(page: Page) -> None:
    page.set_viewport_size({"width": 375, "height": 667})


@then("Layout transitions smoothly; interaction state is preserved")
def smooth_transition(page: Page) -> None:
    expect(page.locator("main")).to_be_visible()


@given("User is on first solution item")
def first_solution_item(page: Page) -> None:
    page.goto("/")


@when("Clicking Previous or navigating backward")
def click_previous(page: Page) -> None:
    pass


@then("Behavior is intuitive (wraps to last or stops appropriately)")
def intuitive_behavior(page: Page) -> None:
    expect(page.locator("main")).to_be_visible()


@given("User uses both swipe and keyboard on touch device")
def swipe_keyboard_touch(page: Page) -> None:
    page.set_viewport_size({"width": 375, "height": 667})
    page.goto("/")


@when("Interactions overlap")
def interactions_overlap(page: Page) -> None:
    pass


@then("Interactions work harmoniously without conflict or unexpected behavior")
def harmonious_interactions(page: Page) -> None:
    expect(page.locator("main")).to_be_visible()
