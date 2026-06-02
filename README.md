# Reproducible-Research-Project-Saran-Mikolaj
Reproducible Research Project (Saran, Mikolaj)

# Reproducible Time-Series Momentum Strategy

This project reproduces and extends the methodology from:

Moskowitz, Ooi, Pedersen (2012)
"Time Series Momentum"

## Reproducible Execution via Docker

You will need Docker (and Docker Desktop on Windows) to generate the report

This project is fully containerized and hosted on Docker Hub. Running the image executes the momentum strategy backtest and auto-compiles the final HTML report without requiring a local Python installation.

Open your terminal (PowerShell on Windows, Terminal on Mac/Linux) and create an empty directory:

```bash
mkdir tsmom-evaluation
```

```bash
cd tsmom-evaluation
```

Run the command matching your operating system. This mounts a local output/ folder to safely capture the generated report before the container automatically deletes itself upon exit.

On Mac, Linux, or Git Bash, run:
```
docker run --rm -v "$(pwd)/output:/app/output" teafox56a/tsmom-framework:latest
```
On Windows PowerShell, run:
```
docker run --rm -v "${PWD}/output:/app/output" teafox56a/tsmom-framework:latest
```
Once the console streams finish processing the portfolio data, look inside your newly created local workspace.

Go to the output/ directory and open report.html.

## Progress Log

### Day 1
- Project setup
- Financial data download
- Return computation
- Baseline momentum signal implementation

### Day 2
- Vectorized backtesting engine
- Portfolio aggregation
- Benchmark comparison
- Performance metrics
- Strategy visualization

### Day 3
- Multi-horizon momentum (1, 3, 6, 12 months)
- Overlapping portfolios
- Volatility scaling
- Cross-asset portfolio

### Day 4 - Cleaning
- Wrapped functions in backtest, data_loader, performance, and signals into classes
- Added docstrings to all methods for Sphinx documentation
- Configured Sphinx
- Added .pre-commit-config.yaml
- Updated .gitignore and requirements.txt

### Day 4 - Reporting
- Created the foundation for the report
- Updated .gitignore and requirements.txt

### Day 5
- Implement pytest suite to validate data loading, signals, and backtesting
- Configure .gitignore and .dockerignore to exclude testing artifacts
- Create README documentation for running the public Docker image
- Add pytest dependencies to requirements.txt
