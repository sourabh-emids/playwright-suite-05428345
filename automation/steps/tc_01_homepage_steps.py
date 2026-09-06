from pytest_bdd import given, scenarios, then, when

scenarios("../features/tc_01_homepage.feature")


@given("the user has a supported browser and an active internet connection")
def supported_browser() -> None:
    """The Playwright page fixture supplies the supported browser."""


@when("the user opens the Emids homepage")
def open_homepage(emids_page) -> None:
    emids_page.open_home()


@then("the homepage is displayed without a visible error or broken layout")
def verify_homepage(emids_page) -> None:
    emids_page.assert_homepage_loaded()
