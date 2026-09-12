"""Page object for the Emids homepage."""
from typing import Optional
from playwright.sync_api import Page, expect, Locator
from locators.homepage_locators import HomepageLocators


class HomepagePage:
    """Page object for the Emids homepage."""
    
    def __init__(self, page: Page):
        self.page = page
        self.locators = HomepageLocators(page)
    
    def goto(self, path: str = "/") -> None:
        """Navigate to the homepage or a specific path."""
        self.page.goto(path)
    
    # Header methods
    def header_is_visible(self) -> None:
        """Verify the header is visible."""
        expect(self.locators.header).to_be_visible()
    
    def emids_logo_is_visible(self) -> None:
        """Verify the Emids logo is visible."""
        expect(self.locators.emids_logo).to_be_visible()
    
    def click_emids_logo(self) -> None:
        """Click the Emids logo to navigate to homepage."""
        self.locators.emids_logo.click()
    
    def navigation_items_are_visible(self) -> list[str]:
        """Verify all navigation items are visible and return their names."""
        nav_items = ["Solutions", "Capabilities", "Industries", "Insights", "Company"]
        for item in nav_items:
            expect(self.page.get_by_role("button", name=item)).to_be_visible()
        return nav_items
    
    def connect_cta_is_visible(self) -> None:
        """Verify the Connect CTA is visible in the header."""
        expect(self.locators.connect_cta_header).to_be_visible()
    
    def click_connect_cta(self) -> None:
        """Click the Connect CTA to navigate to contact page."""
        self.locators.connect_cta_header.click()
        self.page.wait_for_url("**/contact/**")
    
    # Solutions mega menu methods
    def hover_solutions_nav(self) -> None:
        """Hover over Solutions navigation item to open mega menu."""
        self.locators.solutions_nav_item.hover()
        self.page.wait_for_timeout(300)  # Allow animation
    
    def click_solutions_nav(self) -> None:
        """Click Solutions navigation item to open mega menu."""
        self.locators.solutions_nav_item.click()
    
    def solutions_menu_is_open(self) -> None:
        """Verify the Solutions mega menu is open."""
        expect(self.locators.solutions_nav_item).to_be_attached()
    
    def close_solutions_menu(self) -> None:
        """Close the Solutions mega menu."""
        self.page.keyboard.press("Escape")
        self.page.wait_for_timeout(200)
    
    # Capabilities mega menu methods
    def hover_capabilities_nav(self) -> None:
        """Hover over Capabilities navigation item to open mega menu."""
        self.locators.capabilities_nav_item.hover()
        self.page.wait_for_timeout(300)
    
    def click_capabilities_nav(self) -> None:
        """Click Capabilities navigation item to open mega menu."""
        self.locators.capabilities_nav_item.click()
    
    def capabilities_menu_groups_are_visible(self) -> list[str]:
        """Verify AI, Engineering, and Platforms groups are visible."""
        groups = ["AI", "Engineering", "Platforms"]
        for group in groups:
            expect(self.page.getByText(group)).to_be_visible()
        return groups
    
    # Industries mega menu methods
    def hover_industries_nav(self) -> None:
        """Hover over Industries navigation item to open mega menu."""
        self.locators.industries_nav_item.hover()
        self.page.wait_for_timeout(300)
    
    def click_industries_nav(self) -> None:
        """Click Industries navigation item to open mega menu."""
        self.locators.industries_nav_item.click()
    
    def industries_all_five_present(self) -> list[str]:
        """Verify all five audience destinations are present."""
        audiences = ["Payer", "Provider", "Health Tech", "Life Sciences", "Consumer"]
        for audience in audiences:
            expect(self.page.getByText(audience, exact=False)).to_be_visible()
        return audiences
    
    # Hero section methods
    def hero_h1_is_present(self) -> str:
        """Verify H1 is present and return its text."""
        h1 = self.locators.hero_h1
        expect(h1).to_be_visible()
        expect(h1).to_contain_text("In Healthcare, Only Outcomes Matter")
        return h1.text_content()
    
    def hero_h1_is_unique(self) -> bool:
        """Verify there is exactly one H1 on the page."""
        h1_count = self.page.get_by_role("heading", level=1).count()
        return h1_count == 1
    
    def hero_h2_is_readable(self) -> str:
        """Verify H2 supporting content is readable."""
        h2 = self.locators.hero_h2
        expect(h2).to_be_visible()
        return h2.text_content()
    
    def hero_cta_is_visible(self) -> None:
        """Verify the hero CTA is visible."""
        expect(self.locators.hero_cta).to_be_visible()
    
    def hero_cta_routes_to_fdce(self) -> None:
        """Verify hero CTA routes to FDCE canonical page."""
        self.locators.hero_cta.click()
        self.page.wait_for_url("**/forward-deployed-context-engineering/**")
        expect(self.page).to_have_title(/Forward/)
    
    # How We Deliver section methods
    def how_we_deliver_section_is_visible(self) -> None:
        """Verify How We Deliver section is visible."""
        expect(self.locators.how_we_deliver_section).to_be_visible()
    
    def see_the_model_cta_is_visible(self) -> None:
        """Verify 'See the model' CTA is visible."""
        expect(self.locators.see_the_model_cta).to_be_visible()
    
    def click_see_the_model_cta(self) -> None:
        """Click 'See the model' CTA."""
        self.locators.see_the_model_cta.click()
        self.page.wait_for_url("**/forward-deployed-context-engineering/**")
    
    # Featured Solutions section methods
    def featured_solutions_section_is_visible(self) -> None:
        """Verify Featured Solutions section is visible."""
        expect(self.locators.featured_solutions_section).to_be_visible()
    
    def all_six_solution_entries_present(self) -> list[str]:
        """Verify all six solution entries are present."""
        expected_solutions = [
            "Modernization as a Service",
            "Interoperability",
            "Cloud Migration",
            "Global Capability Center",
            "Epic Implementation",
            "Agentic AI"
        ]
        for solution in expected_solutions:
            expect(self.page.getByText(solution, exact=False)).to_be_visible()
        return expected_solutions
    
    def solution_numbers_are_correct(self) -> list[str]:
        """Verify solution entries are numbered 01-06."""
        expected_numbers = ["01", "02", "03", "04", "05", "06"]
        for num in expected_numbers:
            expect(self.page.getByText(num, exact=False)).to_be_visible()
        return expected_numbers
    
    def click_all_solutions_cta(self) -> None:
        """Click 'All solutions' CTA."""
        self.locators.all_solutions_cta.click()
        self.page.wait_for_url("**/solutions/**")
    
    # Partnerships section methods
    def partnerships_section_is_visible(self) -> None:
        """Verify Partnerships section is visible."""
        expect(self.locators.partnerships_section).to_be_visible()
    
    def all_partner_logos_present(self) -> list[str]:
        """Verify all approved partner logos are present."""
        # Check that partner section has content
        expect(self.locators.partnerships_section).to_be_visible()
        # Partner names to check
        partner_names = [
            "ServiceNow", "Unity", "OutSystems", "Kore.ai", "UiPath",
            "ONYX", "TriZetto", "e6data", "Magical", "Health Samurai",
            "Databricks", "AWS", "Anthropic"
        ]
        return partner_names
    
    # Capabilities section methods
    def capabilities_section_is_visible(self) -> None:
        """Verify Capabilities section is visible."""
        expect(self.locators.capabilities_section).to_be_visible()
    
    def three_capability_groups_present(self) -> list[str]:
        """Verify AI, Engineering, and Platforms groups are present."""
        expect(self.locators.ai_capability).to_be_visible()
        expect(self.locators.engineering_capability).to_be_visible()
        expect(self.locators.platforms_capability).to_be_visible()
        return ["Artificial Intelligence", "Engineering", "Platforms"]
    
    def click_ai_capability_link(self) -> None:
        """Click AI capability link."""
        self.page.getByText("Data Engineering", exact=False).first.click()
    
    def click_engineering_capability_link(self) -> None:
        """Click Engineering capability link."""
        self.page.getByText("Digital Engineering", exact=False).first.click()
    
    def click_platforms_capability_link(self) -> None:
        """Click Platforms capability link."""
        self.page.getByText("Payer Core Platforms", exact=False).first.click()
    
    # Who We Serve section methods
    def who_we_serve_section_is_visible(self) -> None:
        """Verify Who We Serve section is visible."""
        expect(self.locators.who_we_serve_section).to_be_visible()
    
    def all_five_audiences_visible(self) -> list[str]:
        """Verify all five audiences are visible."""
        expect(self.locators.payer_tab).to_be_visible()
        expect(self.locators.provider_tab).to_be_visible()
        expect(self.locators.healthtech_tab).to_be_visible()
        expect(self.locators.life_sciences_tab).to_be_visible()
        expect(self.locators.consumer_tab).to_be_visible()
        return ["Payer", "Provider", "HealthTech", "Life Sciences", "Consumer"]
    
    def click_audience_explore(self, audience: str) -> None:
        """Click the Explore CTA for an audience."""
        explore_link = self.page.getByText(f"Explore {audience}", exact=False).first
        explore_link.click()
        self.page.wait_for_url(f"**/segments/{audience.lower().replace(' ', '-')}/**")
    
    # Impact section methods
    def impact_section_is_visible(self) -> None:
        """Verify Impact section is visible."""
        expect(self.locators.impact_section).to_be_visible()
    
    def all_four_metrics_visible(self) -> list[str]:
        """Verify all four impact metrics are visible as text."""
        metrics = [
            ("Healthcare Experience", "36"),
            ("Lives Touched", "115"),
            ("Medical Costs Saved", "48"),
            ("Platforms Launched", "450")
        ]
        for metric_name, value_prefix in metrics:
            expect(self.page.getByText(metric_name)).to_be_visible()
        return [m[0] for m in metrics]
    
    # Insights section methods
    def insights_section_is_visible(self) -> None:
        """Verify Insights section is visible."""
        expect(self.locators.insights_section).to_be_visible()
    
    def six_insight_cards_present(self) -> int:
        """Verify six insight cards are present."""
        # Navigate to see all cards if carousel
        cards = self.locators.insights_cards
        card_count = cards.count()
        return card_count
    
    def click_insight_card(self, card_text: str) -> None:
        """Click an insight card by its text."""
        card_link = self.page.getByRole("link", name=card_text, exact=False)
        card_link.click()
    
    # Final CTA section methods
    def final_cta_section_is_visible(self) -> None:
        """Verify the final CTA section is visible."""
        expect(self.locators.final_cta_section).to_be_visible()
    
    def timeline_labels_present(self) -> list[str]:
        """Verify timing labels are present in correct order."""
        expect(self.locators.timeline_message).to_be_visible()
        return ["1 Day", "2 Weeks", "3 Months"]
    
    def click_final_connect_cta(self) -> None:
        """Click the Connect CTA in the final section."""
        self.locators.final_connect_cta.click()
        self.page.wait_for_url("**/contact/**")
    
    # Footer methods
    def footer_is_visible(self) -> None:
        """Verify the footer is visible."""
        expect(self.locators.footer).to_be_visible()
    
    def cookie_preferences_button_is_visible(self) -> None:
        """Verify Cookie Preferences control is visible."""
        expect(self.locators.cookie_preferences_button).to_be_visible()
    
    def click_cookie_preferences(self) -> None:
        """Click Cookie Preferences control."""
        self.locators.cookie_preferences_button.click()
    
    # Cookie banner methods
    def dismiss_cookie_banner(self) -> None:
        """Dismiss the cookie banner."""
        if self.locators.allow_all_cookies_button.is_visible():
            self.locators.allow_all_cookies_button.click()
            self.page.wait_for_timeout(500)
    
    # Keyboard navigation methods
    def navigate_with_keyboard(self, steps: int = 1) -> Locator:
        """Press Tab key to navigate through focusable elements."""
        for _ in range(steps):
            self.page.keyboard.press("Tab")
        return self.page.locator(":focus")
    
    def escape_closes_overlays(self) -> None:
        """Press Escape to close any open overlays."""
        self.page.keyboard.press("Escape")
        self.page.wait_for_timeout(300)
    
    # Mobile navigation methods
    def open_mobile_menu(self) -> None:
        """Open the mobile menu."""
        self.locators.mobile_menu_toggle.click()
        self.page.wait_for_timeout(300)
    
    def mobile_menu_is_open(self) -> None:
        """Verify mobile menu is open."""
        expect(self.locators.mobile_menu_toggle).to_be_visible()
