import pytest
import pandas as pd
import numpy as np
from src.data_loader import DataLoader
from src.signals import MomentumSignals
from src.backtest import Backtester


@pytest.fixture
def sample_price_data():
    """Generates a dummy DataFrame simulating daily stock prices."""
    dates = pd.date_range(start="2026-01-01", periods=10, freq="D")
    data = {
        "AAPL": [100, 101, 102, 103, 104, 105, 106, 107, 108, 109],
        "GLD": [200, 199, 198, 197, 196, 195, 194, 193, 192, 191],
    }
    return pd.DataFrame(data, index=dates)


def test_compute_returns(sample_price_data):
    loader = DataLoader()
    returns = loader.compute_returns(sample_price_data)

    assert "AAPL" in returns.columns
    assert "GLD" in returns.columns

    assert not pd.isna(returns.iloc[0]["AAPL"])


def test_momentum_signal_shape(sample_price_data):
    signal_gen = MomentumSignals()
    signals = signal_gen.compute_momentum_signal(sample_price_data, lookback=2)

    assert signals.shape == sample_price_data.shape
    unique_signals = np.unique(signals.dropna())
    for s in unique_signals:
        assert s in [-1.0, 0.0, 1.0]


def test_backtester_execution(sample_price_data):
    loader = DataLoader()
    signal_gen = MomentumSignals()
    tester = Backtester()

    returns = loader.compute_returns(sample_price_data)
    signals = signal_gen.compute_momentum_signal(sample_price_data, lookback=2)

    scaled = tester.compute_vol_scaled_returns(returns, signals, target_vol=0.10)

    assert scaled is not None
    assert isinstance(scaled, pd.DataFrame)
