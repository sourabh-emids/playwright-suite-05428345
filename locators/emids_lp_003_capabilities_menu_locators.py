"""Locators for emids_lp_003: Implement Capabilities mega-menu."""
from playwright.sync_api import Locator, Page


class CapabilitiesMenuLocators:
    """Capabilities mega-menu locators."""

    def __init__(self, page: Page):
        self.page = page

    @property
    def capabilities_nav(self) -> Locator:
        """Capabilities navigation item in header."""
        return self.page.get_by_role("link", name="Capabilities")

    @property
    def capabilities_button(self) -> Locator:
        """Capabilities button for mega-menu trigger."""
        return self.page.get_by_role("button", name="Capabilities")

    @property
    def capabilities_menu(self) -> Locator:
        """Capabilities mega-menu container."""
        return self.page.locator('[aria-label="Capabilities menu"], [role="menu"]').first

    @property
    def ai_group(self) -> Locator:
        """AI capability group label."""
        return self.page.get_by_text("AI", exact=True)

    @property
    def engineering_group(self) -> Locator:
        """Engineering capability group label."""
        return self.page.get_by_text("Engineering", exact=True)

    @property
    def platforms_group(self) -> Locator:
        """Platforms capability group label."""
        return self.page.get_by_text("Platforms", exact=True)

    @property
    def data_engineering_link(self) -> Locator:
        """Data Engineering link."""
        return self.page.get_by_role("link", name="Data Engineering")

    @property
    def automation_link(self) -> Locator:
        """Automation link."""
        return self.page.get_by_role("link", name="Automation")

    @property
    def pacca_ai_link(self) -> Locator:
        """Pacca AI link."""
        return self.page.get_by_role("link", name="Pacca AI")

    @property
    def digital_engineering_link(self) -> Locator:
        """Digital Engineering link."""
        return self.page.get_by_role("link", name="Digital Engineering")

    @property
    def low_code_link(self) -> Locator:
        """Low Code link."""
        return self.page.get_by_role("link", name="Low Code")

    @property
    def user_experience_link(self) -> Locator:
        """User Experience link."""
        return self.page.get_by_role("link", name="User Experience")

    @property
    def cloud_transformation_cap_link(self) -> Locator:
        """Cloud Transformation capability link."""
        return self.page.get_by_role("link", name="Cloud Transformation")

    @property
    def payer_core_platforms_link(self) -> Locator:
        """Payer Core Platforms link."""
        return self.page.get_by_role("link", name="Payer Core Platforms")

    @property
    def provider_platforms_link(self) -> Locator:
        """Provider Platforms link."""
        return self.page.get_by_role("link", name="Provider Platforms")

    def get_ai_links(self) -> list[Locator]:
        """Get AI group links."""
        return [self.data_engineering_link, self.automation_link, self.pacca_ai_link]

    def get_engineering_links(self) -> list[Locator]:
        """Get Engineering group links."""
        return [
            self.digital_engineering_link,
            self.low_code_link,
            self.user_experience_link,
            self.cloud_transformation_cap_link,
        ]

    def get_platforms_links(self) -> list[Locator]:
        """Get Platforms group links."""
        return [self.payer_core_platforms_link, self.provider_platforms_link]
