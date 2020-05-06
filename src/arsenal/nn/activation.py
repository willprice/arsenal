import numpy as np


def softmax(xs, axis=-1):
    """Apply softmax function over a dimension of ``xs``.

    Args:
        xs: Array of floats to softmax.
        axis: Dimension to softmax

    Returns:
        Softmaxed ``xs``
    """
    xs = xs - np.max(xs, axis=axis, keepdims=True)
    xs_exp = np.exp(xs)
    return xs_exp / xs_exp.sum(axis=axis, keepdims=True)
