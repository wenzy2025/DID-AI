"""Main application for running DID analysis via command line or UI."""

from did_model import run_did
from trend_test import run_trend_test
from placebo_test import run_placebo_test
from llm_writer import write_results
from utils import load_data


def main(data_path: str, outcome: str, treatment: str, time: str):
    """Run DID analysis and tests given dataset and parameters."""
    df = load_data(data_path)
    results = run_did(df, outcome, treatment, time)
    trend_fig = run_trend_test(df, outcome, treatment, time)
    placebo_results = run_placebo_test(df, outcome, treatment, time)
    report = write_results(results, trend_fig, placebo_results)
    print(report)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Run DID analysis")
    parser.add_argument("data", help="Path to CSV data file")
    parser.add_argument("--outcome", required=True, help="Outcome variable name")
    parser.add_argument("--treatment", required=True, help="Treatment variable name")
    parser.add_argument("--time", required=True, help="Time variable name")

    args = parser.parse_args()
    main(args.data, args.outcome, args.treatment, args.time)
