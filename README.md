# Old Norse Dictionary

Old Norse to English Dictionary for Python. The dictionary consists of 35 000+ Old Norse words with English translations.

Based on the classic dictionary by Richard Cleasby and Gudbrand Vigfusson. If you find this one too abbreviated, academic or hard to read, you might want to check out [A Concise Dictionary of Old Icelandic](https://github.com/stscoundrel/old-icelandic-dictionary-py)

### Install

`pip install old-norse-dictionary`

### Usage

The dictionary comes in two variants:
- Default dictionary has HTML markup `<i>` and `<b>` to match look of the original book.
- No-markup version has the same content without any additional formatting tags.

```python

from old_norse_dictionary import get_default, get_no_markup

# Both dictionaries return entries that consist of headword, and definitions list.
default = get_default()
no_markup = get_no_markup()

# Headwords wont differ between dictionaries.
print(default[1989].word)   # át-frekr
print(no_markup[1989].word) # át-frekr

# But definition markup does differ.
print(default[14].definitions[0])   # adj. <i>greedy, voracious,</i> Hkv. 2. 41.
print(no_markup[14].definitions[0]) # adj. greedy, voracious, Hkv. 2. 41.

```

Individual words are returned in format of:

```python
{
    word: str
    definitions: Tuple[str, ...]
}
```

### About Cleasby & Vigfusson Dictionary

"Icelandic-English" dictionary was started by Richard Cleasby and finished by Gudbrand Vigfusson. It was published in 1874, which leads to there being many public domain versions of the book available.
