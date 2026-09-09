FROM mcr.microsoft.com/playwright/python:v1.49.0-jammy

WORKDIR /suite

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /usr/local/bin/

COPY pyproject.toml .
RUN uv sync

COPY . .

CMD ["uv", "run", "pytest", "-n", "auto"]
