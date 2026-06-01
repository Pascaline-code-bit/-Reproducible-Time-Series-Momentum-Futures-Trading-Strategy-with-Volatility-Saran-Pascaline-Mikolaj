"""signals.py

Momentum signal generation for time-series trading strategies.
"""

import numpy as np


class MomentumSignals:
    """A class to compute time-series momentum trading signals based on historical asset prices."""

    def compute_momentum_signal(self, prices, lookback=252):
        """Compute time-series momentum signals.

        Generates a signal of +1 if the asset's asset return over the lookback
        period is positive, and -1 if it is negative. The signal is shifted by 1 day
        to avoid lookahead bias.

        Args:
            prices (pd.DataFrame or pd.Series): Historical asset price data.
            lookback (int): Number of trading days for the momentum lookback window. Defaults to 252.

        Returns:
            pd.DataFrame or pd.Series: Generated trading signals containing values of 1.0 or -1.0.
        """
        past_returns = prices.pct_change(lookback)
        signals = np.sign(past_returns)
        signals = signals.shift(1)
        return signals

    def compute_multi_horizon_signals(self, prices):
        """Compute signals for multiple horizons: 1, 3, 6, and 12 months.

        Calculates momentum indicators over different business-day windows
        representing standard financial lookback horizons.

        Args:
            prices (pd.DataFrame or pd.Series): Historical asset price data.

        Returns:
            dict: A dictionary mapping each integer horizon lookback window (21, 63, 126, 252)
                to its corresponding shifted signal DataFrame or Series.
        """
        horizons = [21, 63, 126, 252]
        signals = {}

        for h in horizons:
            sig = np.sign(prices.pct_change(h)).shift(1)
            signals[h] = sig

        return signals
