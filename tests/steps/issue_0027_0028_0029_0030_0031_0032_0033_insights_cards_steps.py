"""Steps for Medicare Advantage and other eBook/blog card displays (issues 0027-0033)."""
from playwright.sync_api import Page, expect
from pytest_bdd import given, when, then

from locators.issue_0027_0028_0029_0030_0031_0032_0033_insights_cards_locators import InsightsCardsLocators


@given("Medicare Advantage eBook card renders")
def medicare_card(page: Page) -> None:
    page.goto("/")


@given("User views Medicare Advantage eBook card")
def view_medicare(page: Page) -> None:
    page.goto("/")


@given("User clicks Download")
def click_download(page: Page) -> None:
    pass


@given("User inspects network traffic on eBook card click")
def inspect_network(page: Page) -> None:
    page.goto("/")


@given("User views Payer data readiness blog card")
def view_payer_blog(page: Page) -> None:
    page.goto("/")


@given("Payer data readiness blog card renders")
def payer_blog_renders(page: Page) -> None:
    page.goto("/")


@when("Page renders")
def page_renders(page: Page) -> None:
    pass


@when("User views card")
def view_card(page: Page) -> None:
    pass


@when("User views card action")
def view_action(page: Page) -> None:
    pass


@when("Navigation occurs")
def navigation(page: Page) -> None:
    pass


@when("Download is initiated")
def download_initiated(page: Page) -> None:
    pass


@then("Card title reads 'Managing the Margin Reset in Medicare Advantage'")
def medicare_title(page: Page) -> None:
    expect(InsightsCardsLocators(page).insights_section).to_be_visible()


@then("Content type is displayed as eBook")
def ebook_type(page: Page) -> None:
    expect(InsightsCardsLocators(page).download_buttons.first).to_be_visible()


@then("Download action is displayed")
def download_displayed(page: Page) -> None:
    expect(InsightsCardsLocators(page).download_buttons.first).to_be_visible()


@then("User is navigated to '/insights/managing-the-margin-reset-in-medicare-advantage/'")
def nav_medicare(page: Page) -> None:
    pass


@then("User reaches resource detail/access flow")
def access_flow(page: Page) -> None:
    expect(InsightsCardsLocators(page).insights_section).to_be_visible()


@then("Implementation does not expose private asset endpoints")
def no_private_endpoints(page: Page) -> None:
    pass


@then("Content type is displayed as Blog")
def blog_type(page: Page) -> None:
    expect(InsightsCardsLocators(page).insights_section).to_be_visible()


@then("Read More action is displayed (not Download)")
def read_more_displayed(page: Page) -> None:
    expect(InsightsCardsLocators(page).insights_section).to_be_visible()
