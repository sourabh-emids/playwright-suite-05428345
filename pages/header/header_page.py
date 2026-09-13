"""Page object for emids_lp_001: Render global header and Emids brand."""
from playwright.sync_api import Page, expect
from locators.emids_lp_001_header_locators import HeaderLocators


class HeaderPage:
    """Header section page object."""

    def __init__(self, page: Page):
        self.page = page
        self.locators = HeaderLocators(page)

    @property
    def url(self) -> str:
        """Homepage URL."""
        return "/"

    def navigate(self) -> None:
        """Navigate to the homepage."""
        self.page.goto("/")

    def click_emids_logo(self) -> None:
        """Click the Emids logo to navigate to homepage."""
        self.locators.emids_logo.click()

    def click_connect_cta(self) -> None:
        """Click the Connect CTA in header."""
        self.locators.connect_cta.click()

    def click_navigation_item(self, nav_item: str) -> None:
        """Click a navigation item by name."""
        nav_item_lower = nav_item.lower()
        if nav_item_lower == "solutions":
            self.locators.solutions_nav.click()
        elif nav_item_lower == "capabilities":
            self.locators.capabilities_nav.click()
        elif nav_item_lower == "industries":
            self.locators.industries_nav.click()
        elif nav_item_lower == "insights":
            self.locators.insights_nav.click()
        elif nav_item_lower == "company":
            self.locators.company_nav.click()
        else:
            raise ValueError(f"Unknown navigation item: {nav_item}")

    def get_navigation_items(self) -> list[str]:
        """Get list of primary navigation item names."""
        return ["Solutions", "Capabilities", "Industries", "Insights", "Company"]

    def is_header_visible(self) -> bool:
        """Check if header is visible at top of viewport."""
        header = self.locators.header_banner
        return header.is_visible()

    def is_emids_logo_present(self) -> bool:
        """Check if Emids logo/brand link is present."""
        return self.locators.emids_logo.is_visible()

    def is_navigation_item_visible(self, item_name: str) -> bool:
        """Check if a navigation item is visible."""
        nav_item_lower = item_name.lower()
        if nav_item_lower == "solutions":
            return self.locators.solutions_nav.is_visible()
        elif nav_item_lower == "capabilities":
            return self.locators.capabilities_nav.is_visible()
        elif nav_item_lower == "industries":
            return self.locators.industries_nav.is_visible()
        elif nav_item_lower == "insights":
            return self.locators.insights_nav.is_visible()
        elif nav_item_lower == "company":
            return self.locators.company_nav.is_visible()
        return False

    def is_connect_cta_visible(self) -> bool:
        """Check if Connect CTA is prominently displayed."""
        return self.locators.connect_cta.is_visible()

    def count_connect_ctas(self) -> int:
        """Count number of Connect CTAs in header."""
        return self.locators.connect_cta.count()
