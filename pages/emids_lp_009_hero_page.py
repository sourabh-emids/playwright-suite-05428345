"""Page object for emids_lp_009-011 - Hero sections."""
from playwright.sync_api import Page, Locator
from pages.base_page import BasePage


class HeroPage(BasePage):
    """Page object for hero section."""

    @property
    def hero_section(self) -> Locator:
        return self.page.locator("section.hero, .hero, [class*='hero']").first

    @property
    def h1(self) -> Locator:
        return self.page.locator("h1").first

    @property
    def h1_elements(self) -> Locator:
        return self.page.locator("h1")

    @property
    def eyebrow(self) -> Locator:
        return self.page.locator(".hero-eyebrow, .eyebrow, [class*='eyebrow']").first

    @property
    def body_copy(self) -> Locator:
        return self.page.locator(".hero-body, .hero p").first

    @property
    def cta(self) -> Locator:
        return self.page.locator(".hero a, .hero button").first

    @property
    def hero_media(self) -> Locator:
        return self.page.locator(".hero img, .hero video, .hero picture").first


class HeroCTAPage(BasePage):
    """Page object for hero CTA."""

    @property
    def hero_cta(self) -> Locator:
        return self.page.locator(".hero a:has-text('See How'), .hero a.primary, .hero a.cta").first

    def click_hero_cta(self) -> None:
        self.hero_cta.click()


class HeroOptimizationPage(BasePage):
    """Page object for hero optimization."""

    @property
    def hero_section(self) -> Locator:
        return self.page.locator("section.hero, .hero").first

    @property
    def hero_text(self) -> Locator:
        return self.page.locator(".hero h1, .hero h2, .hero p").first

    @property
    def hero_media(self) -> Locator:
        return self.page.locator(".hero img, .hero video").first


class HowWeDeliverPage(BasePage):
    """Page object for How We Deliver section."""

    @property
    def section(self) -> Locator:
        return self.page.locator("section.how-we-deliver, section[class*='deliver']").first

    @property
    def section_heading(self) -> Locator:
        return self.page.locator("section.how-we-deliver h2, section[class*='deliver'] h2").first

    @property
    def section_body(self) -> Locator:
        return self.page.locator("section.how-we-deliver p, section[class*='deliver'] p").first

    @property
    def see_model_cta(self) -> Locator:
        return self.page.locator("a:has-text('See the model'), button:has-text('See the model')").first

    @property
    def all_headings(self) -> Locator:
        return self.page.locator("section.how-we-deliver h1, section.how-we-deliver h2, section.how-we-deliver h3, section.how-we-deliver h4")


class SeeModelCTAPage(BasePage):
    """Page object for See the model CTA."""

    @property
    def see_model_cta(self) -> Locator:
        return self.page.locator("a:has-text('See the model'), button:has-text('See the model')").first


class FeaturedSolutionsPage(BasePage):
    """Page object for Featured Solutions section."""

    @property
    def section(self) -> Locator:
        return self.page.locator("section.featured-solutions, section[class*='solutions']").first

    @property
    def solution_cards(self) -> Locator:
        return self.page.locator(".solution-card, [class*='solution'] article, section.solutions article")

    @property
    def solution_numbers(self) -> Locator:
        return self.page.locator(".solution-number, [class*='number']")

    @property
    def solution_titles(self) -> Locator:
        return self.page.locator(".solution-card h3, [class*='solution'] h3")

    @property
    def solution_links(self) -> Locator:
        return self.page.locator(".solution-card a, [class*='solution'] a")


class AllSolutionsCTAPage(BasePage):
    """Page object for All Solutions CTA."""

    @property
    def all_solutions_cta(self) -> Locator:
        return self.page.locator("a:has-text('All Solutions'), a:has-text('View All'), a[href='/solutions/']").first


class SolutionsInteractionPage(BasePage):
    """Page object for solutions interaction."""

    @property
    def section(self) -> Locator:
        return self.page.locator("section.featured-solutions").first

    @property
    def solution_cards(self) -> Locator:
        return self.page.locator(".solution-card")

    @property
    def carousel_controls(self) -> Locator:
        return self.page.locator(".carousel button, [class*='carousel'] button")


