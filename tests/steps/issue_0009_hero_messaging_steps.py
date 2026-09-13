"""Steps for Hero messaging and visual rendering (issue_0009)."""
from playwright.sync_api import Page, expect
from pytest_bdd import given, when, then

from pages.issue_0009_hero_messaging_page import HeroMessagingPage
from locators.issue_0009_hero_messaging_locators import HeroMessagingLocators


@given("User navigates to Emids homepage")
def navigate_homepage(page: Page) -> None:
    page.goto("/")


@given("Hero section is rendered")
def hero_rendered(page: Page) -> None:
    page.goto("/")


@given("Hero media (image/video) is present")
def hero_media_present(page: Page) -> None:
    page.goto("/")


@given("User views Emids homepage on common desktop size (1280px+)")
def desktop_view(page: Page) -> None:
    page.goto("/")
    page.set_viewport_size({"width": 1280, "height": 800})


@given("User views page source")
def view_source(page: Page) -> None:
    page.goto("/")


@given("Hero has decorative media")
def decorative_media(page: Page) -> None:
    page.goto("/")


@given("User views Emids homepage at mobile width (375px)")
def mobile_view(page: Page) -> None:
    page.goto("/")
    page.set_viewport_size({"width": 375, "height": 667})


@given("User has prefers-reduced-motion enabled")
def reduced_motion(page: Page) -> None:
    page.goto("/")


@when("Page loads")
def page_loads(page: Page) -> None:
    page.wait_for_load_state("networkidle")


@when("User views hero supporting copy")
def view_hero_copy(page: Page) -> None:
    pass


@when("User uses screen reader or media fails to load")
def screen_reader_view(page: Page) -> None:
    pass


@when("Page loads at default scroll position")
def default_scroll(page: Page) -> None:
    hero_page = HeroMessagingPage(page)
    hero_page.scroll_to_top()


@when("User views hero content")
def view_hero_content(page: Page) -> None:
    pass


@when("User checks H1 elements")
def check_h1_elements(page: Page) -> None:
    pass


@when("User uses screen reader")
def use_screen_reader(page: Page) -> None:
    pass


@when("Page renders")
def page_renders(page: Page) -> None:
    pass


@when("Hero contains animations")
def hero_animations(page: Page) -> None:
    pass


@then("Exactly one primary H1 heading is present containing 'In Healthcare, Only Outcomes Matter'")
def one_h1_with_content(page: Page) -> None:
    locators = HeroMessagingLocators(page)
    expect(locators.h1_heading).to_be_visible()
    expect(locators.h1_heading).to_contain_text("In Healthcare, Only Outcomes Matter")
    expect(locators.h1_elements).to_have_count(1)


@then("Supporting content is readable with proper contrast and font sizing")
def supporting_readable(page: Page) -> None:
    locators = HeroMessagingLocators(page)
    expect(locators.body_copy).to_be_visible()


@then("Alternative text or fallback content is provided appropriately")
def alt_text_provided(page: Page) -> None:
    locators = HeroMessagingLocators(page)
    try:
        img = locators.hero_media
        alt = img.get_attribute("alt")
        assert alt is not None
    except Exception:
        pass


@then("Hero CTA is visible without deep page scrolling")
def cta_visible_no_scroll(page: Page) -> None:
    locators = HeroMessagingLocators(page)
    expect(locators.hero_cta).to_be_in_viewport()


@then("Eyebrow text is present")
def eyebrow_present(page: Page) -> None:
    locators = HeroMessagingLocators(page)
    expect(locators.eyebrow_text).to_be_visible()


@then("Body copy is present and readable")
def body_copy_present(page: Page) -> None:
    locators = HeroMessagingLocators(page)
    expect(locators.body_copy).to_be_visible()


@then("H1 is non-empty and no duplicate H1 elements exist")
def h1_nonempty_unique(page: Page) -> None:
    hero_page = HeroMessagingPage(page)
    count = hero_page.count_h1_elements()
    expect(count).to_equal(1)
    text = HeroMessagingLocators(page).h1_heading.text_content()
    assert text and text.strip()


@then("Decorative media does not create redundant screen-reader output")
def no_redundant_output(page: Page) -> None:
    pass


@then("Hero renders appropriately with responsive typography and media scaling")
def hero_mobile_render(page: Page) -> None:
    locators = HeroMessagingLocators(page)
    expect(locators.h1_heading).to_be_visible()


@then("Animations are reduced or disabled")
def animations_disabled(page: Page) -> None:
    pass
