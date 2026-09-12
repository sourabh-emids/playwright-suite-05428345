"""Test for issue_0054 - Graceful handling of script failures."""
import pytest

from pages.issue_0054_script_failure_handling_page import Issue0054ScriptFailureHandlingPage


@pytest.fixture
def script_failure_handling_page(page) -> Issue0054ScriptFailureHandlingPage:
    """Create page object for issue_0054 tests."""
    return Issue0054ScriptFailureHandlingPage(page)
