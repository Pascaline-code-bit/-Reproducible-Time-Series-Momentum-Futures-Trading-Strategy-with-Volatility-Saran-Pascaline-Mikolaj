"""backtest.py

Backtesting utilities for Time-Series Momentum trading strategies.
"""


class Backtester:
    """A class containing utilities for backtesting trading strategies."""

    def compute_strategy_returns(self, returns, signals):
        """Compute returns from strategy.

        Args:
            returns (pd.Series or pd.DataFrame): Historical asset returns.
            signals (pd.Series or pd.DataFrame): Generated trading signals.

        Returns:
            pd.Series or pd.DataFrame: Strategy returns with NaN values dropped.
        """
        strategy_returns = signals * returns
        strategy_returns = strategy_returns.dropna()
        return strategy_returns

    def compute_overlapping_returns(self, returns, signals_dict):
        """Average signals across multiple horizons.

        Args:
            returns (pd.Series or pd.DataFrame): Historical asset returns.
            signals_dict (dict): Dictionary containing signals for different horizons.

        Returns:
            pd.Series or pd.DataFrame: Averaged strategy returns.
        """
        combined = None

        for sig in signals_dict.values():
            strat = sig * returns

            if combined is None:
                combined = strat
            else:
                combined += strat

        combined = combined / len(signals_dict)
        return combined

    def compute_vol_scaled_returns(self, returns, signals, target_vol=0.1):
        """Volatility scaling.

        Args:
            returns (pd.Series or pd.DataFrame): Historical asset returns.
            signals (pd.Series or pd.DataFrame): Trading signals.
            target_vol (float): Annualized target volatility. Defaults to 0.1.

        Returns:
            pd.Series or pd.DataFrame: Volatility-scaled strategy returns.
        """
        vol = returns.rolling(60).std()

        scaling = target_vol / vol
        scaling = scaling.clip(lower=0.5, upper=1.5)

        scaled_returns = signals * scaling * returns
        return scaled_returns

    def aggregate_portfolio_returns(self, strategy_returns):
        """Aggregate returns across assets.

        Args:
            strategy_returns (pd.DataFrame): Strategy returns across multiple assets.

        Returns:
            pd.Series: Equally-weighted portfolio returns.
        """
        portfolio_returns = strategy_returns.mean(axis=1)
        return portfolio_returns

    def compute_cumulative_returns(self, portfolio_returns):
        """Compute cumulative portfolio performance.

        Args:
            portfolio_returns (pd.Series): Time series of daily portfolio returns.

        Returns:
            pd.Series: Cumulative compound returns.
        """
        cumulative_returns = (1 + portfolio_returns).cumprod()
        return cumulative_returns
