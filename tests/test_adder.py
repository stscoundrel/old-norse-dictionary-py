from src.template import adder


def test_adds_two():
    result1 = adder.add_two(2)
    result2 = adder.add_two(0)

    assert result1 == 4
    assert result2 == 2


