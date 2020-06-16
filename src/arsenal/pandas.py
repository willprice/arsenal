import pandas as pd


def swap_index_values(series: pd.Series) -> pd.Series:
    """Swap index and values in series.

    Examples:
        >>> s = pd.Series({'a': 1, 'b': 2})
        >>> s.name = 'val'
        >>> s.index.name = 'char'
        >>> swap_index_values(s)
        val
        1    a
        2    b
        Name: char, dtype: object
    """
    swapped = pd.Series(series.index.values, index=pd.Index(series.values))
    swapped.name = series.index.name
    swapped.index.name = series.name
    return swapped
