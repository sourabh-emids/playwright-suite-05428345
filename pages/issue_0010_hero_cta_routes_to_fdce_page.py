"""Page object for issue_0010: Hero CTA routes to FDCE"""

from playwright.sync_api import Page, expect

from locators.issue_0010_hero_cta_routes_to_fdce_locators import Issue0010HeroCTALocators


class Issue0010HeroCTAPage:
    """Page object for Hero CTA routing."""

    def __init__(self, page: Page):
        self.page = page
        self.locators = Issue0010HeroCTALocators(page)

    def navigate_to_homepage(self) -> None:
        """Navigate to homepage."""
        self.page.goto("https://www.emids.com")

    def click_hero_cta(self) -> None:
        """Click the hero CTA."""
        self.locators.hero_cta.click()

    def verify_routes_to_fdce(self) -> None:
        """Verify navigation to FDCE page."""
        expect(self.page).to_have_url("https://www.emids.com/forward-deployed-context-engineering/")

    def verify_https_canonical(self) -> None:
        """Verify URL is HTTPS and canonical."""
        href = self.locators.hero_cta.get_attribute("href")
        expect(href).to_match(r"^https://www\.emids\.com/forward-deployed-context-engineering/?$")

    def verify_semantic_element(self) -> None:
        """Verify CTA is a semantic link or button."""
        role = self.locators.hero_cta.get_attribute("role")
        tag = self.locators.hero_cta.evaluate("el => el.tagName")
        is_semantic = tag in ["A", "BUTTON"] or role in ["link", "button"]
        expect(is_semantic).to_be(True)
