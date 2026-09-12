"""Test for issue_0011: Solutions menu items have valid URLs."""
import pytest
from playwright.sync_api import Page


@pytest.fixture
def page_ready(page: Page) -> Page:
    """Navigate to homepage with cookies accepted."""
    page.goto("/")
    try:
        page.get_by_role("button", name="Allow all").click()
    except Exception:
        pass
    return page


def test_solutions_menu_items_valid_urls(page_ready: Page) -> None:
    """Test all Solutions menu items have valid URLs."""
    page_ready.get_by_role("button", name="Solutions").first.click()
    
    expected_urls = [
        "/solutions/modernization-as-a-service/",
        "/solutions/interoperability/",
        "/solutions/cloud-migration-solutions/",
        "/solutions/agentic-ai/",
        "/solutions/global-capability-center/",
    ]
    
    for url_path in expected_urls:
        link_text = url_path.split("/")[2].replace("-", " ").replace("as a service", "").title().strip()
        link = page_ready.get_by_role("link", name=link_text)
        href = link.get_attribute("href")
        assert href is not None, f"Link should have href"
        assert url_path in href or f"https://www.emids.com{url_path}" in href, f"Link should point to {url_path}"
