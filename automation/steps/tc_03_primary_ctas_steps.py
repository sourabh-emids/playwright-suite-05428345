from pytest_bdd import given, parsers, scenarios, then, when

scenarios("../features/tc_03_primary_ctas.feature")


@given("the Emids homepage is displayed")
def homepage(emids_page) -> None:
    emids_page.open_home()
    emids_page.assert_homepage_loaded()


@when(
    parsers.parse(
        'the user selects the primary "{action}" call to action'
    )
)
def select_primary_cta(emids_page, action: str) -> None:
    emids_page.select_primary_cta(action)


@then(
    parsers.parse(
        '"{path}" is displayed with the heading "{heading}"'
    )
)
def verify_cta_destination(
    emids_page, path: str, heading: str
) -> None:
    emids_page.assert_destination(path, heading)
