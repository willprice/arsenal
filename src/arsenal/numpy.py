import numpy as np


def select(xs: np.ndarray, xs_ids: np.ndarray, chosen_ids: np.ndarray) -> np.ndarray:
    """

    Args:
        xs: Array to select elements from
        xs_ids: Array to

    Returns:

    """
    if len(xs) != len(xs_ids):
        raise ValueError(f"Expected xs and xs_ids to be the same length but were "
                         f"{len(xs)} and {len(xs_ids)} respectively.")
    xs_lookup = {
        id: idx for idx, id in enumerate(xs_ids)
    }
    chosen_idx = np.array([xs_lookup[id] for id in chosen_ids], dtype=np.int)
    return xs[chosen_idx]