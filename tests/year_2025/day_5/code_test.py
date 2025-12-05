import src.year_2025.day_5.code as day_5


def test_some_function():
    """Test with the example from the README - should return 3 fresh ingredients"""
    expected = 3
    result = day_5.some_function("test.txt")
    assert result == expected


def test_answer_some_function():
    """Test with actual puzzle input"""
    expected = 511
    result = day_5.some_function("input.txt")
    assert result == expected


def test_part_two_some_function():
    """Test part two with the example - should return 14 total fresh IDs"""
    expected = 14
    result = day_5.some_function("test.txt", True)
    assert result == expected


def test_answer_part_two_some_function():
    """Test part two with actual puzzle input"""
    expected = 350939902751909
    result = day_5.some_function("input.txt", True)
    assert result == expected
