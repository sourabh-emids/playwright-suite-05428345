from pytest_bdd import given, scenarios, then, when

scenarios("../features/tc_05_contact_validation.feature")


@given("the contact form is open with every required field empty")
def empty_contact_form(emids_page) -> None:
    emids_page.open_contact()
    emids_page.assert_required_fields_empty()


@when("the user submits the contact form")
def submit_empty_contact_form(emids_page) -> None:
    emids_page.submit_contact_form()


@then("the form remains open and every required field shows a clear message")
def verify_required_messages(emids_page) -> None:
    emids_page.assert_all_required_validation_messages()
