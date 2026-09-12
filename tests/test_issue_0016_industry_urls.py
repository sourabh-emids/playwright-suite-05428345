"""Test for issue_0016: Industry links use canonical URLs."""
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


def test_industry_links_use_https(page_ready: Page) -> None:
    """Test industry links use canonical HTTPS URLs."""
    page_ready.get_by_role("button", name="Industries").first.click()
    
    expected_paths = [
        "/segments/payer/",
        "/segments/provider/",
        "/segments/healthtech/",
        "/segments/life-sciences/",
        "/segments/consumer/",
    ]
    
    for path in expected_paths:
        full_url = f"https://www.emids.com{path}"
        audience = path.split("/")[2].replace("-", " ").title()
        link = page_ready.get_by_role("link", name=audience)
        href = link.get_attribute("href")
        assert href is not None, f"Link for {audience} should have href"
        assert href.startswith("https://"), f"Link should use HTTPS: {href}"
        assert path in href or full_url in href, f"Link should point to {path}"
