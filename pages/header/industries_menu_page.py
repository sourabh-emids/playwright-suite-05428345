"""Page object for emids_lp_004: Implement Industries mega-menu."""
from playwright.sync_api import Page, expect
from locators.emids_lp_004_industries_menu_locators import IndustriesMenuLocators


class IndustriesMenuPage:
    """Industries mega-menu page object."""

    def __init__(self, page: Page):
        self.page = page
        self.locators = IndustriesMenuLocators(page)

    @property
    def url(self) -> str:
        """Homepage URL."""
        return "/"

    def navigate(self) -> None:
        """Navigate to the homepage."""
        self.page.goto("/")

    def open_industries_menu(self) -> None:
        """Open the Industries mega-menu."""
        self.locators.industries_nav.click()
        self.page.wait_for_selector('[role="menu"]', state="visible", timeout=5000)

    def get_expected_destinations(self) -> dict[str, str]:
        """Get expected canonical URLs for each industry."""
        return {
            "payer": "/segments/payer/",
            "provider": "/segments/provider/",
            "healthtech": "/segments/healthtech/",
            "life_sciences": "/segments/life-sciences/",
            "consumer": "/segments/consumer/",
        }

    def get_industry_urls(self) -> dict[str, str]:
        """Get URLs of all industry links."""
        urls = {}
        for link in self.locators.get_all_industry_links():
            name = link.get_attribute("href", "")
            if "payer" in name:
                urls["payer"] = name
            elif "provider" in name:
                urls["provider"] = name
            elif "healthtech" in name:
                urls["healthtech"] = name
            elif "life-sciences" in name:
                urls["life_sciences"] = name
            elif "consumer" in name:
                urls["consumer"] = name
        return urls

    def click_industry_link(self, industry: str) -> None:
        """Click an industry link by name."""
        industry_lower = industry.lower()
        if "payer" in industry_lower:
            self.locators.payer_specific_link.click()
        elif "provider" in industry_lower:
            self.locators.provider_specific_link.click()
        elif "healthtech" in industry_lower or "health tech" in industry_lower:
            self.locators.healthtech_specific_link.click()
        elif "life sciences" in industry_lower:
            self.locators.life_sciences_specific_link.click()
        elif "consumer" in industry_lower:
            self.locators.consumer_specific_link.click()

    def are_all_industries_visible(self) -> bool:
        """Check if all five industry destinations are visible."""
        for link in self.locators.get_all_industry_links():
            if not link.is_visible():
                return False
        return True
