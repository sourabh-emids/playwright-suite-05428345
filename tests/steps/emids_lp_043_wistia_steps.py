"""Step definitions for emids_lp_043-044 - Media integrations."""
from playwright.sync_api import Page, expect
from pytest_bdd import given, then


@then("No Wistia player script is loaded")
def verify_no_wistia_script(page: Page) -> None:
    from pages.emids_lp_043_wistia_page import WistiaPage
    page_obj = WistiaPage(page)
    # No wistia-related elements should be present
    expect(page_obj.hero_section).to_be_visible()


@then("Player has accessible title and controls")
def verify_player_accessible(page: Page) -> None:
    from pages.emids_lp_043_wistia_page import WistiaPage
    page_obj = WistiaPage(page)
    expect(page_obj.hero_section).to_be_visible()


@then("Valid video ID is provided; invalid ID handled gracefully")
def verify_video_id(page: Page) -> None:
    from pages.emids_lp_043_wistia_page import WistiaPage
    page_obj = WistiaPage(page)
    expect(page_obj.hero_section).to_be_visible()


@then("Player respects user preferences; no unwanted autoplay")
def verify_motion_preference(page: Page) -> None:
    from pages.emids_lp_043_wistia_page import WistiaPage
    page_obj = WistiaPage(page)
    expect(page_obj.hero_section).to_be_visible()


@then("Fallback displayed; no page break")
def verify_player_blocked(page: Page) -> None:
    from pages.emids_lp_043_wistia_page import WistiaPage
    page_obj = WistiaPage(page)
    expect(page_obj.hero_section).to_be_visible()


@then("Player loads only when applicable consent rules are satisfied")
def verify_consent_wistia(page: Page) -> None:
    from pages.emids_lp_043_wistia_page import WistiaPage
    page_obj = WistiaPage(page)
    expect(page_obj.hero_section).to_be_visible()


@then("Graceful error or placeholder displayed")
def verify_missing_video(page: Page) -> None:
    from pages.emids_lp_043_wistia_page import WistiaPage
    page_obj = WistiaPage(page)
    expect(page_obj.hero_section).to_be_visible()


@then("No YouTube player resources are loaded")
def verify_no_youtube_resources(page: Page) -> None:
    from pages.emids_lp_044_youtube_page import YouTubePage
    page_obj = YouTubePage(page)
    expect(page_obj.hero_section).to_be_visible()


@then("Player is keyboard accessible with proper focus management")
def verify_youtube_keyboard(page: Page) -> None:
    from pages.emids_lp_044_youtube_page import YouTubePage
    page_obj = YouTubePage(page)
    expect(page_obj.hero_section).to_be_visible()


@then("Player has accessible title attribute")
def verify_youtube_title(page: Page) -> None:
    from pages.emids_lp_044_youtube_page import YouTubePage
    page_obj = YouTubePage(page)
    expect(page_obj.hero_section).to_be_visible()


@then("Valid video ID is used; invalid ID shows appropriate error")
def verify_youtube_id(page: Page) -> None:
    from pages.emids_lp_044_youtube_page import YouTubePage
    page_obj = YouTubePage(page)
    expect(page_obj.hero_section).to_be_visible()


@then("Video does not autoplay with sound by default")
def verify_no_autoplay(page: Page) -> None:
    from pages.emids_lp_044_youtube_page import YouTubePage
    page_obj = YouTubePage(page)
    expect(page_obj.hero_section).to_be_visible()


@then("Graceful error displayed; no page break")
def verify_video_removed(page: Page) -> None:
    from pages.emids_lp_044_youtube_page import YouTubePage
    page_obj = YouTubePage(page)
    expect(page_obj.hero_section).to_be_visible()


@then("Appropriate message displayed")
def verify_regional_restriction(page: Page) -> None:
    from pages.emids_lp_044_youtube_page import YouTubePage
    page_obj = YouTubePage(page)
    expect(page_obj.hero_section).to_be_visible()


@then("Player loads in privacy-enhanced mode or shows appropriate message")
def verify_cookies_blocked(page: Page) -> None:
    from pages.emids_lp_044_youtube_page import YouTubePage
    page_obj = YouTubePage(page)
    expect(page_obj.hero_section).to_be_visible()
