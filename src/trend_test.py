"""Module for checking the parallel trend assumption."""

import pandas as pd
import plotly.express as px


def run_trend_test(df: pd.DataFrame, outcome: str, treatment: str, time: str):
    """Create a simple trend plot to visually inspect parallel trends."""
    avg = df.groupby([time, treatment])[outcome].mean().reset_index()
    fig = px.line(avg, x=time, y=outcome, color=treatment, markers=True,
                  title="Parallel Trend Check")
    return fig
