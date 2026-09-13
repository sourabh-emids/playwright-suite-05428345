"""Page object for issue_0013: See the model CTA functionality"""

from playwright.sync_api import Page, expect

from locators.issue_0013_see_the_model_cta_functionality_locators import Issue0013SeeModelCTALocators


class Issue0013SeeModelCTAPage:
    """Page object for See the model CTA."""

    def __init__(self, page: Page):
        self.page = page
        self.locators = Issue0013SeeModelCTALocators(page)

    def navigate_to_homepage(self) -> None:
        """Navigate to homepage."""
        self.page.goto("https://www.emids.com")

    def click_see_model_cta(self) -> None:
        """Click the See the model CTA."""
        self.locators.see_model_cta.click()

    def verify_routes_to_fdce(self) -> None:
        """Verify navigation to FDCE page."""
        expect(self.page).to_have_url("https://www.emids.com/forward-deployed-context-engineering/")

    def focus_and_press_enter(self) -> None:
        """Focus on CTA and press Enter."""
        self.locators.see_model_cta.focus()
        self.page.keyboard.press("Enter")

    def verify_accessible_name(self) -> None:
        """Verify CTA has descriptive accessible name."""
        name = self.locators.see_model_cta.get_attribute("aria-label") or self.locators.see_model_cta.inner_text()
        expect(name.lower()).to_contain("model")

    def verify_destination_returns_200(self) -> None:
        """Verify destination URL returns 200."""
        href = self.locators.see_model_cta.get_attribute("href")
        response = self.page.request.get(href)
        expect(response.status).to_be(200)
