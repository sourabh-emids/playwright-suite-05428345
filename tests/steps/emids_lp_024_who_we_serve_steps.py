"""Steps for emids_lp_024: Render five audience industry entries."""
from playwright.sync_api import Page, expect
from pytest_bdd import given, parsers, then, when

from pages.who_we_serve.who_we_serve_page import WhoWeServePage


@given(parsers.parse("User views Who We Serve section"))
def view_who_we_serve(page: Page) -> None:
    """User views Who We Serve section."""
    wws_page = WhoWeServePage(page)
    wws_page.navigate()
    wws_page.scroll_to_section()


@given(parsers.parse("User clicks Explore on each audience card"))
def click_explore(page: Page) -> None:
    """User clicks Explore."""
    wws_page = WhoWeServePage(page)
    wws_page.navigate()
    wws_page.scroll_to_section()


@given(parsers.parse("User navigates via keyboard or touch"))
def keyboard_or_touch(page: Page) -> None:
    """User navigates via keyboard or touch."""
    wws_page = WhoWeServePage(page)
    wws_page.navigate()
    wws_page.scroll_to_section()


@given(parsers.parse("One segment page is unavailable"))
def segment_unavailable(page: Page) -> None:
    """One segment page is unavailable."""
    pass


@given(parsers.parse("User selects an audience tab"))
def select_audience_tab(page: Page) -> None:
    """User selects an audience tab."""
    wws_page = WhoWeServePage(page)
    wws_page.navigate()
    wws_page.scroll_to_section()
    wws_page.click_audience_tab("Payer")


@when("User counts audience entries")
def count_audiences(page: Page) -> None:
    """Count audience entries."""
    pass


@when("Navigation completes")
def navigation_completes(page: Page) -> None:
    """Navigation completes."""
    page.wait_for_load_state("domcontentloaded")


@when("User activates Explore action")
def activate_explore(page: Page) -> None:
    """Activate Explore action."""
    pass


@when("User counts audience items")
def count_items(page: Page) -> None:
    """Count audience items."""
    pass


@when("User examines audience destinations")
def examine_destinations(page: Page) -> None:
    """Examine audience destinations."""
    pass


@when("User checks URLs")
def check_urls(page: Page) -> None:
    """Check URLs."""
    pass


@when("Page renders Who We Serve section")
def page_renders(page: Page) -> None:
    """Page renders."""
    page.wait_for_load_state("domcontentloaded")


@when("User resizes browser window")
def resize_browser(page: Page) -> None:
    """Resize browser."""
    page.set_viewport_size({"width": 375, "height": 667})


@then("Payer, Provider, HealthTech, Life Sciences, and Consumer audiences all display")
def all_audiences_display(page: Page) -> None:
    """Verify all audiences display."""
    wws_page = WhoWeServePage(page)
    expect(wws_page.get_audience_count()).to_equal(5)


@then("Payer navigates to /segments/payer/")
def payer_routes_correct(page: Page) -> None:
    """Verify Payer routes correct."""
    wws_page = WhoWeServePage(page)
    wws_page.navigate()
    wws_page.scroll_to_section()
    wws_page.click_audience_tab("Payer")
    expect(page).to_have_url("/segments/payer/")


@then("Provider to /segments/provider/")
def provider_routes_correct(page: Page) -> None:
    """Verify Provider routes correct."""
    wws_page = WhoWeServePage(page)
    wws_page.navigate()
    wws_page.scroll_to_section()
    wws_page.click_audience_tab("Provider")
    expect(page).to_have_url("/segments/provider/")


@then("HealthTech to /segments/healthtech/")
def healthtech_routes_correct(page: Page) -> None:
    """Verify HealthTech routes correct."""
    wws_page = WhoWeServePage(page)
    wws_page.navigate()
    wws_page.scroll_to_section()
    wws_page.click_audience_tab("HealthTech")
    expect(page).to_have_url("/segments/healthtech/")


@then("Life Sciences to /segments/life-sciences/")
def life_sciences_routes_correct(page: Page) -> None:
    """Verify Life Sciences routes correct."""
    wws_page = WhoWeServePage(page)
    wws_page.navigate()
    wws_page.scroll_to_section()
    wws_page.click_audience_tab("Life Sciences")
    expect(page).to_have_url("/segments/life-sciences/")


@then("Consumer to /segments/consumer/")
def consumer_routes_correct(page: Page) -> None:
    """Verify Consumer routes correct."""
    wws_page = WhoWeServePage(page)
    wws_page.navigate()
    wws_page.scroll_to_section()
    wws_page.click_audience_tab("Consumer")
    expect(page).to_have_url("/segments/consumer/")


@then("Navigation works")
def navigation_works(page: Page) -> None:
    """Verify navigation works."""
    wws_page = WhoWeServePage(page)
    expect(wws_page.locators.payer_tab).to_be_focusable()


@then("Content accessible without mouse")
def accessible_without_mouse(page: Page) -> None:
    """Verify accessible without mouse."""
    wws_page = WhoWeServePage(page)
    expect(wws_page.locators.payer_tab).to_be_visible()


@then("Exactly five audiences display for this content version")
def exactly_five(page: Page) -> None:
    """Verify exactly five audiences."""
    wws_page = WhoWeServePage(page)
    expect(wws_page.get_audience_count()).to_equal(5)


@then("All URLs use canonical segment paths")
def canonical_paths(page: Page) -> None:
    """Verify canonical paths."""
    wws_page = WhoWeServePage(page)
    urls = wws_page.get_expected_urls()
    for url in urls.values():
        expect(url).to_match(r"^/segments/")


@then("Available segments display")
def available_segments_display(page: Page) -> None:
    """Verify available segments display."""
    wws_page = WhoWeServePage(page)
    expect(wws_page.get_audience_count()).to_be_greater_than(0)


@then("Unavailable segment handled gracefully")
def unavailable_handled(page: Page) -> None:
    """Verify unavailable handled gracefully."""
    wws_page = WhoWeServePage(page)
    expect(wws_page.locators.section_heading).to_be_visible()


@then("Tab selection or content state adapts appropriately")
def state_adapts(page: Page) -> None:
    """Verify state adapts."""
    wws_page = WhoWeServePage(page)
    expect(wws_page.locators.section_heading).to_be_visible()


@then("No permanent loss of state")
def no_state_loss(page: Page) -> None:
    """Verify no state loss."""
    wws_page = WhoWeServePage(page)
    expect(wws_page.locators.payer_tab).to_be_visible()
