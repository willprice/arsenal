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
