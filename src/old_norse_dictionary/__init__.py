from typing import Tuple
from .dictionary import DictionaryEntry, DictionaryPath, get_dictionary


def get_default() -> Tuple[DictionaryEntry, ...]:
    return get_dictionary(DictionaryPath.DEFAULT)