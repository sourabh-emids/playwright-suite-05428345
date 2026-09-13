"""Page object for emids_lp_006: Implement Company navigation group."""
from playwright.sync_api import Page, expect
from locators.emids_lp_006_company_nav_locators import CompanyNavLocators


class CompanyNavPage:
    """Company navigation page object."""

    def __init__(self, page: Page):
        self.page = page
        self.locators = CompanyNavLocators(page)

    @property
    def url(self) -> str:
        """Homepage URL."""
        return "/"

    def navigate(self) -> None:
        """Navigate to the homepage."""
        self.page.goto("/")

    def open_company_menu(self) -> None:
        """Open the Company menu."""
        self.locators.company_nav.click()
        self.page.wait_for_selector('[role="menu"]', state="visible", timeout=5000)

    def close_company_menu(self) -> None:
        """Close the Company menu."""
        self.page.keyboard.press("Escape")

    def are_groups_visible(self) -> bool:
        """Check if group labels are visible."""
        return (
            self.locators.about_us.is_visible()
            and self.locators.connect_with_us.is_visible()
        )

    def get_all_links(self) -> list:
        """Get all links."""
        return self.locators.get_all_links()

    def click_company_link(self, link_name: str) -> None:
        """Click a company link by name."""
        link_lower = link_name.lower()
        if "our story" in link_lower:
            self.locators.our_story_link.click()
        elif "leadership" in link_lower:
            self.locators.leadership_team_link.click()
        elif "partner" in link_lower:
            self.locators.partners_link.click()
        elif "career" in link_lower:
            self.locators.careers_link.click()
        elif "office" in link_lower:
            self.locators.offices_link.click()
        elif "contact" in link_lower:
            self.locators.contact_us_link.click()

    def verify_link_has_valid_href(self, link: "CompanyNavLocators") -> bool:
        """Verify link has a valid href."""
        href = link.get_attribute("href")
        return href and len(href) > 0 and not any(x in href for x in ["undefined", "null", "404"])