class PartnerLogosPage(BasePage):
    """Page object for partner logos."""

    @property
    def section(self) -> Locator:
        return self.page.locator("section.partners, section[class*='partner']").first

    @property
    def partner_logos(self) -> Locator:
        return self.page.locator(".partner-logo img, [class*='partner'] img")


class PartnerAnimationPage(BasePage):
    """Page object for partner animation."""

    @property
    def section(self) -> Locator:
        return self.page.locator("section.partners").first

    @property
    def partner_logos(self) -> Locator:
        return self.page.locator(".partner-logo img")


class CapabilitiesPage(BasePage):
    """Page object for capabilities section."""

    @property
    def section(self) -> Locator:
        return self.page.locator("section.capabilities").first

    @property
    def ai_group(self) -> Locator:
        return self.page.locator("[class*='capability']:has-text('AI')").first

    @property
    def engineering_group(self) -> Locator:
        return self.page.locator("[class*='capability']:has-text('Engineering')").first

    @property
    def platforms_group(self) -> Locator:
        return self.page.locator("[class*='capability']:has-text('Platforms')").first

    @property
    def ai_label(self) -> Locator:
        return self.page.locator("h3:has-text('AI'), .capability h4:has-text('AI')").first

    @property
    def engineering_label(self) -> Locator:
        return self.page.locator("h3:has-text('Engineering'), .capability h4:has-text('Engineering')").first

    @property
    def platforms_label(self) -> Locator:
        return self.page.locator("h3:has-text('Platforms'), .capability h4:has-text('Platforms')").first

    @property
    def ai_link(self) -> Locator:
        return self.page.locator("a[href*='/ai/'], a[href*='/capabilities/']").first

    @property
    def ai_title(self) -> Locator:
        return self.page.locator(".capability h3:has-text('AI'), .capability h4:has-text('AI')").first

    @property
    def ai_card(self) -> Locator:
        return self.page.locator(".capability-card:has-text('AI')").first


class WhoWeServePage(BasePage):
    """Page object for Who We Serve section."""

    @property
    def section(self) -> Locator:
        return self.page.locator("section.who-we-serve, section[class*='audience']").first

    @property
    def payer_tab(self) -> Locator:
        return self.page.locator("button:has-text('Payer'), a:has-text('Payer')").first

    @property
    def provider_tab(self) -> Locator:
        return self.page.locator("button:has-text('Provider'), a:has-text('Provider')").first

    @property
    def healthtech_tab(self) -> Locator:
        return self.page.locator("button:has-text('HealthTech'), a:has-text('HealthTech')").first

    @property
    def life_sciences_tab(self) -> Locator:
        return self.page.locator("button:has-text('Life Sciences'), a:has-text('Life Sciences')").first

    @property
    def consumer_tab(self) -> Locator:
        return self.page.locator("button:has-text('Consumer'), a:has-text('Consumer')").first

    @property
    def audience_tabs(self) -> Locator:
        return self.page.locator("section.who-we-serve button, section[class*='audience'] button")

    @property
    def explore_cta(self) -> Locator:
        return self.page.locator("a:has-text('Explore'), button:has-text('Explore')")


class ImpactPage(BasePage):
    """Page object for Impact metrics section."""

    @property
    def section(self) -> Locator:
        return self.page.locator("section.impact, section[class*='metrics'], section[class*='impact']").first

    @property
    def metric_1(self) -> Locator:
        return self.page.locator("text=36, text=Years Healthcare").first

    @property
    def metric_2(self) -> Locator:
        return self.page.locator("text=115, text=Million Lives").first

    @property
    def metric_3(self) -> Locator:
        return self.page.locator("text=48, text=Billion").first

    @property
    def metric_4(self) -> Locator:
        return self.page.locator("text=450, text=Platforms").first


class InsightsPage(BasePage):
    """Page object for Insights section."""

    @property
    def section(self) -> Locator:
        return self.page.locator("section.insights, section[class*='insights']").first

    @property
    def insight_cards(self) -> Locator:
        return self.page.locator(".insight-card, [class*='insight'] article")

    @property
    def download_buttons(self) -> Locator:
        return self.page.locator("a:has-text('Download'), button:has-text('Download')")


