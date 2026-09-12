"""Locators for issue_0002 - Solutions mega-menu functionality."""
from playwright.sync_api import Locator


class Issue0002SolutionsMenuLocators:
    """Locators for Solutions mega-menu."""

    @property
    def solutions_nav_button(self) -> Locator:
        """Return the Solutions navigation button."""
        return self.page.locator('button:has-text("Solutions")')

    @property
    def solutions_mega_menu(self) -> Locator:
        """Return the Solutions mega-menu container."""
        return self.solutions_nav_button.locator("..").locator("..").locator("> :last-child")

    @property
    def solutions_by_initiative_header(self) -> Locator:
        """Return the 'Solutions by Initiative' header."""
        return self.page.locator("text=Solutions by Initiative")

    @property
    def modernization_link(self) -> Locator:
        """Return the Modernization solution link."""
        return self.page.get_by_role("link", name="Modernization")

    @property
    def interoperability_link(self) -> Locator:
        """Return the Interoperability solution link."""
        return self.page.get_by_role("link", name="Interoperability")

    @property
    def cloud_transformation_link(self) -> Locator:
        """Return the Cloud Transformation solution link."""
        return self.page.get_by_role("link", name="Cloud Transformation")

    @property
    def agentic_ai_link(self) -> Locator:
        """Return the Agentic AI solution link."""
        return self.page.get_by_role("link", name="Agentic AI")

    @property
    def global_capability_center_link(self) -> Locator:
        """Return the Global Capability Center solution link."""
        return self.page.get_by_role("link", name="Global Capability Center")

    @property
    def browse_by_industry_header(self) -> Locator:
        """Return the 'Browse By Industry' header."""
        return self.page.locator("text=Browse By Industry")

    @property
    def payers_link(self) -> Locator:
        """Return the Payers industry link."""
        return self.page.get_by_role("link", name="Payers")

    @property
    def providers_link(self) -> Locator:
        """Return the Providers industry link."""
        return self.page.get_by_role("link", name="Providers")

    @property
    def health_tech_link(self) -> Locator:
        """Return the Health Tech industry link."""
        return self.page.get_by_role("link", name="Health Tech")

    @property
    def life_sciences_link(self) -> Locator:
        """Return the Life Sciences industry link."""
        return self.page.get_by_role("link", name="Life Sciences")

    @property
    def the_portfolio_header(self) -> Locator:
        """Return the 'The Portfolio' header."""
        return self.page.locator("text=The Portfolio")

    @property
    def explore_all_solutions_link(self) -> Locator:
        """Return the 'Explore all solutions' link."""
        return self.page.get_by_role("link", name="Solutions")
