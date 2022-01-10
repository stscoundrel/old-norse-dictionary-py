from . import reader
from enum import Enum
from typing import NamedTuple, Tuple


class DictionaryPath(str, Enum):
    DEFAULT = "default.json"
    NO_MARKUP = "no-markup.json"


class DictionaryEntry(NamedTuple):
    word: str
    definitions: Tuple[str, ...]


def get_dictionary(path: DictionaryPath) -> Tuple[DictionaryEntry, ...]:
    raw_data = reader.read_json(path.value)

    return tuple(
        DictionaryEntry(raw_entry["word"], raw_entry["definitions"])
        for raw_entry in raw_data
    )
