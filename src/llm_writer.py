"""LLM interface for generating result summaries."""

from typing import Any


def write_results(model: Any, trend_fig: Any, placebo_model: Any) -> str:
    """Generate a markdown summary of the results using a placeholder LLM call."""
    # TODO: Integrate with actual LLM service such as DeepSeek or OpenAI
    interaction_term = [p for p in model.params.index if ':' in p]
    effect = model.params[interaction_term[0]] if interaction_term else 'N/A'
    summary = (
        "# DID Analysis Results\n"
        f"Estimated treatment effect: {effect}\n\n"
        "Parallel trend and placebo test outputs available."
    )
    return summary
