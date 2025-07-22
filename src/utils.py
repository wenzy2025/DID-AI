"""Utility functions for data loading and preprocessing."""

import pandas as pd


def load_data(path: str) -> pd.DataFrame:
    """Load CSV data from the given path."""
    return pd.read_csv(path)
