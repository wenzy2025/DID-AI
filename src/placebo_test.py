"""Module implementing a simple placebo test for DID analysis."""

from typing import Optional

import pandas as pd

from did_model import run_did


def run_placebo_test(df: pd.DataFrame, outcome: str, treatment: str, time: str):
    """Run a placebo test by randomly shuffling the treatment indicator."""
    shuffled = df.copy().sample(frac=1, random_state=42).reset_index(drop=True)
    shuffled[treatment] = shuffled[treatment].sample(frac=1, random_state=42).values
    model = run_did(shuffled, outcome, treatment, time)
    return model
