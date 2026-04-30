"""Pattern conversion and vectorized pattern matching helpers."""

from __future__ import annotations

import numpy as np
from numpy.lib.stride_tricks import sliding_window_view
from numpy.typing import NDArray


def pattern_to_array(pattern: str) -> NDArray[np.int_]:
    """Convert an H/T pattern string into a numpy 0/1 array.

    Args:
        pattern: String containing only H and T characters.

    Returns:
        A numpy integer array where H is 1 and T is 0.

    Raises:
        ValueError: If the pattern is empty or contains unsupported characters.
    """
    if not pattern:
        raise ValueError("pattern must not be empty")

    normalized = pattern.upper()
    invalid_chars = set(normalized) - {"H", "T"}
    if invalid_chars:
        invalid = ", ".join(sorted(invalid_chars))
        raise ValueError(f"pattern contains unsupported characters: {invalid}")

    return np.fromiter((1 if char == "H" else 0 for char in normalized), dtype=np.int_)


def find_pattern_matches(
    flips: NDArray[np.integer],
    pattern: NDArray[np.integer],
) -> NDArray[np.int_]:
    """Return starting indices where a pattern appears in a flip sequence.

    Overlapping matches are included.

    Args:
        flips: One-dimensional numpy array of simulated flips.
        pattern: One-dimensional numpy array representing the pattern to find.

    Returns:
        A numpy integer array of zero-based starting indices.

    Raises:
        ValueError: If either input is not one-dimensional or pattern is empty.
    """
    if flips.ndim != 1:
        raise ValueError("flips must be a one-dimensional array")
    if pattern.ndim != 1:
        raise ValueError("pattern must be a one-dimensional array")
    if pattern.size == 0:
        raise ValueError("pattern must not be empty")
    if pattern.size > flips.size:
        return np.array([], dtype=np.int_)

    windows = sliding_window_view(flips, pattern.size)
    matches = np.all(windows == pattern, axis=1)
    return np.flatnonzero(matches).astype(np.int_, copy=False)
