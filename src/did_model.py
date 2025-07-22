"""Core module for Difference-in-Differences estimation."""

from typing import Tuple

import pandas as pd
import statsmodels.formula.api as smf


def run_did(df: pd.DataFrame, outcome: str, treatment: str, time: str):
    """Estimate a basic DID model using statsmodels OLS.

    Parameters
    ----------
    df : pd.DataFrame
        Input dataframe containing outcome, treatment and time columns.
    outcome : str
        Outcome variable name.
    treatment : str
        Binary treatment indicator.
    time : str
        Time period indicator.
    """
    formula = f"{outcome} ~ {treatment} * {time}"
    model = smf.ols(formula, data=df).fit(cov_type="HC3")
    return model
