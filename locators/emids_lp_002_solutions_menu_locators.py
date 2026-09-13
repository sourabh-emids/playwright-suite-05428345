"""Locators for emids_lp_002: Implement Solutions mega-menu."""
from playwright.sync_api import Locator, Page


class SolutionsMenuLocators:
    """Solutions mega-menu locators."""

    def __init__(self, page: Page):
        self.page = page

    @property
    def solutions_nav(self) -> Locator:
        """Solutions navigation item in header."""
        return self.page.get_by_role("link", name="Solutions")

    @property
    def solutions_button(self) -> Locator:
        """Solutions button for mega-menu trigger."""
        return self.page.get_by_role("button", name="Solutions")

    @property
    def solutions_menu(self) -> Locator:
        """Solutions mega-menu container."""
        return self.page.locator('[aria-label="Solutions menu"], [role="menu"]').first

    @property
    def solutions_by_initiative(self) -> Locator:
        """Solutions by Initiative group."""
        return self.page.get_by_text("Solutions by Initiative")

    @property
    def browse_by_industry(self) -> Locator:
        """Browse By Industry group."""
        return self.page.get_by_text("Browse By Industry")

    @property
    def the_portfolio(self) -> Locator:
        """The Portfolio group."""
        return self.page.get_by_text("The Portfolio")

    @property
    def modernization_link(self) -> Locator:
        """Modernization solution link."""
        return self.page.get_by_role("link", name="Modernization Modernization that turns fragile legacy systems into cloud-native platforms, domain by domain.")

    @property
    def interoperability_link(self) -> Locator:
        """Interoperability solution link."""
        return self.page.get_by_role("link", name="Interoperability Interoperability that turns siloed clinical data into connected, CMS-compliant systems.")

    @property
    def cloud_transformation_link(self) -> Locator:
        """Cloud Transformation solution link."""
        return self.page.get_by_role("link", name="Cloud Transformation Cloud assessment, migration, and operations, built for PHI security and cost control.")

    @property
    def agentic_ai_link(self) -> Locator:
        """Agentic AI solution link."""
        return self.page.get_by_role("link", name="Agentic AI AI agents for prior authorization, claims, and clinical review, governed end to end.")

    @property
    def global_capability_center_link(self) -> Locator:
        """Global Capability Center solution link."""
        return self.page.get_by_role("link", name="Global Capability Center Full-lifecycle Global Capability Center for healthcare and life sciences enterprises.")

    @property
    def explore_all_solutions_link(self) -> Locator:
        """Explore all solutions link."""
        return self.page.get_by_role("link", name="Solutions")

    def get_all_solution_links(self) -> list[Locator]:
        """Get all solution links in the menu."""
        return [
            self.modernization_link,
            self.interoperability_link,
            self.cloud_transformation_link,
            self.agentic_ai_link,
            self.global_capability_center_link,
        ]
