"""Runnable example for the coin-flip pattern experiment."""

from __future__ import annotations

from src.experiments.streaks import run_pattern_experiment


def print_results(results: dict) -> None:
    """Print experiment results in a compact human-readable format."""
    for pattern, stats in results.items():
        first_simulation = stats["first_simulation"]
        first_position = stats["first_position"]
        first_seen = (
            "not seen"
            if first_simulation is None
            else f"simulation {first_simulation}, position {first_position}"
        )

        print(f"Pattern: {pattern}")
        print(f"  Total matches:       {stats['total_count']}")
        print(f"  Simulations seen:    {stats['simulations_seen']}")
        print(f"  Probability seen:    {stats['probability_seen']:.3f}")
        print(f"  First seen:          {first_seen}")
        print(f"  Counts/simulation:   {stats['counts_per_simulation']}")
        print()


def main() -> None:
    """Run the default streak-detection experiment."""
    guesses = ["HHHHHHHHHH", "TTTTTTTTTT", "HTHTHTHTHT", "HHTTHHTTHH"]
    results = run_pattern_experiment(
        n_flips=1_000_000,
        guesses=guesses,
        n_simulations=10,
        seed=42,
    )
    print_results(results)


if __name__ == "__main__":
    main()
