"""Vectorized coin-flip simulation utilities."""

from __future__ import annotations

import numpy as np
from numpy.typing import NDArray


def simulate_flips(
    n: int,
    p_heads: float = 0.5,
    rng: np.random.Generator | None = None,
) -> NDArray[np.int_]:
    """Simulate independent coin flips as a vectorized 0/1 numpy array.

    Args:
        n: Number of flips to simulate.
        p_heads: Probability that a flip is heads.
        rng: Optional numpy random generator. When omitted, a new default
            generator is created.

    Returns:
        A numpy integer array where 1 represents heads and 0 represents tails.

    Raises:
        ValueError: If n is negative or p_heads is outside [0, 1].
    """
    if n < 0:
        raise ValueError("n must be non-negative")
    if not 0.0 <= p_heads <= 1.0:
        raise ValueError("p_heads must be between 0 and 1")

    generator = rng if rng is not None else np.random.default_rng()
    return generator.binomial(1, p_heads, size=n).astype(np.int_, copy=False)
