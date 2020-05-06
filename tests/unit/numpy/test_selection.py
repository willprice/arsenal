import hypothesis.strategies as st
import pytest
from hypothesis import given
import numpy as np

from arsenal.numpy import select


def test_selecting_0_elements():
    xs = np.array([1, 2, 3], dtype=np.float32)
    ids = np.array(["a", "b", "c"])
    chosen_ids = np.array([])

    selection = select(xs, ids, chosen_ids)

    assert len(selection) == 0
    assert selection.dtype == xs.dtype


def test_selecting_1_element():
    xs = np.array([1, 2, 3], dtype=np.float32)
    ids = np.array(["a", "b", "c"])
    chosen_ids = np.array(["b"])

    selection = select(xs, ids, chosen_ids)

    np.testing.assert_array_equal(selection, np.array([2], dtype=np.float32))


def test_selecting_duplicate_element():
    xs = np.array([1, 2, 3], dtype=np.float32)
    ids = np.array(["a", "b", "c"])
    chosen_ids = np.array(["b", "b"])

    selection = select(xs, ids, chosen_ids)

    np.testing.assert_array_equal(selection, np.array([2, 2], dtype=np.float32))


def test_throw_error_if_xs_and_xs_ids_arent_same_length():
    with pytest.raises(ValueError):
        select(np.array([1, 2]), np.array([1]), np.array([1]))
