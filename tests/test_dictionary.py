from src import old_norse_dictionary


def test_default_dictionary_has_correct_length() -> None:
    result = old_norse_dictionary.get_default()
    assert len(result) == 35207


def test_default_dictionary_has_expected_content() -> None:
    result = old_norse_dictionary.get_default()

    assert result[100].word == "af-kymi"
    assert result[100].definitions[0] == "a, m. <i>nook</i>, Ísl. ii. 471 (paper MS.); kymi, id., is now freq."

    assert result[1989].word == "át-frekr"
    assert (
        result[1989].definitions[0]
        == "adj. <i>greedy, voracious,</i> Hkv. 2. 41."
    )

    assert result[30000].word == "tor-velda"
    assert result[30000].definitions[0] == "<strong>1.</strong> d, <i>to make difficulties;</i> t. e-t fyrir e-m, Ld. 238."