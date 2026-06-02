FROM python:3.11-slim

RUN apt-get update && apt-get install -y \
    curl \
    gdebi-core \
    && rm -rf /var/lib/apt/lists/*

RUN curl -LO https://github.com/quarto-dev/quarto-cli/releases/download/v1.4.549/quarto-1.4.549-linux-amd64.deb \
    && gdebi --non-interactive quarto-1.4.549-linux-amd64.deb \
    && rm quarto-1.4.549-linux-amd64.deb

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY src/ ./src/
COPY report/ ./report/
COPY Makefile .

CMD ["sh", "-c", "mkdir -p /app/output && quarto render report/report.qmd && cp report/report.html /app/output/report.html"]
