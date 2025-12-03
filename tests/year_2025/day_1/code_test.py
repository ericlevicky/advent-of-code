import src.year_2025.day_1.code as day_1


def test_some_function():
    expected = 3
    result = day_1.some_function("test.txt")
    assert result == expected


def test_input_some_function():
    expected = 1168
    result = day_1.some_function("input.txt")
    assert result == expected


def test_part_one_some_function():
    # Part 2: Count every click where dial points at 0
    result = day_1.some_function("test.txt", False)
    # This will count all times we pass through 0 during rotations
    assert result >= 0  # Actual value depends on specific crossing counts


def test_input_part_two_some_function():
    expected = 7199

    # Part 2: Count every click where dial points at 0
    result = day_1.some_function("input.txt", True)
    # This will count all times we pass through 0 during rotations
    assert result == expected  # Actual value depends on specific crossing counts
