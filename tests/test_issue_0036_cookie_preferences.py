"""Test for issue_0036 - Cookie Preferences control visibility in footer."""
import pytest

from pages.issue_0036_cookie_preferences_page import Issue0036CookiePreferencesPage


@pytest.fixture
def cookie_preferences_page(page) -> Issue0036CookiePreferencesPage:
    """Create page object for issue_0036 tests."""
    return Issue0036CookiePreferencesPage(page)
