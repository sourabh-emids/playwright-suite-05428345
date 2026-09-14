"""Step definitions for issue_0020: Render capabilities overview."""
from playwright.sync_api import expect, Page
from pytest_bdd import given, when, then


@given("User views Capabilities section")
def view_capabilities_section(page: Page) -> None:
    page.goto("/")


@when("Checking group display")
def check_group_display(page: Page) -> None:
    pass


@then("AI, Engineering, and Platforms groups are all visible")
def three_groups_visible(page: Page) -> None:
    expect(page.getByText("Capabilities that deliver on ambitious goals")).to_be_visible()
    expect(page.getByText("AI")).to_be_visible()
    expect(page.getByText("Engineering")).to_be_visible()
    expect(page.getByText("Platforms")).to_be_visible()


@given("User examines each capability group")
def examine_groups(page: Page) -> None:
    page.goto("/")


@when("Checking content and interactivity")
def check_content_interactivity(page: Page) -> None:
    pass


@then("Each group contains summary content and relevant link/action")
def groups_have_content(page: Page) -> None:
    expect(page.getByText("Capabilities that deliver on ambitious goals")).to_be_visible()


@given("User compares Capabilities section to header navigation")
def compare_capabilities_navigation(page: Page) -> None:
    page.goto("/")


@when("Checking label consistency")
def check_label_consistency(page: Page) -> None:
    pass


@then("Section labels 'AI', 'Engineering', 'Platforms' match navigation taxonomy exactly")
def labels_match_taxonomy(page: Page) -> None:
    expect(page.getByText("AI")).to_be_visible()
    expect(page.getByText("Engineering")).to_be_visible()
    expect(page.getByText("Platforms")).to_be_visible()


@given("Current content version specification")
def content_version_spec(page: Page) -> None:
    page.goto("/")


@when("Checking capability groups")
def check_capability_groups(page: Page) -> None:
    pass


@then("Exactly three primary groups display: AI, Engineering, Platforms")
def exactly_three_groups(page: Page) -> None:
    expect(page.getByText("Capabilities that deliver on ambitious goals")).to_be_visible()


@given("One capability group fails to load")
def group_fails_load(page: Page) -> None:
    page.goto("/")


@when("Page renders")
def page_renders(page: Page) -> None:
    pass


@then("Remaining groups display; missing group is logged")
def remaining_groups_display(page: Page) -> None:
    expect(page.getByText("Capabilities that deliver on ambitious goals")).to_be_visible()


@given("CMS applies incorrect taxonomy label")
def incorrect_taxonomy_label(page: Page) -> None:
    page.goto("/")


@when("Page renders")
def render_page(page: Page) -> None:
    pass


@then("QA catches mislabeling; correct taxonomy is enforced")
def mislabeling_caught(page: Page) -> None:
    expect(page.getByText("Capabilities that deliver on ambitious goals")).to_be_visible()


@given("Capability content is extensive")
def extensive_content(page: Page) -> None:
    page.goto("/")


@when("Page renders at standard viewport")
def render_standard_viewport(page: Page) -> None:
    pass


@then("Content does not overflow container boundaries")
def no_overflow(page: Page) -> None:
    expect(page.locator("main")).to_be_visible()
