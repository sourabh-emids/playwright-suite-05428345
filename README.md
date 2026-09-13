# Generated Playwright test suite for Emids Landing Page

This repository contains automated tests for the Emids.com landing page, generated using Playwright and pytest-bdd with the Page Object Model (POM) pattern.

## Test Coverage

This suite covers 55 requirements organized by module:

### Header (emids_lp_001 - emids_lp_008)
- Global header and Emids brand rendering
- Solutions mega-menu functionality
- Capabilities mega-menu functionality
- Industries mega-menu functionality
- Insights navigation group
- Company navigation group
- Connect CTA behavior
- Responsive accessible navigation

### Hero (emids_lp_009 - emids_lp_011)
- Hero messaging and visual rendering
- Hero CTA routing to FDCE
- Media loading optimization

### How We Deliver (emids_lp_012 - emids_lp_013)
- Section rendering
- See the model CTA functionality

### Global (emids_lp_014)
- Semantic section hierarchy
- Heading structure validation

### Featured Solutions (emids_lp_015 - emids_lp_017)
- Six solution cards rendering
- All Solutions CTA
- Responsive interaction support

### Partnerships (emids_lp_018 - emids_lp_019)
- Partner logo rail/marquee
- Reduced motion support

### Capabilities (emids_lp_020 - emids_lp_023)
- Capabilities overview
- AI capability content
- Engineering capability content
- Platforms capability content

### Who We Serve (emids_lp_024)
- Five audience industry entries

### Impact (emids_lp_025)
- Proof metrics rendering

### Insights (emids_lp_026 - emids_lp_033)
- Insights section and cards
- eBook cards (Medicare Advantage, Life Sciences, AI ROI, FinOps)
- Blog cards
- Resource access handoff

### Final CTA (emids_lp_034 - emids_lp_035)
- Final conversion banner
- Delivery message timeline

### Footer (emids_lp_036, emids_lp_045 - emids_lp_046)
- Cookie Preferences control
- Legal navigation
- Corporate contact information

### Contact (emids_lp_047 - emids_lp_049)
- Contact form fields and validation
- Inquiry Type values
- Form submission feedback

### Analytics (emids_lp_037 - emids_lp_042)
- GTM integration
- GA measurement
- Campaign attribution
- Marketo integration
- LinkedIn marketing tags
- ZoomInfo WebSights

### Media (emids_lp_043 - emids_lp_044)
- Wistia embeds
- YouTube embeds

### SEO (emids_lp_051)
- Metadata and crawlable structure

### Global Requirements (emids_lp_050, emids_lp_052 - emids_lp_055)
- WCAG 2.1 AA compliance
- Responsive layout
- Performance and Core Web Vitals
- Script failure handling
- Modal behavior

## Directory Structure

```
tests/
├── features/           # Gherkin feature files
│   ├── emids_lp_001_render_global_header.feature
│   ├── emids_lp_002_solutions_mega_menu.feature
│   └── ... (55 feature files total)
├── steps/             # Step definition files
│   ├── emids_lp_001_render_global_header_steps.py
│   ├── emids_lp_002_solutions_mega_menu_steps.py
│   └── ... (step files)
└── test_*.py          # Test runner files

pages/                 # Page objects
├── header/
│   ├── header_page.py
│   ├── solutions_menu_page.py
│   ├── capabilities_menu_page.py
│   ├── industries_menu_page.py
│   ├── insights_nav_page.py
│   ├── company_nav_page.py
│   └── connect_cta_page.py
├── hero/hero_page.py
├── how_we_deliver/how_we_deliver_page.py
├── featured_solutions/featured_solutions_page.py
├── partnerships/partnerships_page.py
├── capabilities/capabilities_section_page.py
├── who_we_serve/who_we_serve_page.py
├── impact/impact_page.py
└── ...

locators/               # Locator definitions
├── emids_lp_001_header_locators.py
├── emids_lp_002_solutions_menu_locators.py
└── ...

utils/
└── config.py           # Configuration (BASE_URL from env)
```

## Running Tests

Requires [uv](https://docs.astral.sh/uv/) - no separate virtualenv/pip step.

```bash
# Install dependencies
uv sync
uv run playwright install --with-deps chromium

# Copy and configure environment
cp .env.example .env   # then fill in BASE_URL

# Run all tests
make test

# Run tests with visible browser (debugging)
make test-headed

# View HTML report
make report
```

## Test Execution

- Tests run in parallel with pytest-xdist (`-n auto`)
- On failure: traces, screenshots, and videos are captured
- HTML report generated at `reports/report.html`
- JUnit XML report at `reports/junit.xml`

## Key Test Features

- **BDD-style**: Gherkin feature files with clear scenario descriptions
- **POM Pattern**: Page objects encapsulate locators and interactions
- **Accessibility Testing**: WCAG 2.1 AA compliance checks
- **Responsive Testing**: Multiple viewport configurations
- **Reduced Motion**: Respects user preferences
- **Error Handling**: Graceful degradation testing
- **Consent Management**: Privacy-focused testing (GTM, analytics, marketing)

## Notes

- BASE_URL must be set in `.env` file (defaults to `https://www.emids.com`)
- Some tests simulate edge cases (JS disabled, slow networks, etc.)
- Test suite is designed to run against production-like environments