class FinalCTAPage(BasePage):
    """Page object for Final CTA section."""

    @property
    def final_cta_banner(self) -> Locator:
        return self.page.locator("section.final-cta, section[class*='cta'], section[class*='conversion']").first

    @property
    def primary_cta(self) -> Locator:
        return self.page.locator("section.final-cta a.primary, section[class*='cta'] a.primary, section.final-cta a").first

    @property
    def supporting_message(self) -> Locator:
        return self.page.locator("section.final-cta p, section[class*='cta'] p").first


class DeliveryMessagePage(BasePage):
    """Page object for delivery message section."""

    @property
    def section(self) -> Locator:
        return self.page.locator("section.delivery, section[class*='delivery']").first

    @property
    def timing_labels(self) -> Locator:
        return self.page.locator("text=1 Day, text=2 Weeks, text=3 Months")


class CookiePreferencesPage(BasePage):
    """Page object for Cookie Preferences."""

    @property
    def cookie_preferences_control(self) -> Locator:
        return self.page.locator("a:has-text('Cookie Preferences'), button:has-text('Cookie'), [aria-controls*='consent']").first

    @property
    def consent_modal(self) -> Locator:
        return self.page.locator("[role='dialog'], .consent-modal, #consent-modal")


class GTMPage(BasePage):
    """Page object for GTM integration."""

    @property
    def hero_section(self) -> Locator:
        return self.page.locator(".hero, section.hero").first

    @property
    def navigation(self) -> Locator:
        return self.page.locator("header nav").first


class AnalyticsPage(BasePage):
    """Page object for analytics integration."""

    @property
    def hero_section(self) -> Locator:
        return self.page.locator(".hero, section.hero").first


class AttributionPage(BasePage):
    """Page object for attribution parameters."""

    @property
    def hero_section(self) -> Locator:
        return self.page.locator(".hero, section.hero").first


class MarketoPage(BasePage):
    """Page object for Marketo integration."""

    @property
    def hero_section(self) -> Locator:
        return self.page.locator(".hero, section.hero").first


class LinkedInPage(BasePage):
    """Page object for LinkedIn integration."""

    @property
    def hero_section(self) -> Locator:
        return self.page.locator(".hero, section.hero").first


class ZoomInfoPage(BasePage):
    """Page object for ZoomInfo integration."""

    @property
    def hero_section(self) -> Locator:
        return self.page.locator(".hero, section.hero").first


class WistiaPage(BasePage):
    """Page object for Wistia integration."""

    @property
    def hero_section(self) -> Locator:
        return self.page.locator(".hero, section.hero").first


class YouTubePage(BasePage):
    """Page object for YouTube integration."""

    @property
    def hero_section(self) -> Locator:
        return self.page.locator(".hero, section.hero").first


class FooterLegalPage(BasePage):
    """Page object for footer legal section."""

    @property
    def legal_section(self) -> Locator:
        return self.page.locator("footer nav.legal, footer [class*='legal']").first

    @property
    def legal_links(self) -> Locator:
        return self.page.locator("footer a[href*='privacy'], footer a[href*='cookie'], footer a[href*='accessibility']")


class FooterCorporatePage(BasePage):
    """Page object for footer corporate section."""

    @property
    def corporate_section(self) -> Locator:
        return self.page.locator("footer [class*='corporate'], footer [class*='contact']").first

    @property
    def social_links(self) -> Locator:
        return self.page.locator("footer a[href*='facebook'], footer a[href*='twitter'], footer a[href*='linkedin']")


