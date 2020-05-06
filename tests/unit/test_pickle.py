from pathlib import Path

from arsenal.pickle import load_pickle, save_pickle


def test_saving_and_loading_pickle(tmpdir):
    d = {
        'a': 1,
        'b': [1,2,3]
    }
    tmp_path = Path(tmpdir) / 'stuff.pkl'
    assert not tmp_path.exists()
    save_pickle(d, tmp_path)
    loaded_d = load_pickle(tmp_path)
    assert loaded_d == d
