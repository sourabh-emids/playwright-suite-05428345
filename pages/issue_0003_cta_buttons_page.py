"""Page object for issue_0003: Primary CTA buttons function properly."""
from playwright.sync_api import Page, expect

from locators.issue_0003_cta_buttons_locators import CtaButtonsLocators


class CtaButtonsPage:
    """Page object for CTA buttons on the homepage."""

    def __init__(self, page: Page):
        self.page = page
        self.locators = CtaButtonsLocators(page)

    def load_homepage(self) -> None:
        self.page.goto("/")

    def click_see_how_cta(self) -> None:
        self.locators.see_how_cta.click()
        expect(self.page).to_have_url("**/forward-deployed-context-engineering/**")

    def click_connect_cta(self) -> None:
        self.locators.connect_cta.click()
        expect(self.page).to_have_url("**/contact/**")

    def click_learn_more_like_cta(self) -> None:
        """Click 'See the model' which serves as a Learn More style CTA."""
        self.locators.see_model_cta.click()
        expect(self.page).to_have_url("**/forward-deployed-context-engineering/**")
