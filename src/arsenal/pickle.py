import pickle
from pathlib import Path
from typing import Any, Union


def load_pickle(filepath: Union[str, Path]) -> Any:
    """Load pickled data from disk

    Args:
        filepath: Path to pickle file

    Returns:
        Contents of pickle.
    """
    with open(filepath, 'rb') as f:
        return pickle.load(f)


def save_pickle(obj: Any, filepath: Union[str, Path], protocol=pickle.DEFAULT_PROTOCOL) -> None:
    """
    Args:
        obj: The object to persist to disk
        filepath: The path to save
        protocol: The pickle protocol to use
    """
    filepath = Path(filepath)
    directory = filepath.parent
    directory.mkdir(parents=True, exist_ok=True)
    with open(filepath, 'wb') as f:
        pickle.dump(obj, f, protocol=protocol)
