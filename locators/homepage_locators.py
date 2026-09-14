"""Locators for the emids.com homepage."""
from playwright.sync_api import Locator, Page


class HomepageLocators:
    """Locators for the homepage header and navigation."""

    def __init__(self, page: Page):
        self.page = page

    @property
    def header(self) -> Locator:
        return self.page.locator("header").first

    @property
    def emids_logo(self) -> Locator:
        return self.page.locator("a[href='/'] img").first

    @property
    def emids_logo_link(self) -> Locator:
        return self.page.get_by_role("link", name="Emids logo")

    @property
    def main_navigation(self) -> Locator:
        return self.page.get_by_role("navigation", name="Main Navigation")

    @property
    def solutions_button(self) -> Locator:
        return self.page.get_by_role("button", name="Solutions")

    @property
    def solutions_mega_menu(self) -> Locator:
        return self.page.locator("nav[aria-label='Solutions']")

    @property
    def solutions_by_initiative_section(self) -> Locator:
        return self.page.get_by_text("Solutions by Initiative")

    @property
    def browse_by_industry_section(self) -> Locator:
        return self.page.get_by_text("Browse By Industry")

    @property
    def the_portfolio_section(self) -> Locator:
        return self.page.get_by_text("The Portfolio")

    @property
    def capabilities_button(self) -> Locator:
        return self.page.get_by_role("button", name="Capabilities")

    @property
    def capabilities_mega_menu(self) -> Locator:
        return self.page.locator("nav[aria-label='Capabilities']")

    @property
    def ai_group_label(self) -> Locator:
        return self.page.get_by_text("AI")

    @property
    def engineering_group_label(self) -> Locator:
        return self.page.get_by_text("Engineering")

    @property
    def platforms_group_label(self) -> Locator:
        return self.page.get_by_text("Platforms")

    @property
    def industries_button(self) -> Locator:
        return self.page.get_by_role("button", name="Industries")

    @property
    def industries_mega_menu(self) -> Locator:
        return self.page.locator("nav[aria-label='Industries']")

    @property
    def insights_button(self) -> Locator:
        return self.page.get_by_role("button", name="Insights")

    @property
    def insights_mega_menu(self) -> Locator:
        return self.page.locator("nav[aria-label='Insights']")

    @property
    def company_button(self) -> Locator:
        return self.page.get_by_role("button", name="Company")

    @property
    def company_mega_menu(self) -> Locator:
        return self.page.locator("nav[aria-label='Company']")

    @property
    def connect_cta(self) -> Locator:
        return self.page.get_by_role("link", name="Connect").first

    @property
    def all_nav_items(self) -> Locator:
        return self.page.get_by_role("navigation", name="Main Navigation").get_by_role("link,button")

    @property
    def hero_section(self) -> Locator:
        return self.page.locator("main > div").first

    @property
    def hero_h1(self) -> Locator:
        return self.page.locator("h1").first

    @property
    def hero_cta(self) -> Locator:
        return self.page.get_by_role("link", name="See How We Deliver Outcomes")

    @property
    def how_we_deliver_section(self) -> Locator:
        return self.page.get_by_text("Forward-Deployed Context Engineering")

    @property
    def see_the_model_cta(self) -> Locator:
        return self.page.get_by_role("link", name="See the model")

    @property
    def featured_solutions_section(self) -> Locator:
        return self.page.get_by_text("The Portfolio")

    @property
    def all_solutions_cta(self) -> Locator:
        return self.page.get_by_role("link", name="All solutions")

    @property
    def partners_section(self) -> Locator:
        return self.page.get_by_text("We've assembled the world's most powerful technology platforms")

    @property
    def partner_logos(self) -> Locator:
        return self.page.locator("[data-testid='partner-logo']")

    @property
    def capabilities_section(self) -> Locator:
        return self.page.get_by_text("Capabilities that deliver on ambitious goals")

    @property
    def ai_capability_card(self) -> Locator:
        return self.page.get_by_text("AI").locator("..").locator("..")

    @property
    def engineering_capability_card(self) -> Locator:
        return self.page.get_by_text("Engineering").locator("..").locator("..")

    @property
    def platforms_capability_card(self) -> Locator:
        return self.page.get_by_text("Platforms").locator("..").locator("..")

    @property
    def who_we_serve_section(self) -> Locator:
        return self.page.get_by_text("Every part of healthcare has its own anatomy")

    @property
    def payer_tab(self) -> Locator:
        return self.page.get_by_role("button", name="Payer")

    @property
    def provider_tab(self) -> Locator:
        return self.page.get_by_role("button", name="Provider")

    @property
    def healthtech_tab(self) -> Locator:
        return self.page.get_by_role("button", name="HealthTech")

    @property
    def life_sciences_tab(self) -> Locator:
        return self.page.get_by_role("button", name="Life Sciences")

    @property
    def consumer_tab(self) -> Locator:
        return self.page.get_by_role("button", name="Consumer")

    @property
    def impact_section(self) -> Locator:
        return self.page.get_by_text("In healthcare, good intentions don't move the needle")

    @property
    def metric_values(self) -> Locator:
        return self.page.locator("[data-testid='metric-value']")

    @property
    def insights_section(self) -> Locator:
        return self.page.get_by_text("The intelligence behind the outcomes")

    @property
    def insight_cards(self) -> Locator:
        return self.page.locator("[data-testid='insight-card']")

    @property
    def final_cta_section(self) -> Locator:
        return self.page.get_by_text("From workshop to agent to scale deployment")

    @property
    def timing_labels(self) -> Locator:
        return self.page.locator("[data-testid='timing-label']")

    @property
    def footer(self) -> Locator:
        return self.page.locator("footer").first

    @property
    def cookie_preferences_button(self) -> Locator:
        return self.page.get_by_role("button", name="Cookie Preferences").or_(self.page.get_by_role("link", name="Cookie Preferences"))

    @property
    def privacy_policy_link(self) -> Locator:
        return self.page.get_by_role("link", name="Privacy Policy")

    @property
    def cookie_policy_link(self) -> Locator:
        return self.page.get_by_role("link", name="Cookie Policy")

    @property
    def accessibility_statement_link(self) -> Locator:
        return self.page.get_by_role("link", name="Accessibility Statement")

    @property
    def mobile_menu_button(self) -> Locator:
        return self.page.get_by_role("button", name="Open menu")

    @property
    def mobile_nav_items(self) -> Locator:
        return self.page.locator("[data-testid='mobile-nav'] a, [data-testid='mobile-nav'] button")

    @property
    def consent_banner(self) -> Locator:
        return self.page.locator("[data-testid='cookie-consent']")

    @property
    def allow_all_button(self) -> Locator:
        return self.page.get_by_role("button", name="Allow all")

    @property
    def customize_button(self) -> Locator:
        return self.page.get_by_role("button", name="Customize")
