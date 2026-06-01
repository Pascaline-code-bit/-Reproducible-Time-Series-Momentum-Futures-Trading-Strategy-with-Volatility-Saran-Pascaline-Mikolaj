"""data_loader.py

Download and preprocess financial data from Yahoo Finance.
"""

import yfinance as yf


class DataLoader:
    """A class to handle downloading and processing financial data."""

    def download_prices(self, tickers, start_date="2010-01-01", end_date="2020-01-01"):
        """Download adjusted close prices from Yahoo Finance.

        Args:
            tickers (list or str): Ticker symbol(s) of the assets to download.
            start_date (str): Start date for data in YYYY-MM-DD format. Defaults to "2010-01-01".
            end_date (str): End date for data in YYYY-MM-DD format. Defaults to "2020-01-01".

        Returns:
            pd.DataFrame or pd.Series: Clean close prices with missing values dropped.
        """
        data = yf.download(tickers, start=start_date, end=end_date, progress=False)

        prices = data["Close"]
        prices = prices.dropna()
        return prices

    def compute_returns(self, prices):
        """Compute daily percentage returns.

        Args:
            prices (pd.DataFrame or pd.Series): Historical price data.

        Returns:
            pd.DataFrame or pd.Series: Daily percentage returns with the first NaN row dropped.
        """
        returns = prices.pct_change()
        returns = returns.dropna()
        return returns
