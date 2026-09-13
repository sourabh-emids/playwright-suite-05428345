"""Page object for See the model CTA functionality (issue_0013)."""
from playwright.sync_api import Page

from locators.issue_0013_see_model_cta_locators import SeeModelCTALocators


class SeeModelCTAPage:
    """Page object for See the model CTA functionality."""

    def __init__(self, page: Page):
        self.page = page
        self.locators = SeeModelCTALocators(page)

    def goto_homepage(self) -> None:
        self.page.goto("/")

    def scroll_to_cta(self) -> None:
        self.locators.see_model_cta.scroll_into_view_if_needed()

    def click_cta(self) -> None:
        self.locators.see_model_cta.click()

    def focus_cta(self) -> None:
        self.locators.see_model_cta.focus()

    def hover_cta(self) -> None:
        self.locators.see_model_cta.hover()

    def get_accessible_name(self) -> str:
        return self.locators.see_model_cta.get_attribute("aria-label") or self.locators.see_model_cta.text_content()