class ContactFormPage(BasePage):
    """Page object for contact form."""

    @property
    def first_name(self) -> Locator:
        return self.page.locator("input[name*='first'], input[id*='first']").first

    @property
    def last_name(self) -> Locator:
        return self.page.locator("input[name*='last'], input[id*='last']").first

    @property
    def email(self) -> Locator:
        return self.page.locator("input[type='email'], input[name*='email']").first

    @property
    def company(self) -> Locator:
        return self.page.locator("input[name*='company'], input[id*='company']").first

    @property
    def title_field(self) -> Locator:
        return self.page.locator("input[name*='title'], input[id*='title']").first

    @property
    def phone(self) -> Locator:
        return self.page.locator("input[type='tel'], input[name*='phone']").first

    @property
    def inquiry_type(self) -> Locator:
        return self.page.locator("select[name*='inquiry'], select[id*='inquiry']").first

    @property
    def comments(self) -> Locator:
        return self.page.locator("textarea[name*='comment'], textarea[name*='message']").first

    @property
    def submit_button(self) -> Locator:
        return self.page.locator("button[type='submit'], input[type='submit']").first

    @property
    def success_message(self) -> Locator:
        return self.page.locator("[role='alert']:has-text('success'), .success:visible").first

    @property
    def error_message(self) -> Locator:
        return self.page.locator("[role='alert']:has-text('error'), .error:visible").first

    @property
    def email_error(self) -> Locator:
        return self.page.locator("[aria-invalid='true']").first

    def fill_valid_form(self) -> None:
        self.first_name.fill("John")
        self.last_name.fill("Doe")
        self.email.fill("john@example.com")
        self.company.fill("Acme Inc")
        self.title_field.fill("Manager")
        self.phone.fill("555-1234")
        self.inquiry_type.select_option("Services")
        self.comments.fill("Test message")


class InquiryTypePage(BasePage):
    """Page object for inquiry type field."""

    @property
    def inquiry_type(self) -> Locator:
        return self.page.locator("select[name*='inquiry'], select[id*='inquiry']").first

    @property
    def inquiry_options(self) -> Locator:
        return self.page.locator("select[name*='inquiry'] option")

    @property
    def submit_button(self) -> Locator:
        return self.page.locator("button[type='submit']").first

    @property
    def inquiry_error(self) -> Locator:
        return self.page.locator("[aria-invalid='true']").first


class FormFeedbackPage(BasePage):
    """Page object for form feedback."""

    @property
    def form(self) -> Locator:
        return self.page.locator("form").first

    @property
    def first_name(self) -> Locator:
        return self.page.locator("input[name*='first']").first

    @property
    def submit_button(self) -> Locator:
        return self.page.locator("button[type='submit']").first

    @property
    def success_message(self) -> Locator:
        return self.page.locator("[role='alert']:has-text('success')").first

    def fill_valid_form(self) -> None:
        self.first_name.fill("John")


class WCAGPage(BasePage):
    """Page object for WCAG compliance checks."""

    @property
    def hero_section(self) -> Locator:
        return self.page.locator(".hero, section.hero").first

    @property
    def form_section(self) -> Locator:
        return self.page.locator("form").first

    @property
    def all_interactive(self) -> Locator:
        return self.page.locator("button, a, input, select, textarea")

    @property
    def images(self) -> Locator:
        return self.page.locator("img")

    @property
    def buttons(self) -> Locator:
        return self.page.locator("button")


class SEOPage(BasePage):
    """Page object for SEO checks."""

    @property
    def h1(self) -> Locator:
        return self.page.locator("h1").first

    @property
    def navigation(self) -> Locator:
        return self.page.locator("header nav").first


class ResponsivePage(BasePage):
    """Page object for responsive layout checks."""

    @property
    def hero_section(self) -> Locator:
        return self.page.locator(".hero, section.hero").first

    @property
    def h1(self) -> Locator:
        return self.page.locator("h1").first

    @property
    def navigation(self) -> Locator:
        return self.page.locator("header nav").first


class PerformancePage(BasePage):
    """Page object for performance checks."""

    @property
    def h1(self) -> Locator:
        return self.page.locator("h1").first

    @property
    def hero_section(self) -> Locator:
        return self.page.locator(".hero, section.hero").first

    @property
    def images(self) -> Locator:
        return self.page.locator("img")


class ScriptFailurePage(BasePage):
    """Page object for script failure scenarios."""

    @property
    def hero_section(self) -> Locator:
        return self.page.locator(".hero, section.hero").first

    @property
    def navigation(self) -> Locator:
        return self.page.locator("header nav").first

    @property
    def cta(self) -> Locator:
        return self.page.locator(".hero a, .cta").first

    @property
    def footer(self) -> Locator:
        return self.page.locator("footer").first


class ModalPage(BasePage):
    """Page object for modal behavior."""

    @property
    def modal(self) -> Locator:
        return self.page.locator("[role='dialog'], .modal, #modal")

    @property
    def close_button(self) -> Locator:
        return self.page.locator("[role='dialog'] button.close, .modal button.close").first

    @property
    def hero_section(self) -> Locator:
        return self.page.locator(".hero, section.hero").first
