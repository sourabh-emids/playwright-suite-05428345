"""Page object for issue_0018 - Partner logo rail rendering and accessibility."""
from playwright.sync_api import Page, expect

from locators.issue_0018_partner_logo_rail_locators import Issue0018PartnerLogoRailLocators


class Issue0018PartnerLogoRailPage:
    """Page object for Partner logo rail."""

    def __init__(self, page: Page):
        self.page = page
        self.locators = Issue0018PartnerLogoRailLocators()
        self.locators.page = page

    def view_partnerships_section(self) -> None:
        """Scroll to the Partnerships section."""
        self.locators.partnerships_section.scroll_into_view_if_needed()

    def partner_logos_should_be_visible(self) -> None:
        """Verify partner logos are visible."""
        expect(self.locators.partner_logos.first).to_be_visible()

    def logos_should_have_alt_text(self) -> None:
        """Verify logos have alt text for accessibility."""
        logos = self.locators.partner_logos
        count = logos.count()
        for i in range(count):
            logo = logos.nth(i)
            alt = await logo.get_attribute("alt")
            assert alt is not None and alt != "", f"Logo at index {i} missing alt text"
