"""Locators for the Emids homepage."""
from playwright.sync_api import Locator, Page


class HomepageLocators:
    """Locators for the Emids homepage."""
    
    def __init__(self, page: Page):
        self.page = page
    
    # Header locators
    @property
    def header(self) -> Locator:
        return self.page.locator("header").first
    
    @property
    def emids_logo(self) -> Locator:
        return self.page.get_by_role("link", name="Emids logo").first
    
    @property
    def navigation(self) -> Locator:
        return self.page.get_by_role("navigation", name="Main Navigation")
    
    @property
    def solutions_nav_item(self) -> Locator:
        return self.page.get_by_role("button", name="Solutions").first
    
    @property
    def capabilities_nav_item(self) -> Locator:
        return self.page.get_by_role("button", name="Capabilities").first
    
    @property
    def industries_nav_item(self) -> Locator:
        return self.page.get_by_role("button", name="Industries").first
    
    @property
    def insights_nav_item(self) -> Locator:
        return self.page.get_by_role("button", name="Insights").first
    
    @property
    def company_nav_item(self) -> Locator:
        return self.page.get_by_role("button", name="Company").first
    
    @property
    def connect_cta_header(self) -> Locator:
        return self.page.get_by_role("link", name="Connect").first
    
    # Solutions mega menu
    @property
    def solutions_menu(self) -> Locator:
        return self.page.locator('[data-testid="solutions-menu"]').first
    
    @property
    def solutions_menu_by_initiative(self) -> Locator:
        return self.page.get_by_text("Solutions by Initiative")
    
    @property
    def solutions_menu_browse_by_industry(self) -> Locator:
        return self.page.get_by_text("Browse By Industry")
    
    @property
    def solutions_menu_portfolio(self) -> Locator:
        return self.page.get_by_text("The Portfolio")
    
    # Capabilities mega menu
    @property
    def capabilities_menu(self) -> Locator:
        return self.page.locator('[data-testid="capabilities-menu"]').first
    
    @property
    def capabilities_menu_ai(self) -> Locator:
        return self.page.get_by_text("AI").first
    
    @property
    def capabilities_menu_engineering(self) -> Locator:
        return self.page.get_by_text("Engineering").first
    
    @property
    def capabilities_menu_platforms(self) -> Locator:
        return self.page.get_by_text("Platforms").first
    
    # Industries mega menu
    @property
    def industries_menu(self) -> Locator:
        return self.page.locator('[data-testid="industries-menu"]').first
    
    # Hero section
    @property
    def hero_section(self) -> Locator:
        return self.page.locator('[class*="hero"]').first
    
    @property
    def hero_h1(self) -> Locator:
        return self.page.get_by_role("heading", level=1).first
    
    @property
    def hero_h2(self) -> Locator:
        return self.page.get_by_role("heading", level=2).first
    
    @property
    def hero_cta(self) -> Locator:
        return self.page.get_by_role("link", name="See How We Deliver Outcomes")
    
    # How We Deliver section
    @property
    def how_we_deliver_section(self) -> Locator:
        return self.page.get_by_text("How We Deliver").first
    
    @property
    def see_the_model_cta(self) -> Locator:
        return self.page.get_by_role("link", name="See the model")
    
    # Featured Solutions section
    @property
    def featured_solutions_section(self) -> Locator:
        return self.page.get_by_text("Featured solutions").first
    
    @property
    def solution_cards(self) -> Locator:
        return self.page.locator('[class*="solution-card"], [class*="featured-solution"]')
    
    @property
    def all_solutions_cta(self) -> Locator:
        return self.page.get_by_role("link", name="All solutions")
    
    # Partnerships section
    @property
    def partnerships_section(self) -> Locator:
        return self.page.get_by_text("Partnerships").first
    
    @property
    def partner_logos(self) -> Locator:
        return self.page.locator('[class*="partner-logo"], [class*="partner"] img')
    
    @property
    def servicenow_logo(self) -> Locator:
        return self.page.locator('img[alt*="ServiceNow"], img[alt*="Servicenow"]').first
    
    @property
    def unity_logo(self) -> Locator:
        return self.page.locator('img[alt*="Unity"]').first
    
    @property
    def outsystems_logo(self) -> Locator:
        return self.page.locator('img[alt*="OutSystems"], img[alt*="Outsystems"]').first
    
    @property
    def kore_logo(self) -> Locator:
        return self.page.locator('img[alt*="Kore"], img[alt*="KoreAI"]').first
    
    @property
    def uipath_logo(self) -> Locator:
        return self.page.locator('img[alt*="UiPath"], img[alt*="UIPath"]').first
    
    @property
    def onyx_logo(self) -> Locator:
        return self.page.locator('img[alt*="ONYX"], img[alt*="Onyx"]').first
    
    @property
    def trizetto_logo(self) -> Locator:
        return self.page.locator('img[alt*="TriZetto"], img[alt*="Trizetto"]').first
    
    @property
    def e6data_logo(self) -> Locator:
        return self.page.locator('img[alt*="e6data"]').first
    
    @property
    def magical_logo(self) -> Locator:
        return self.page.locator('img[alt*="Magical"]').first
    
    @property
    def health_samurai_logo(self) -> Locator:
        return self.page.locator('img[alt*="health samurai"], img[alt*="Health Samurai"]').first
    
    @property
    def databricks_logo(self) -> Locator:
        return self.page.locator('img[alt*="Databricks"]').first
    
    @property
    def aws_logo(self) -> Locator:
        return self.page.locator('img[alt*="AWS"], img[alt*="Amazon"]').first
    
    @property
    def anthropic_logo(self) -> Locator:
        return self.page.locator('img[alt*="Anthropic"]').first
    
    # Capabilities section
    @property
    def capabilities_section(self) -> Locator:
        return self.page.get_by_text("Capabilities").first
    
    @property
    def ai_capability(self) -> Locator:
        return self.page.get_by_role("heading", name="Artificial Intelligence")
    
    @property
    def engineering_capability(self) -> Locator:
        return self.page.get_by_role("heading", name="Engineering")
    
    @property
    def platforms_capability(self) -> Locator:
        return self.page.get_by_role("heading", name="Platforms")
    
    # Who We Serve section
    @property
    def who_we_serve_section(self) -> Locator:
        return self.page.get_by_text("Who we Serve").first
    
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
    
    # Impact section
    @property
    def impact_section(self) -> Locator:
        return self.page.get_by_text("Impact").first
    
    @property
    def years_experience_metric(self) -> Locator:
        return self.page.getByText("36+ Years", exact=False).first
    
    @property
    def lives_touched_metric(self) -> Locator:
        return self.page.getByText("115+ Million", exact=False).first
    
    @property
    def costs_saved_metric(self) -> Locator:
        return self.page.getByText("$48+ Billion", exact=False).first
    
    @property
    def platforms_launched_metric(self) -> Locator:
        return self.page.getByText("450+", exact=False).first
    
    # Insights section
    @property
    def insights_section(self) -> Locator:
        return self.page.get_by_text("Insights").first
    
    @property
    def insights_cards(self) -> Locator:
        return self.page.locator('[class*="insight-card"], [class*="resource-card"]')
    
    @property
    def insights_prev_button(self) -> Locator:
        return self.page.get_by_role("button", name="Previous")
    
    @property
    def insights_next_button(self) -> Locator:
        return self.page.get_by_role("button", name="Next")
    
    @property
    def insights_carousel_indicators(self) -> Locator:
        return self.page.locator('[class*="carousel-indicator"], [class*="indicator"]')
    
    # Medicare Advantage eBook
    @property
    def medicare_advantage_ebook(self) -> Locator:
        return self.page.get_by_role("link", name="Managing the Margin Reset in Medicare Advantage")
    
    # CMS-0057 eBook
    @property
    def cms_0057_ebook(self) -> Locator:
        return self.page.get_by_role("link", name="CMS-0057: The Interoperability Imperative")
    
    # Life Sciences eBook
    @property
    def life_sciences_ebook(self) -> Locator:
        return self.page.get_by_role("link", name="Unlocking Trusted Digital Transformation in Life Sciences")
    
    # AI ROI eBook
    @property
    def ai_roi_ebook(self) -> Locator:
        return self.page.get_by_role("link", name="Closing the AI ROI Gap in Healthcare")
    
    # FinOps blog
    @property
    def finops_blog(self) -> Locator:
        return self.page.get_by_role("link", name="FinOps Principles")
    
    # Final CTA section
    @property
    def final_cta_section(self) -> Locator:
        return self.page.locator('[class*="final-cta"], [class*="closing-cta"]').first
    
    @property
    def timeline_message(self) -> Locator:
        return self.page.getByText("1 Day · 2 Weeks · 3 Months")
    
    @property
    def final_connect_cta(self) -> Locator:
        return self.page.locator('[class*="final-cta"] a, [class*="closing-cta"] a').last
    
    # Footer
    @property
    def footer(self) -> Locator:
        return self.page.locator("footer").first
    
    @property
    def code_of_conduct_link(self) -> Locator:
        return self.page.get_by_role("link", name="Code of Conduct")
    
    @property
    def privacy_policy_link(self) -> Locator:
        return self.page.get_by_role("link", name="Privacy Policy")
    
    @property
    def transparency_coverage_link(self) -> Locator:
        return self.page.get_by_role("link", name="Transparency in Coverage")
    
    @property
    def cookie_policy_link(self) -> Locator:
        return self.page.get_by_role("link", name="Cookie Policy")
    
    @property
    def accessibility_statement_link(self) -> Locator:
        return self.page.get_by_role("link", name="Accessibility Statement")
    
    @property
    def cookie_preferences_button(self) -> Locator:
        return self.page.get_by_role("button", name="Open cookie settings widget")
    
    # Cookie banner
    @property
    def cookie_banner(self) -> Locator:
        return self.page.locator('[class*="cookie"], [class*="consent"]').first
    
    @property
    def allow_all_cookies_button(self) -> Locator:
        return self.page.get_by_role("button", name="Allow all")
    
    @property
    def customize_cookies_button(self) -> Locator:
        return self.page.get_by_role("button", name="Customize")
    
    # Mobile navigation
    @property
    def mobile_menu_toggle(self) -> Locator:
        return self.page.get_by_role("button", name="Toggle mobile menu")
