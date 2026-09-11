"""Page object for REQ-003: Primary CTA buttons function correctly."""

from playwright.sync_api import Page, expect

from pages.base_page import BasePage
from locators.req_003_cta_locators import Req003CtaLocators


class Req003CtaPage(BasePage):
    """Page object for CTA button operations."""

    def __init__(self, page: Page):
        super().__init__(page)
        self.locators = Req003CtaLocators(page)

    def click_see_how_we_deliver_outcomes(self) -> None:
        """Click on 'See How We Deliver Outcomes' link."""
        self.locators.see_how_we_deliver_outcomes_link.click()
        self.page.wait_for_load_state("networkidle")

    def click_see_the_model(self) -> None:
        """Click on 'See the model' link."""
        self.locators.see_the_model_link.click()
        self.page.wait_for_load_state("networkidle")

    def click_all_solutions(self) -> None:
        """Click on 'All solutions' link."""
        self.locators.all_solutions_link.click()
        self.page.wait_for_load_state("networkidle")

    def click_connect_cta(self) -> None:
        """Click on 'Connect' CTA link."""
        self.locators.connect_cta_link.click()
        self.page.wait_for_load_state("networkidle")

    def verify_navigated_to_forward_deployed_page(self) -> None:
        """Verify navigation to Forward-Deployed Context Engineering page."""
        expect(self.page).to_have_url("*forward-deployed-context-engineering*")

    def verify_navigated_to_solutions_page(self) -> None:
        """Verify navigation to Solutions page."""
        expect(self.page).to_have_url("*solutions*")

    def verify_navigated_to_contact_page(self) -> None:
        """Verify navigation to Contact page."""
        expect(self.page).to_have_url("*contact*")

    def verify_see_how_we_deliver_outcomes_visible(self) -> None:
        """Verify 'See How We Deliver Outcomes' button is visible."""
        expect(self.locators.see_how_we_deliver_outcomes_link).to_be_visible()

    def verify_see_the_model_visible(self) -> None:
        """Verify 'See the model' button is visible."""
        expect(self.locators.see_the_model_link).to_be_visible()

    def verify_all_solutions_visible(self) -> None:
        """Verify 'All solutions' button is visible."""
        expect(self.locators.all_solutions_link).to_be_visible()

    def verify_connect_cta_visible(self) -> None:
        """Verify 'Connect' CTA button is visible."""
        expect(self.locators.connect_cta_link).to_be_visible()
