"""Step definitions for Issue 0029 - Life Sciences transformation eBook card."""
from pytest_bdd import given, when, then
from playwright.sync_api import Page, expect
from pages.homepage_page import HomepagePage


@given("A user views the Life Sciences transformation eBook card")
def view_ls_ebook(page: Page):
    page.goto("/")
    page.evaluate("() => window.scrollTo(0, 7300)")


@when("The card renders")
def ls_ebook_renders(page: Page):
    page.wait_for_load_state("networkidle")


@then("Card displays 'Unlocking Trusted Digital Transformation in Life Sciences' with eBook type and Download action")
def ls_ebook_content(page: Page):
    homepage = HomepagePage(page)
    expect(homepage.life_sciences_ebook).to_be_visible()
    expect(page.getByText("eBook", exact=False)).to_be_visible()
    expect(page.getByText("Download", exact=False)).to_be_visible()


@given("A user clicks the Download action on the Life Sciences eBook card")
def click_ls_download(page: Page):
    homepage = HomepagePage(page)
    homepage.click_insight_card("Unlocking Trusted Digital Transformation in Life Sciences")


@when("The action is activated")
def ls_activated(page: Page):
    pass


@then("User is navigated to /insights/unlocking-trusted-digital-transformation-in-life-sciences/")
def ls_navigates(page: Page):
    page.wait_for_url("**/insights/unlocking-trusted-digital-transformation-in-life-sciences/**")


@given("A user examines the Life Sciences eBook card URL")
def examine_ls_url(page: Page):
    page.goto("/")
    page.evaluate("() => window.scrollTo(0, 7300)")


@when("The URL is analyzed")
def ls_url_analyzed(page: Page):
    pass


@then("The URL is canonical to the current detail page")
def ls_url_canonical(page: Page):
    homepage = HomepagePage(page)
    href = homepage.life_sciences_ebook.get_attribute("href")
    assert href.endswith("/unlocking-trusted-digital-transformation-in-life-sciences/")
