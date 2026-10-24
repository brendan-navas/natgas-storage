import pandas as pd
import pytest

from natgas.config import get_eia_key, load_config

def test_config_has_required_sections():
    assert "sample" in load_config()
    assert "costs" in load_config()
    assert "paths" in load_config()

def test_train_ends_before_test_starts():
    train_end = pd.Timestamp(load_config()["sample"]["train_end"])
    test_start = pd.Timestamp(load_config()["sample"]["test_start"])
    assert train_end < test_start

def test_missing_key_raises(tmp_path, monkeypatch):
    monkeypatch.delenv("EIA_API_KEY", raising=False)
    with pytest.raises(RuntimeError):
        get_eia_key(env_file=tmp_path / "missing.env")