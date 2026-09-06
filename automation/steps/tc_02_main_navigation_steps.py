from pytest_bdd import given, parsers, scenarios, then, when

scenarios("../features/tc_02_main_navigation.feature")


@given("the Emids homepage and main navigation are available")
def homepage_with_navigation(emids_page) -> None:
    emids_page.open_home()
    emids_page.assert_main_navigation_available()


@when(
    parsers.parse(
        'the user opens "{menu}" and selects "{destination}"'
    )
)
def select_main_navigation(
    emids_page, menu: str, destination: str
) -> None:
    emids_page.select_navigation_destination(menu, destination)


@then(
    parsers.parse(
        '"{path}" is displayed with the heading "{heading}"'
    )
)
def verify_navigation_destination(
    emids_page, path: str, heading: str
) -> None:
    emids_page.assert_destination(path, heading)
