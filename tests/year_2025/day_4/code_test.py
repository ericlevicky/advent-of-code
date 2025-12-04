import src.year_2025.day_4.code as day_4


def test_some_function():
    expected = 13
    result = day_4.some_function("test.txt")
    assert result == expected


def test_input_some_function():
    expected = 1518
    result = day_4.some_function("input.txt")
    assert result == expected


def test_part_two_some_function():
    expected = 43
    result = day_4.some_function("test.txt", True)
    assert result == expected


def test_input_part_two_some_function():
    expected = 8665
    result = day_4.some_function("input.txt", True)
    assert result == expected
