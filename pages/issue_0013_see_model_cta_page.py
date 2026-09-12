"""Page object for issue_0013 - See the model CTA routing and operation."""
from playwright.sync_api import Page, expect

from locators.issue_0013_see_model_cta_locators import Issue0013SeeModelCTALocators


class Issue0013SeeModelCTAPage:
    """Page object for See the model CTA."""

    def __init__(self, page: Page):
        self.page = page
        self.locators = Issue0013SeeModelCTALocators()
        self.locators.page = page

    def view_how_we_deliver_section(self) -> None:
        """Scroll to the How We Deliver section."""
        self.locators.see_model_cta.scroll_into_view_if_needed()

    def see_model_cta_should_be_visible(self) -> None:
        """Verify See the model CTA is visible."""
        expect(self.locators.see_model_cta).to_be_visible()

    def cta_should_link_to_fdce_page(self) -> None:
        """Verify CTA links to FDCE page."""
        expect(self.locators.see_model_cta).to_have_attribute(
            "href", "https://www.emids.com/forward-deployed-context-engineering/"
        )

    def click_see_model_cta(self) -> None:
        """Click the See the model CTA."""
        self.locators.see_model_cta.click()

    def should_be_on_fdce_page(self) -> None:
        """Verify user is on the FDCE page."""
        expect(self.page).to_have_url("**/forward-deployed-context-engineering/**")
