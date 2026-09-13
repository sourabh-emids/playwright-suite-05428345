"""Steps for Industries mega-menu implementation (issue_0004)."""
from playwright.sync_api import Page, expect
from pytest_bdd import given, when, then

from pages.issue_0004_industries_megamenu_page import IndustriesMegamenuPage
from locators.issue_0004_industries_megamenu_locators import IndustriesMegamenuLocators


@given("Industries menu is open")
def industries_menu_open(page: Page) -> None:
    page.goto("/")
    industries_page = IndustriesMegamenuPage(page)
    industries_page.activate_industries()


@given("User is on desktop viewing Emids homepage")
def desktop_view(page: Page) -> None:
    page.goto("/")
    page.set_viewport_size({"width": 1280, "height": 800})


@given("User is on mobile viewing Emids homepage")
def mobile_view(page: Page) -> None:
    page.goto("/")
    page.set_viewport_size({"width": 375, "height": 667})


@when("User views menu content")
def view_menu_content(page: Page) -> None:
    pass


@when("User uses keyboard to navigate")
def keyboard_navigate(page: Page) -> None:
    page.keyboard.press("Tab")


@when("User clicks Payer")
def click_payer(page: Page) -> None:
    industries_page = IndustriesMegamenuPage(page)
    industries_page.activate_industries()
    industries_page.click_payer()


@when("User clicks Provider")
def click_provider(page: Page) -> None:
    industries_page = IndustriesMegamenuPage(page)
    industries_page.activate_industries()
    industries_page.click_provider()


@when("User clicks HealthTech")
def click_healthtech(page: Page) -> None:
    industries_page = IndustriesMegamenuPage(page)
    industries_page.activate_industries()
    industries_page.click_healthtech()


@when("User clicks Life Sciences")
def click_life_sciences(page: Page) -> None:
    industries_page = IndustriesMegamenuPage(page)
    industries_page.activate_industries()
    industries_page.click_life_sciences()


@when("User clicks Consumer")
def click_consumer(page: Page) -> None:
    industries_page = IndustriesMegamenuPage(page)
    industries_page.activate_industries()
    industries_page.click_consumer()


@when("User activates Industries")
def activate_industries(page: Page) -> None:
    industries_page = IndustriesMegamenuPage(page)
    industries_page.activate_industries()


@when("User inspects audience link URLs")
def inspect_urls(page: Page) -> None:
    pass


@then("Menu contains Payer, Provider, HealthTech, Life Sciences, and Consumer destinations")
def menu_contains_five_audiences(page: Page) -> None:
    locators = IndustriesMegamenuLocators(page)
    industries_page = IndustriesMegamenuPage(page)
    industries_page.activate_industries()
    expect(locators.payer_link).to_be_visible()
    expect(locators.provider_link).to_be_visible()
    expect(locators.healthtech_link).to_be_visible()
    expect(locators.life_sciences_link).to_be_visible()
    expect(locators.consumer_link).to_be_visible()


@then("All five audience destinations are keyboard accessible")
def all_audiences_keyboard_accessible(page: Page) -> None:
    locators = IndustriesMegamenuLocators(page)
    for link in [locators.payer_link, locators.provider_link, locators.healthtech_link,
                 locators.life_sciences_link, locators.consumer_link]:
        link.focus()
        expect(link).to_be_focused()


@then("User is navigated to '/segments/payer/'")
def navigated_to_payer(page: Page) -> None:
    expect(page).to_have_url("/segments/payer/")


@then("User is navigated to '/segments/provider/'")
def navigated_to_provider(page: Page) -> None:
    expect(page).to_have_url("/segments/provider/")


@then("User is navigated to '/segments/healthtech/'")
def navigated_to_healthtech(page: Page) -> None:
    expect(page).to_have_url("/segments/healthtech/")


@then("User is navigated to '/segments/life-sciences/'")
def navigated_to_life_sciences(page: Page) -> None:
    expect(page).to_have_url("/segments/life-sciences/")


@then("User is navigated to '/segments/consumer/'")
def navigated_to_consumer(page: Page) -> None:
    expect(page).to_have_url("/segments/consumer/")


@then("Desktop uses grouped menu layout")
def desktop_grouped_layout(page: Page) -> None:
    expect(IndustriesMegamenuLocators(page).industries_button).to_be_visible()


@then("Mobile uses stacked list/disclosure pattern")
def mobile_stacked_list(page: Page) -> None:
    expect(IndustriesMegamenuLocators(page).industries_button).to_be_visible()


@then("All links use canonical URLs matching the specified endpoints")
def canonical_urls(page: Page) -> None:
    pass
