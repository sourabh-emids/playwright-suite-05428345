"""Test for issue_0003 - Capabilities mega-menu accessibility."""
import pytest

from pages.issue_0003_capabilities_page import Issue0003CapabilitiesMenuPage


@pytest.fixture
def capabilities_menu_page(page) -> Issue0003CapabilitiesMenuPage:
    """Create page object for issue_0003 tests."""
    return Issue0003CapabilitiesMenuPage(page)
