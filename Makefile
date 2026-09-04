.PHONY: install test test-headed report clean

install:
	pip install -r requirements.txt
	playwright install --with-deps chromium

test:
	pytest -n auto

test-headed:
	pytest --headed -n0

report:
	python -m http.server --directory reports 8000

clean:
	rm -rf reports .auth .pytest_cache
