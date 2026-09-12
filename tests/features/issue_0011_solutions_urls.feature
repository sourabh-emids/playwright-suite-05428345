"""Solutions menu items have valid URLs."""
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


@then("all Solutions menu items have valid URLs")
def solutions_menu_items_valid_urls(page: Page) -> None:
    """Verify all Solutions menu items have valid URLs."""
    page.get_by_role("button", name="Solutions").first.click()
    
    expected_urls = [
        "/solutions/modernization-as-a-service/",
        "/solutions/interoperability/",
        "/solutions/cloud-migration-solutions/",
        "/solutions/agentic-ai/",
        "/solutions/global-capability-center/",
        "/solutions/segment/payer/",
        "/solutions/segment/provider/",
        "/solutions/segment/healthtech/",
        "/solutions/segment/life-sciences/",
    ]
    
    for url_path in expected_urls:
        full_url = f"https://www.emids.com{url_path}"
        link = page.get_by_role("link", name=url_path.split("/")[2].replace("-", " ").title()).first
        href = link.get_attribute("href")
        assert href is not None, f"Link should have href"
        assert url_path in href or full_url in href, f"Link should point to {url_path}"
