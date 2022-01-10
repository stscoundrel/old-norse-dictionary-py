from importlib.resources import open_text
from json import load
from typing import Any
from . import resources


def read_json(path: str) -> Any:
    file = open_text(resources, path)
    raw_data = load(file)
    file.close()

    return raw_data
