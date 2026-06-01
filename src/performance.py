"""performance.py

Performance metrics to evaluate trading strategy results.
"""

import numpy as np


class PerformanceMetrics:
    """A class to compute key financial performance metrics for trading strategies."""

    def annualized_return(self, returns, periods=252):
        """Compute annualized return.

        Args:
            returns (pd.Series or pd.DataFrame): Historical daily returns.
            periods (int): Number of trading periods in a year. Defaults to 252 (daily data).

        Returns:
            float or pd.Series: The annualized average return.
        """
        return returns.mean() * periods

    def annualized_volatility(self, returns, periods=252):
        """Compute annualized volatility.

        Args:
            returns (pd.Series or pd.DataFrame): Historical daily returns.
            periods (int): Number of trading periods in a year. Defaults to 252 (daily data).

        Returns:
            float or pd.Series: The annualized standard deviation of returns.
        """
        return returns.std() * np.sqrt(periods)

    def sharpe_ratio(self, returns, risk_free_rate=0.0, periods=252):
        """Compute annualized Sharpe ratio.

        Args:
            returns (pd.Series or pd.DataFrame): Historical daily returns.
            risk_free_rate (float): Annual risk-free rate. Defaults to 0.0.
            periods (int): Number of trading periods in a year. Defaults to 252 (daily data).

        Returns:
            float or pd.Series: The annualized Sharpe ratio (excess return per unit of volatility).
        """
        excess_returns = returns - risk_free_rate / periods
        ann_return = excess_returns.mean() * periods
        ann_vol = excess_returns.std() * np.sqrt(periods)
        return ann_return / ann_vol

    def max_drawdown(self, cumulative_returns):
        """Compute maximum drawdown.

        Args:
            cumulative_returns (pd.Series or pd.DataFrame): Continuous cumulative returns series.

        Returns:
            float or pd.Series: The peak-to-trough maximum percentage drop.
        """
        running_max = cumulative_returns.cummax()
        drawdown = (cumulative_returns - running_max) / running_max
        return drawdown.min()
