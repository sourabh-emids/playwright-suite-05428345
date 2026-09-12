.PHONY: install test test-headed report clean

install:
	uv sync
	uv run playwright install --with-deps chromium

test:
	uv run pytest -n auto

test-headed:
	uv run pytest --headed -n0

report:
	uv run python -m http.server --directory reports 8000

clean:
	rm -rf reports .auth .pytest_cache .venv
