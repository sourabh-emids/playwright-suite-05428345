"""Locators for emids_lp_004: Implement Industries mega-menu."""
from playwright.sync_api import Locator, Page


class IndustriesMenuLocators:
    """Industries mega-menu locators."""

    def __init__(self, page: Page):
        self.page = page

    @property
    def industries_nav(self) -> Locator:
        """Industries navigation item in header."""
        return self.page.get_by_role("link", name="Industries")

    @property
    def industries_button(self) -> Locator:
        """Industries button for mega-menu trigger."""
        return self.page.get_by_role("button", name="Industries")

    @property
    def industries_menu(self) -> Locator:
        """Industries mega-menu container."""
        return self.page.locator('[aria-label="Industries menu"], [role="menu"]').first

    @property
    def payer_link(self) -> Locator:
        """Payer industry link."""
        return self.page.get_by_role("link", name__regex=r"^Payer", exact=False).first

    @property
    def provider_link(self) -> Locator:
        """Provider industry link."""
        return self.page.get_by_role("link", name__regex=r"^Providers", exact=False).first

    @property
    def healthtech_link(self) -> Locator:
        """HealthTech industry link."""
        return self.page.get_by_role("link", name__regex=r"^Health Tech", exact=False).first

    @property
    def life_sciences_link(self) -> Locator:
        """Life Sciences industry link."""
        return self.page.get_by_role("link", name__regex=r"^Life Sciences", exact=False).first

    @property
    def consumer_link(self) -> Locator:
        """Consumer industry link."""
        return self.page.get_by_role("link", name__regex=r"^Consumer", exact=False).first

    @property
    def payer_specific_link(self) -> Locator:
        """Payer industry link - specific selector."""
        return self.page.get_by_role("link", name="Payer Cost optimization, member engagement, interoperability, and value-based care for health plans.")

    @property
    def provider_specific_link(self) -> Locator:
        """Provider industry link - specific selector."""
        return self.page.get_by_role("link", name="Providers EHR optimization, cloud, AI, and care delivery for hospitals and health systems.")

    @property
    def healthtech_specific_link(self) -> Locator:
        """HealthTech industry link - specific selector."""
        return self.page.get_by_role("link", name="Health Tech Engineering, platform modernization, FHIR, and product scale for HealthTech companies.")

    @property
    def life_sciences_specific_link(self) -> Locator:
        """Life Sciences industry link - specific selector."""
        return self.page.get_by_role("link", name="Life Sciences AI, platform modernization, and regulatory compliance for pharma, biotech, and MedTech.")

    @property
    def consumer_specific_link(self) -> Locator:
        """Consumer industry link - specific selector."""
        return self.page.get_by_role("link", name="Consumer Experience design, digital engineering, agentic AI, and cloud delivery for consumer-facing brands.")

    def get_all_industry_links(self) -> list[Locator]:
        """Get all industry links."""
        return [
            self.payer_specific_link,
            self.provider_specific_link,
            self.healthtech_specific_link,
            self.life_sciences_specific_link,
            self.consumer_specific_link,
        ]
