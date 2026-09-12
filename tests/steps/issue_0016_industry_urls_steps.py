"""Step definitions for issue_0016: Industry links use canonical URLs."""
from pytest_bdd import given, then
from playwright.sync_api import Page


@given("I have navigated to the homepage")
def navigate_to_homepage(page: Page) -> None:
    """Navigate to the homepage."""
    page.goto("/")
    try:
        page.get_by_role("button", name="Allow all").click()
    except Exception:
        pass


@then("industry links use canonical HTTPS URLs")
def industry_links_use_https(page: Page) -> None:
    """Verify industry links use canonical HTTPS URLs."""
    page.get_by_role("button", name="Industries").first.click()
    
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
        link = page.get_by_role("link", name=audience)
        href = link.get_attribute("href")
        assert href is not None, f"Link for {audience} should have href"
        assert href.startswith("https://"), f"Link should use HTTPS: {href}"
        assert path in href or full_url in href, f"Link should point to {path}"
