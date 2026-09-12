"""Locators for the Emids homepage."""
from playwright.sync_api import Locator, Page


class HomePageLocators:
    """Locators for the Emids homepage."""

    def __init__(self, page: Page):
        self.page = page

    # Header locators
    @property
    def emids_logo(self) -> Locator:
        return self.page.get_by_role("link", name="Emids logo")

    @property
    def navigation(self) -> Locator:
        return self.page.get_by_role("navigation", name="Main Navigation")

    @property
    def solutions_nav_link(self) -> Locator:
        return self.page.get_by_role("link", name="Solutions").first

    @property
    def capabilities_nav_link(self) -> Locator:
        return self.page.get_by_role("link", name="Capabilities").first

    @property
    def industries_nav_link(self) -> Locator:
        return self.page.get_by_role("link", name="Industries").first

    @property
    def insights_nav_link(self) -> Locator:
        return self.page.get_by_role("link", name="Insights").first

    @property
    def company_nav_link(self) -> Locator:
        return self.page.get_by_role("link", name="Company").first

    @property
    def header_connect_cta(self) -> Locator:
        return self.page.get_by_role("link", name="Connect").first

    # Solutions mega-menu
    @property
    def solutions_menu_button(self) -> Locator:
        return self.page.get_by_role("button", name="Solutions").first

    @property
    def solutions_menu(self) -> Locator:
        return self.page.locator('[aria-label="Solutions menu"], [class*="solutions"]').first

    # Capabilities mega-menu
    @property
    def capabilities_menu_button(self) -> Locator:
        return self.page.get_by_role("button", name="Capabilities").first

    # Industries menu
    @property
    def industries_menu_button(self) -> Locator:
        return self.page.get_by_role("button", name="Industries").first

    # Insights menu
    @property
    def insights_menu_button(self) -> Locator:
        return self.page.get_by_role("button", name="Insights").first

    # Company menu
    @property
    def company_menu_button(self) -> Locator:
        return self.page.get_by_role("button", name="Company").first

    # Hero section
    @property
    def hero_h1(self) -> Locator:
        return self.page.get_by_role("heading", level=1).first

    @property
    def hero_cta(self) -> Locator:
        return self.page.get_by_role("link", name="See How We Deliver Outcomes")

    # How We Deliver section
    @property
    def how_we_deliver_section(self) -> Locator:
        return self.page.locator("text=How We Deliver").first

    @property
    def see_the_model_cta(self) -> Locator:
        return self.page.get_by_role("link", name="See the model")

    # Featured Solutions
    @property
    def featured_solutions_section(self) -> Locator:
        return self.page.locator("text=Featured solutions").first

    @property
    def all_solutions_cta(self) -> Locator:
        return self.page.get_by_role("link", name="All solutions")

    @property
    def featured_solution_cards(self) -> Locator:
        return self.page.locator('[href*="/solutions/"]').filter(has_text=["01", "02", "03", "04", "05", "06"])

    # Partnerships logos
    @property
    def partnerships_section(self) -> Locator:
        return self.page.locator("text=Partnerships").first

    @property
    def partner_logos(self) -> Locator:
        return self.page.locator('[src*="Partner"], img[alt*="Partner"], img[alt*="Logo"]')

    # Capabilities section
    @property
    def capabilities_section(self) -> Locator:
        return self.page.locator("text=Capabilities").first

    @property
    def ai_capabilities_group(self) -> Locator:
        return self.page.get_by_role("heading", name="Artificial Intelligence")

    @property
    def engineering_capabilities_group(self) -> Locator:
        return self.page.get_by_role("heading", name="Engineering")

    @property
    def platforms_capabilities_group(self) -> Locator:
        return self.page.get_by_role("heading", name="Platforms")

    # Who We Serve section
    @property
    def who_we_serve_section(self) -> Locator:
        return self.page.locator("text=Who we Serve").first

    @property
    def audience_buttons(self) -> Locator:
        return self.page.get_by_role("button", name=["Payer", "Provider", "HealthTech", "Life Sciences", "Consumer"])

    # Impact metrics
    @property
    def impact_section(self) -> Locator:
        return self.page.locator("text=Impact").first

    @property
    def impact_metrics(self) -> Locator:
        return self.page.locator('[aria-label*="Years"], [aria-label*="Millions"], [aria-label*="Billion"], [aria-label*="Platforms"]')

    # Insights section
    @property
    def insights_section(self) -> Locator:
        return self.page.get_by_role("heading", name="The intelligence behind the outcomes")

    @property
    def insights_next_button(self) -> Locator:
        return self.page.get_by_role("button", name="Next")

    @property
    def insights_cards(self) -> Locator:
        return self.page.locator('[class*="insight"], [class*="card"]').filter(has_text=["eBook", "blog", "Webinar", "Case Study"])

    # Final CTA section
    @property
    def final_cta_section(self) -> Locator:
        return self.page.locator("text=1 Day · 2 Weeks · 3 Months").first

    @property
    def final_cta_connect(self) -> Locator:
        return self.page.locator('[class*="cta"] >> text=Connect').first

    @property
    def timing_labels(self) -> Locator:
        return self.page.locator('[class*="timing"], text=/1 Day|2 Weeks|3 Months/')

    # Footer
    @property
    def footer(self) -> Locator:
        return self.page.get_by_role("contentinfo")

    @property
    def cookie_preferences_button(self) -> Locator:
        return self.page.get_by_role("button", name="Cookie Preferences")

    @property
    def footer_legal_links(self) -> Locator:
        return self.page.get_by_role("link", name=["Privacy Policy", "Terms of Use", "Accessibility Statement"])

    # Cookie consent
    @property
    def cookie_consent_banner(self) -> Locator:
        return self.page.locator('text="This website uses cookies"')

    @property
    def allow_all_cookies_button(self) -> Locator:
        return self.page.get_by_role("button", name="Allow all")

    @property
    def customize_cookies_button(self) -> Locator:
        return self.page.get_by_role("button", name="Customize")

    @property
    def show_cookie_details_link(self) -> Locator:
        return self.page.get_by_role("link", name="Show details")
