import src.year_2025.day_3.code as day_3


def test_some_function():
    expected = 357
    result = day_3.some_function("test.txt")
    assert result == expected


def test_input_some_function():
    expected = 17383
    result = day_3.some_function("input.txt")
    assert result == expected


def test_part_two_some_function():
    expected = 3121910778619
    result = day_3.some_function("test.txt", True)
    assert result == expected


def test_input_part_two_some_function():
    expected = 172601598658203
    result = day_3.some_function("input.txt", True)
    assert result == expected
