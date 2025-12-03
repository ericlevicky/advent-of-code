import src.year_2025.day_2.code as day_2


def test_is_repeated_sequence():
    # Test cases for repeated sequences
    assert day_2.is_repeated_sequence(55) is True
    assert day_2.is_repeated_sequence(1010) is True
    assert day_2.is_repeated_sequence(123123) is True
    assert day_2.is_repeated_sequence(99) is True
    assert day_2.is_repeated_sequence(1111) is True

    # Test cases for non-repeated sequences
    assert day_2.is_repeated_sequence(12) is False
    assert day_2.is_repeated_sequence(123) is False
    assert day_2.is_repeated_sequence(1234) is False


def test_some_function():
    # Part 1: Sum of invalid IDs in test ranges
    result = day_2.some_function("test.txt")
    assert result == 1142


def test_part_two_some_function():
    # Part 2: Count of invalid IDs in test ranges
    result = day_2.some_function("test.txt", True)
    assert result == 2252


def test_input_some_function():
    # Part 1: Sum of invalid IDs in test ranges
    result = day_2.some_function("input.txt")
    assert result == 24043483400


def test_input_part_two_some_function():
    # Part 2: Count of invalid IDs in test ranges
    result = day_2.some_function("input.txt", True)
    assert result == 38262920235
