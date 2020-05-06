from typing import Any
from typing import Dict
from typing import List
from typing import Sequence

import numpy as np


def intersperse(ls, elem, first=False, last=False):
    """

    Args:
        ls: A list of elements
        elem: The element to insert in between each element
        first: Whether to add the element at the beginning of the sequence
        last: Whether to add the element at the end of the sequence

    Returns:
        ``ls`` interspersed with ``elem```


    Examples:
        >>> intersperse([1, 2, 3], 0)
        [1, 0, 2, 0, 3]
        >>> intersperse([1, 2, 3], 0, first=True)
        [0, 1, 0, 2, 0, 3]
        >>> intersperse([1, 2, 3], 0, first=True, last=True)
        [0, 1, 0, 2, 0, 3, 0]
    """
    length = len(ls)
    new = []
    if first:
        new.append(elem)
    for i in range(length - 1):
        new.append(ls[i])
        new.append(elem)
    new.append(ls[-1])
    if last:
        new.append(elem)
    return new


def index_collated_dict(d: Dict[str, Any], idxs: Sequence[int]) -> Dict[str, Any]:
    """
    Args:
        d: dictionary of sequences with arbitrary levels of sub-dictionary nesting
        idxs: list/array of indices

    Returns:
        Dictionary where all sequences are indexed by idxs.
    """

    idxs = np.asarray(idxs)
    subset_dict: Dict[str, Any] = dict()
    for key, values in d.items():
        if isinstance(values, list):
            subset_dict[key] = [values[i] for i in idxs]
        elif isinstance(values, np.ndarray):
            subset_dict[key] = values[idxs]
        elif isinstance(values, dict):
            subset_dict[key] = index_collated_dict(values, idxs)
        else:
            raise TypeError(f"Unknown data type: {type(values)}")
    return subset_dict
