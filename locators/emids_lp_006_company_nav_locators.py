"""Locators for emids_lp_006: Implement Company navigation group."""
from playwright.sync_api import Locator, Page


class CompanyNavLocators:
    """Company navigation locators."""

    def __init__(self, page: Page):
        self.page = page

    @property
    def company_nav(self) -> Locator:
        """Company navigation item in header."""
        return self.page.get_by_role("link", name="Company")

    @property
    def company_button(self) -> Locator:
        """Company button for mega-menu trigger."""
        return self.page.get_by_role("button", name="Company")

    @property
    def company_menu(self) -> Locator:
        """Company menu container."""
        return self.page.locator('[aria-label="Company menu"], [role="menu"]').first

    @property
    def about_us(self) -> Locator:
        """About Us group label."""
        return self.page.get_by_text("About Us")

    @property
    def connect_with_us(self) -> Locator:
        """Connect with Us group label."""
        return self.page.get_by_text("Connect with Us")

    @property
    def our_story_link(self) -> Locator:
        """Our Story link."""
        return self.page.get_by_role("link", name="Our Story")

    @property
    def leadership_team_link(self) -> Locator:
        """Leadership Team link."""
        return self.page.get_by_role("link", name="Leadership Team")

    @property
    def partners_link(self) -> Locator:
        """Partners link."""
        return self.page.get_by_role("link", name="Partners")

    @property
    def careers_link(self) -> Locator:
        """Careers link."""
        return self.page.get_by_role("link", name="Careers")

    @property
    def offices_link(self) -> Locator:
        """Offices link."""
        return self.page.get_by_role("link", name="Offices")

    @property
    def contact_us_link(self) -> Locator:
        """Contact Us link."""
        return self.page.get_by_role("link", name="Contact Us")

    def get_about_links(self) -> list[Locator]:
        """Get About Us group links."""
        return [
            self.our_story_link,
            self.leadership_team_link,
            self.partners_link,
            self.careers_link,
        ]

    def get_connect_links(self) -> list[Locator]:
        """Get Connect with Us group links."""
        return [self.offices_link, self.contact_us_link]

    def get_all_links(self) -> list[Locator]:
        """Get all links."""
        return self.get_about_links() + self.get_connect_links()
