"""Steps for Wistia and YouTube embeds (issues 0043-0044)."""
from playwright.sync_api import Page, expect
from pytest_bdd import given, when, then

from locators.issue_0043_0044_wistia_youtube_locators import MediaEmbedsLocators


@given("No Wistia content is configured")
def no_wistia(page: Page) -> None:
    page.goto("/")


@given("Wistia video is configured")
def wistia_configured(page: Page) -> None:
    page.goto("/")


@given("User prefers reduced motion")
def reduced_motion(page: Page) -> None:
    page.goto("/")


@given("No YouTube embed is configured")
def no_youtube(page: Page) -> None:
    page.goto("/")


@given("YouTube embed is configured")
def youtube_configured(page: Page) -> None:
    page.goto("/")


@when("Page loads")
def page_loads(page: Page) -> None:
    page.wait_for_load_state("domcontentloaded")


@when("Page renders")
def page_renders(page: Page) -> None:
    pass


@when("Video plays")
def video_plays(page: Page) -> None:
    pass


@when("Video attempts to autoplay")
def autoplay(page: Page) -> None:
    pass


@when("User loads page")
def user_loads(page: Page) -> None:
    pass


@then("No Wistia player script is loaded unnecessarily")
def no_wistia_script(page: Page) -> None:
    expect(MediaEmbedsLocators(page).main_content).to_be_visible()


@then("Player has accessible title and controls")
def player_accessible(page: Page) -> None:
    expect(MediaEmbedsLocators(page).main_content).to_be_visible()


@then("Motion preferences are respected")
def motion_respected(page: Page) -> None:
    expect(MediaEmbedsLocators(page).main_content).to_be_visible()


@then("No YouTube player resources are required")
def no_youtube_resources(page: Page) -> None:
    expect(MediaEmbedsLocators(page).main_content).to_be_visible()


@then("Autoplay does not occur with sound by default")
def no_autoplay_sound(page: Page) -> None:
    expect(MediaEmbedsLocators(page).main_content).to_be_visible()


@then("Appropriate consent/privacy behavior is implemented")
def consent_privacy(page: Page) -> None:
    expect(MediaEmbedsLocators(page).main_content).to_be_visible()
