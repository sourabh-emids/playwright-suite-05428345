"""Step definitions for issue_0014 - Semantic heading hierarchy and landmarks."""
from pytest_bdd import given, then, when

from pages.issue_0014_semantic_page import Issue0014SemanticPage


@given("I navigate to the homepage")
def navigate_to_homepage(page: Issue0014SemanticPage):
    """Navigate to the homepage."""
    page.page.goto("/")


@when("I view the page")
def view_page(page: Issue0014SemanticPage):
    """View the page."""
    pass


@then("the heading hierarchy should follow logical order")
def heading_hierarchy_logical(page: Issue0014SemanticPage):
    """Verify heading hierarchy follows logical order."""
    page.heading_hierarchy_follows_logical_order()


@then("there should be a single H1")
def single_h1(page: Issue0014SemanticPage):
    """Verify there is exactly one H1."""
    page.there_should_be_single_h1()


@then("H2 headings should be used for section titles")
def h2_for_sections(page: Issue0014SemanticPage):
    """Verify H2 is used for section titles."""
    page.h2_should_be_used_for_sections()


@then("H3 headings should be used for subsection titles")
def h3_for_subsections(page: Issue0014SemanticPage):
    """Verify H3 is used for subsection titles."""
    page.h3_should_be_used_for_subsections()


@then("there should be a header landmark")
def header_landmark_exists(page: Issue0014SemanticPage):
    """Verify header landmark exists."""
    page.header_landmark_should_exist()


@then("there should be a main landmark")
def main_landmark_exists(page: Issue0014SemanticPage):
    """Verify main landmark exists."""
    page.main_landmark_should_exist()


@then("there should be a footer landmark")
def footer_landmark_exists(page: Issue0014SemanticPage):
    """Verify footer landmark exists."""
    page.footer_landmark_should_exist()
