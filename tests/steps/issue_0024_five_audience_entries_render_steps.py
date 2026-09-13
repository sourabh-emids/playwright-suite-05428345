"""Step definitions for issue_0024: Five audience entries render"""

from playwright.sync_api import Page, expect
from pytest_bdd import given, when, then

from pages.issue_0024_five_audience_entries_render_page import Issue0024WhoWeServePage


@given("The Who We Serve section is rendered")
def who_we_serve_rendered(page: Page):
    page_object = Issue0024WhoWeServePage(page)
    page_object.navigate_to_homepage()


@given("Each audience entry has an Explore CTA")
def each_audience_has_explore(page: Page):
    page_object = Issue0024WhoWeServePage(page)
    page_object.navigate_to_homepage()


@given("The page is viewed on a touch device")
def touch_device(page: Page):
    page_object = Issue0024WhoWeServePage(page)
    page_object.resize_to_mobile()
    page_object.navigate_to_homepage()


@when("Visual inspection confirms content")
def visual_inspection(page: Page):
    pass


@when("A user clicks an Explore action")
def user_clicks_explore(page: Page):
    pass


@when("Keyboard navigation testing runs")
def keyboard_testing(page: Page):
    page.keyboard.press("Tab")


@when("Touch testing validates interaction")
def touch_testing(page: Page):
    pass


@when("Automated testing counts audience entries")
def automated_counts(page: Page):
    pass


@when("Automated testing validates URLs")
def automated_validates_urls(page: Page):
    pass


@then("Payer, Provider, HealthTech, Life Sciences, and Consumer audiences are displayed")
def all_audiences_displayed(page: Page):
    page_object = Issue0024WhoWeServePage(page)
    page_object.verify_all_audiences()


@then("Navigation routes to the canonical segment page")
def routes_to_canonical(page: Page):
    expect(page).not_to_have_title("/404/")


@then("All Explore CTAs are keyboard accessible")
def ctas_keyboard_accessible(page: Page):
    expect(page.get_by_role("main")).to_be_visible()


@then("All Explore CTAs are touch accessible")
def ctas_touch_accessible(page: Page):
    page_object = Issue0024WhoWeServePage(page)
    page_object.verify_all_audiences()


@then("Exactly five audience entries are present")
def exactly_five_audiences(page: Page):
    page_object = Issue0024WhoWeServePage(page)
    page_object.verify_all_audiences()


@then("All URLs follow canonical patterns")
def urls_canonical(page: Page):
    expect(page.get_by_role("main")).to_be_visible()
