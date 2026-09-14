"""Page object for the emids.com homepage."""
from playwright.sync_api import Page, expect

from locators.homepage_locators import HomepageLocators
from pages.base_page import BasePage


class HomepagePage(BasePage):
    """Page object for the emids.com homepage."""

    def __init__(self, page: Page):
        super().__init__(page)
        self.locators = HomepageLocators(page)

    def goto_homepage(self) -> None:
        """Navigate to the homepage."""
        self.goto("/")

    def click_emids_logo(self) -> None:
        """Click the Emids logo."""
        self.locators.emids_logo_link.click()

    def click_solutions_button(self) -> None:
        """Click the Solutions navigation button to open the mega-menu."""
        self.locators.solutions_button.click()

    def click_capabilities_button(self) -> None:
        """Click the Capabilities navigation button."""
        self.locators.capabilities_button.click()

    def click_industries_button(self) -> None:
        """Click the Industries navigation button."""
        self.locators.industries_button.click()

    def click_insights_button(self) -> None:
        """Click the Insights navigation button."""
        self.locators.insights_button.click()

    def click_company_button(self) -> None:
        """Click the Company navigation button."""
        self.locators.company_button.click()

    def click_connect_cta(self) -> None:
        """Click the Connect CTA in the header."""
        self.locators.connect_cta.click()

    def click_hero_cta(self) -> None:
        """Click the hero CTA."""
        self.locators.hero_cta.click()

    def click_see_the_model_cta(self) -> None:
        """Click the 'See the model' CTA."""
        self.locators.see_the_model_cta.click()

    def click_all_solutions_cta(self) -> None:
        """Click the 'All solutions' CTA."""
        self.locators.all_solutions_cta.click()

    def click_cookie_preferences(self) -> None:
        """Click the Cookie Preferences button/link."""
        self.locators.cookie_preferences_button.click()

    def click_privacy_policy(self) -> None:
        """Click the Privacy Policy link."""
        self.locators.privacy_policy_link.click()

    def click_cookie_policy(self) -> None:
        """Click the Cookie Policy link."""
        self.locators.cookie_policy_link.click()

    def click_accessibility_statement(self) -> None:
        """Click the Accessibility Statement link."""
        self.locators.accessibility_statement_link.click()

    def click_mobile_menu_button(self) -> None:
        """Click the mobile menu button."""
        self.locators.mobile_menu_button.click()

    def click_allow_all_cookies(self) -> None:
        """Click the 'Allow all' cookies button."""
        self.locators.allow_all_button.click()

    def press_tab_key(self, times: int = 1) -> None:
        """Press the Tab key a specified number of times."""
        for _ in range(times):
            self.page.keyboard.press("Tab")

    def press_escape_key(self) -> None:
        """Press the Escape key."""
        self.page.keyboard.press("Escape")

    def get_current_url(self) -> str:
        """Get the current page URL."""
        return self.page.url

    def navigate_to_path(self, path: str) -> None:
        """Navigate to a specific path."""
        self.goto(path)

    def verify_header_visible(self) -> None:
        """Verify the header is visible."""
        expect(self.locators.header).to_be_visible()

    def verify_solutions_mega_menu_visible(self) -> None:
        """Verify the Solutions mega-menu is visible."""
        expect(self.locators.solutions_mega_menu).to_be_visible()

    def verify_capabilities_mega_menu_visible(self) -> None:
        """Verify the Capabilities mega-menu is visible."""
        expect(self.locators.capabilities_mega_menu).to_be_visible()

    def verify_industries_mega_menu_visible(self) -> None:
        """Verify the Industries mega-menu is visible."""
        expect(self.locators.industries_mega_menu).to_be_visible()

    def verify_insights_mega_menu_visible(self) -> None:
        """Verify the Insights mega-menu is visible."""
        expect(self.locators.insights_mega_menu).to_be_visible()

    def verify_company_mega_menu_visible(self) -> None:
        """Verify the Company mega-menu is visible."""
        expect(self.locators.company_mega_menu).to_be_visible()

    def verify_hero_h1_visible(self) -> None:
        """Verify the hero H1 is visible."""
        expect(self.locators.hero_h1).to_be_visible()

    def verify_connect_cta_visible(self) -> None:
        """Verify the Connect CTA is visible."""
        expect(self.locators.connect_cta).to_be_visible()

    def verify_footer_visible(self) -> None:
        """Verify the footer is visible."""
        expect(self.locators.footer).to_be_visible()

    def get_h1_text(self) -> str:
        """Get the H1 text content."""
        return self.locators.hero_h1.text_content()

    def get_nav_item_count(self) -> int:
        """Get the count of navigation items."""
        return self.locators.all_nav_items.count()

    def get_solution_cards_count(self) -> int:
        """Get the count of featured solution cards."""
        return self.page.locator("[data-testid='solution-card']").count()

    def get_partner_logos_count(self) -> Locator:
        """Get the count of partner logos."""
        return self.page.locator("[data-testid='partner-logo']").count()

    def get_insight_cards_count(self) -> int:
        """Get the count of insight cards."""
        return self.locators.insight_cards.count()

    def get_capability_cards(self) -> list:
        """Get all capability cards."""
        return [
            self.locators.ai_capability_card,
            self.locators.engineering_capability_card,
            self.locators.platforms_capability_card,
        ]

    def get_industry_tabs(self) -> list:
        """Get all industry tabs."""
        return [
            self.locators.payer_tab,
            self.locators.provider_tab,
            self.locators.healthtech_tab,
            self.locators.life_sciences_tab,
            self.locators.consumer_tab,
        ]

    def get_timing_labels_text(self) -> list:
        """Get all timing label text."""
        return [label.text_content() for label in self.locators.timing_labels.all()]

    def check_nav_item_has_valid_href(self, item_index: int) -> bool:
        """Check if a navigation item has a valid href."""
        items = self.locators.all_nav_items.all()
        if item_index < len(items):
            href = items[item_index].get_attribute("href")
            return href is not None and href != "#" and href != ""
        return False

    def get_focusable_elements_in_order(self) -> list:
        """Get all focusable elements in order for keyboard navigation testing."""
        return self.page.evaluate("""() => {
            const focusable = [];
            const elements = document.querySelectorAll(
                'a[href], button:not([disabled]), input:not([disabled]), ' +
                'select:not([disabled]), textarea:not([disabled]), ' +
                '[tabindex]:not([tabindex="-1"])'
            );
            elements.forEach(el => {
                const rect = el.getBoundingClientRect();
                if (rect.width > 0 && rect.height > 0) {
                    focusable.push({
                        tag: el.tagName,
                        text: el.textContent?.trim().substring(0, 50),
                        href: el.getAttribute('href')
                    });
                }
            });
            return focusable;
        }""")
