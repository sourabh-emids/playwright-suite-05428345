from pytest_bdd import given, scenarios, then, when

scenarios("../features/tc_04_mobile_usability.feature")


@given("the Emids homepage is open in a mobile-sized viewport")
def mobile_homepage(emids_page) -> None:
    emids_page.use_mobile_viewport()
    emids_page.open_home()


@when("the user opens the mobile navigation menu")
def open_mobile_navigation(emids_page) -> None:
    emids_page.open_mobile_menu()


@then("the homepage text, logo, call to action, and mobile menu are usable")
def verify_mobile_homepage(emids_page) -> None:
    emids_page.assert_mobile_homepage_and_menu_usable()


@when("the user selects Connect from the mobile menu")
def select_mobile_connect(emids_page) -> None:
    emids_page.select_mobile_connect()


@then("the contact page opens without horizontal page overflow")
def verify_mobile_contact_page(emids_page) -> None:
    emids_page.assert_mobile_contact_page_usable()
