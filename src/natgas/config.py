"""Load project settings from config.yaml and secrets from.env."""
import os
from pathlib import Path

import yaml
from dotenv import load_dotenv

REPO_ROOT = Path(__file__).resolve().parents[2]

def load_config(path: Path | None = None) -> dict:
    """Return the settings in config.yaml as a dict"""
    if path is None:
        path = REPO_ROOT / "config.yaml"
    with open(path) as f:
        return yaml.safe_load(f)

def get_eia_key(env_file: Path | None=None) -> str:
    """Return the EIA API key, or raise a clear error if isn't set"""
    if env_file is None:
        env_file = REPO_ROOT / ".env"
    load_dotenv(env_file)
    key = os.getenv("EIA_API_KEY")
    if not key: 
        raise RuntimeError("copy .env.example to .env and add a key")
    return key
