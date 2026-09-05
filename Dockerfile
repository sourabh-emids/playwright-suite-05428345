FROM mcr.microsoft.com/playwright/python:v1.49.0-jammy

WORKDIR /suite
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["pytest", "-n", "auto"]
