"""Generic steps every feature file can use without its own steps file
redefining them -- kept here, not per-requirement, so the same "I navigate
to a path" or "I see some text" step isn't authored a dozen times over.
"""
from playwright.sync_api import Page, expect
from pytest_bdd import given, parsers, then


@given(parsers.parse('I navigate to "{path}"'))
def navigate_to_path(page: Page, path: str) -> None:
    page.goto(path)


@then(parsers.parse('I see "{text}"'))
def i_see_text(page: Page, text: str) -> None:
    expect(page.get_by_text(text)).to_be_visible()


@then(parsers.parse('the page title is "{title}"'))
def page_title_is(page: Page, title: str) -> None:
    expect(page).to_have_title(title)
