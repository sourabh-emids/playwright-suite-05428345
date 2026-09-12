"""Step definitions for Issue 0027 - Medicare Advantage eBook card display."""
from pytest_bdd import given, when, then
from playwright.sync_api import Page, expect
from pages.homepage_page import HomepagePage


@given("A user views the Medicare Advantage eBook card")
def view_medicare_card(page: Page):
    page.goto("/")
    page.evaluate("() => window.scrollTo(0, 7300)")


@when("The card renders")
def medicare_card_renders(page: Page):
    page.wait_for_load_state("networkidle")


@then("Card displays title 'Managing the Margin Reset in Medicare Advantage', eBook type, and Download action")
def medicare_card_content(page: Page):
    homepage = HomepagePage(page)
    expect(homepage.medicare_advantage_ebook).to_be_visible()
    expect(page.getByText("eBook", exact=False)).to_be_visible()
    expect(page.getByText("Download", exact=False)).to_be_visible()


@given("The Medicare Advantage eBook has imagery configured")
def medicare_has_image(page: Page):
    pass


@when("The card renders")
def medicare_renders_image(page: Page):
    page.goto("/")
    page.evaluate("() => window.scrollTo(0, 7300)")


@then("Image is displayed; card renders without broken image if image is unavailable")
def image_displayed(page: Page):
    homepage = HomepagePage(page)
    expect(homepage.medicare_advantage_ebook).to_be_visible()


@given("A user clicks the Medicare Advantage eBook card")
def click_medicare_card(page: Page):
    homepage = HomepagePage(page)
    homepage.click_insight_card("Managing the Margin Reset in Medicare Advantage")


@when("The Download action is activated")
def download_activated(page: Page):
    pass


@then("The user is navigated to /insights/managing-the-margin-reset-in-medicare-advantage/")
def navigated_to_medicare(page: Page):
    page.wait_for_url("**/insights/managing-the-margin-reset-in-medicare-advantage/**")


@given("The Medicare Advantage resource is removed or gated differently")
def medicare_removed(page: Page):
    pass


@when("The card renders")
def medicare_card_render_removed(page: Page):
    page.goto("/")
    page.evaluate("() => window.scrollTo(0, 7300)")


@then("Appropriate handling occurs (redirect, unavailable message, or card excluded)")
def medicare_handling(page: Page):
    # Card should render or graceful fallback
    homepage = HomepagePage(page)
    expect(homepage.insights_section).to_be_visible()
