import numpy as np
from arsenal.collections import index_collated_dict
from numpy.testing import assert_array_equal


def test_indexing_flat_dict_of_lists():
    indexed_dict = index_collated_dict({"a": [1, 2, 3], "b": [4, 5, 6]}, [0, 2])

    assert indexed_dict == {"a": [1, 3], "b": [4, 6]}


def test_indexing_of_nested_dict():
    indexed_dict = index_collated_dict({"b": {"c": [4, 5, 6]}}, [0, 2])

    assert indexed_dict == {"b": {"c": [4, 6]}}


def test_indexing_of_np_arrays():
    indexed_dict = index_collated_dict({"a": np.array([4, 5, 6])}, [0, 2])

    assert len(indexed_dict) == 1
    assert_array_equal(indexed_dict["a"], np.array([4, 6]))
