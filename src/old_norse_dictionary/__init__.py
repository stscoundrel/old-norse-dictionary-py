from typing import Tuple
from .dictionary import DictionaryEntry, DictionaryPath, get_dictionary


def get_default() -> Tuple[DictionaryEntry, ...]:
    return get_dictionary(DictionaryPath.DEFAULT)


def get_no_markup() -> Tuple[DictionaryEntry, ...]:
    return get_dictionary(DictionaryPath.NO_MARKUP)
