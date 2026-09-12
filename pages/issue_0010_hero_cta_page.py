"""Page object for issue_0010 - Hero CTA routing to FDCE experience."""
from playwright.sync_api import Page, expect

from locators.issue_0010_hero_cta_locators import Issue0010HeroCTALocators


class Issue0010HeroCTAPage:
    """Page object for hero CTA."""

    def __init__(self, page: Page):
        self.page = page
        self.locators = Issue0010HeroCTALocators()
        self.locators.page = page

    def hero_cta_should_be_visible(self) -> None:
        """Verify hero CTA is visible."""
        expect(self.locators.hero_cta).to_be_visible()

    def cta_should_link_to_fdce_page(self) -> None:
        """Verify CTA links to FDCE page."""
        expect(self.locators.hero_cta).to_have_attribute(
            "href", "https://www.emids.com/forward-deployed-context-engineering/"
        )

    def click_hero_cta(self) -> None:
        """Click the hero CTA."""
        self.locators.hero_cta.click()

    def should_be_on_fdce_page(self) -> None:
        """Verify user is on the FDCE page."""
        expect(self.page).to_have_url("**/forward-deployed-context-engineering/**")
