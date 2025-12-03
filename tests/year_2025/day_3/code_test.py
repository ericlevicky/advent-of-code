import src.year_2025.day_3.code as day_3


def test_some_function():
    expected = 357
    result = day_3.some_function("test.txt")
    assert result == expected


def test_input_some_function():
    expected = 17535
    result = day_3.some_function("input.txt")
    assert result == expected


def test_part_two_some_function():
    expected = 3121910778619
    result = day_3.some_function("test.txt", True)
    assert result == expected


def test_input_part_two_some_function():
    expected = 173577199527257
    result = day_3.some_function("input.txt", True)
    assert result == expected
