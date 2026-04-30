"""Experiments for detecting specified streak patterns in coin flips."""

from __future__ import annotations

from typing import TypedDict

import numpy as np

from ..patterns import find_pattern_matches, pattern_to_array
from ..simulator import simulate_flips


class PatternExperimentResult(TypedDict):
    """Summary statistics for one pattern in a pattern experiment."""

    total_count: int
    simulations_seen: int
    first_simulation: int | None
    first_position: int | None
    counts_per_simulation: list[int]
    probability_seen: float


def _empty_result(n_simulations: int) -> PatternExperimentResult:
    """Create an initialized result container for a pattern."""
    return {
        "total_count": 0,
        "simulations_seen": 0,
        "first_simulation": None,
        "first_position": None,
        "counts_per_simulation": [0] * n_simulations,
        "probability_seen": 0.0,
    }


def run_pattern_experiment(
    n_flips: int,
    guesses: list[str],
    n_simulations: int,
    p_heads: float = 0.5,
    seed: int | None = None,
) -> dict[str, PatternExperimentResult]:
    """Run repeated simulations and summarize occurrences of each guess pattern.

    Args:
        n_flips: Number of flips per simulation.
        guesses: Pattern strings to search for, such as "HHHHHHHHHH".
        n_simulations: Number of independent simulations to run.
        p_heads: Probability that each flip is heads.
        seed: Optional seed for reproducible simulations.

    Returns:
        A dictionary keyed by pattern string with counts and first-seen metadata.

    Raises:
        ValueError: If n_flips or n_simulations is negative.
    """
    if n_flips < 0:
        raise ValueError("n_flips must be non-negative")
    if n_simulations < 0:
        raise ValueError("n_simulations must be non-negative")

    rng = np.random.default_rng(seed)
    pattern_arrays = {guess: pattern_to_array(guess) for guess in guesses}
    results = {guess: _empty_result(n_simulations) for guess in guesses}

    for simulation_index in range(n_simulations):
        flips = simulate_flips(n_flips, p_heads=p_heads, rng=rng)

        for guess, pattern in pattern_arrays.items():
            match_indices = find_pattern_matches(flips, pattern)
            count = int(match_indices.size)
            result = results[guess]

            result["counts_per_simulation"][simulation_index] = count
            result["total_count"] += count

            if count > 0:
                result["simulations_seen"] += 1
                if result["first_simulation"] is None:
                    result["first_simulation"] = simulation_index
                    result["first_position"] = int(match_indices[0])

    for result in results.values():
        result["probability_seen"] = (
            result["simulations_seen"] / n_simulations if n_simulations > 0 else 0.0
        )

    return results
