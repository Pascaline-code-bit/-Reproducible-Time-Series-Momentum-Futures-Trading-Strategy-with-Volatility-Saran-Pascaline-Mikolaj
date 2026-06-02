FROM python:3.11-slim

RUN apt-get update && apt-get install -y \
    curl \
    gdebi-core \
    make \
    && rm -rf /var/lib/apt/lists/*

RUN ARCH=$(dpkg --print-architecture) \
    && if [ "$ARCH" = "arm64" ]; then QUARTO_ARCH="arm64"; else QUARTO_ARCH="amd64"; fi \
    && curl -LO "https://github.com/quarto-dev/quarto-cli/releases/download/v1.4.549/quarto-1.4.549-linux-${QUARTO_ARCH}.deb" \
    && gdebi --non-interactive "quarto-1.4.549-linux-${QUARTO_ARCH}.deb" \
    && rm "quarto-1.4.549-linux-${QUARTO_ARCH}.deb"

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY src/ ./src/
COPY report/ ./report/
COPY tests/ ./tests/
COPY docs/ ./docs/
COPY Makefile .

# Executed when the container runs:
# 1. Runs pytest. 2. Builds Sphinx docs. 3. Prepares output folder. 4. Renders Quarto report.
CMD ["sh", "-c", "make test && make sphinx-build && mkdir -p /app/output && quarto render report/report.qmd && cp report/report.html /app/output/report.html"]
