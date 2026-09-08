import pytest
from playwright.sync_api import Page
from pytest_bdd import given, parsers, then, when

from pages.tc_03_primary_ctas_page import Tc03PrimaryCtasPage


@pytest.fixture
def tc_03_ctas(page: Page) -> Tc03PrimaryCtasPage:
    return Tc03PrimaryCtasPage(page)


@given("the Emids homepage primary calls to action are available")
def open_homepage(tc_03_ctas: Tc03PrimaryCtasPage) -> None:
    tc_03_ctas.open()


@when(
    parsers.parse(
        'I select the "{call_to_action}" primary call to action'
    )
)
def select_call_to_action(
    tc_03_ctas: Tc03PrimaryCtasPage,
    call_to_action: str,
) -> None:
    tc_03_ctas.select_primary_call_to_action(call_to_action)


@then(
    parsers.parse(
        'its assigned destination "{path}" loads without a visible error'
    )
)
def verify_call_to_action_destination(
    tc_03_ctas: Tc03PrimaryCtasPage,
    path: str,
) -> None:
    tc_03_ctas.assert_destination_loaded(path)
