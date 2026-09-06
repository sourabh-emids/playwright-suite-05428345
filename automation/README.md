# Emids web automation

Python Playwright tests for TC-01 through TC-05, implemented with
`pytest-bdd` and a shared Page Object Model. Locators were inspected on the
live Emids website. The current site labels its primary contact and learn
CTAs **Connect** and **See How We Deliver Outcomes**, so the scenarios use
those live accessible names.

## Setup

```bash
uv sync
uv run playwright install chromium
```

## Run

```bash
uv run pytest
```

The suite targets `https://www.emids.com` by default. Override it without
changing test code when needed:

```bash
EMIDS_BASE_URL=https://www.emids.com uv run pytest
```

TC-05 intentionally enforces validation feedback for every required field,
as stated in its acceptance criteria.
