"""Step definitions for issue_0010 - Hero CTA routing to FDCE experience."""
from pytest_bdd import given, then, when

from pages.issue_0010_hero_cta_page import Issue0010HeroCTAPage


@given("I navigate to the homepage")
def navigate_to_homepage(page: Issue0010HeroCTAPage):
    """Navigate to the homepage."""
    page.page.goto("/")


@when("I view the hero section")
def view_hero_section(page: Issue0010HeroCTAPage):
    """View the hero section."""
    pass


@then('the "See How We Deliver Outcomes" CTA should be visible')
def hero_cta_visible(page: Issue0010HeroCTAPage):
    """Verify hero CTA is visible."""
    page.hero_cta_should_be_visible()


@then("the CTA should link to the FDCE page")
def cta_links_to_fdce(page: Issue0010HeroCTAPage):
    """Verify CTA links to FDCE page."""
    page.cta_should_link_to_fdce_page()


@when('I click the "See How We Deliver Outcomes" CTA')
def click_hero_cta(page: Issue0010HeroCTAPage):
    """Click the hero CTA."""
    page.click_hero_cta()


@then("I should be navigated to the FDCE page")
def on_fdce_page(page: Issue0010HeroCTAPage):
    """Verify user is on the FDCE page."""
    page.should_be_on_fdce_page()
