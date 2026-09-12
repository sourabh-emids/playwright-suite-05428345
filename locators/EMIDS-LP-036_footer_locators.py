"""Locators for Footer section - EMIDS-LP-036, EMIDS-LP-045, EMIDS-LP-046"""
from playwright.sync_api import Page, Locator


class FooterLocators:
    """Locators for Footer section elements."""

    def __init__(self, page: Page):
        self.page = page

    @property
    def footer(self) -> Locator:
        return self.page.get_by_role("contentinfo")

    @property
    def cookie_preferences(self) -> Locator:
        return self.footer.get_by_role("link", name="Cookie Preferences")

    @property
    def privacy_policy_link(self) -> Locator:
        return self.footer.get_by_role("link", name="Privacy Policy")

    @property
    def code_of_conduct_link(self) -> Locator:
        return self.footer.get_by_role("link", name="Code of Conduct")

    @property
    def transparency_in_coverage_link(self) -> Locator:
        return self.footer.get_by_role("link", name="Transparency in Coverage")

    @property
    def emids_logo(self) -> Locator:
        return self.footer.get_by_role("link", name="Emids logo")

    @property
    def legal_links(self) -> Locator:
        return self.footer.get_by_role("list").last.locator("a")

    @property
    def social_links(self) -> Locator:
        return self.footer.locator('a[href*="linkedin"], a[href*="twitter"], a[href*="facebook"]')
