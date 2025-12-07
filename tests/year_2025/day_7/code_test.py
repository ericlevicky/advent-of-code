import src.year_2025.day_7.code as day_7


def test_part1_example():
    """Test part 1 with the example from the problem description."""
    expected = 21
    result = day_7.part1("test.txt")
    assert result == expected


def test_part1_input():
    """Test part 1 with actual puzzle input"""
    expected = 1605
    result = day_7.part1("input.txt")
    assert result == expected


def test_part2_example():
    """Test part 2 with the example from the problem description."""
    expected = 40
    result = day_7.part2("test.txt")
    assert result == expected


def test_part2_input():
    """Test part 2 with actual puzzle input"""
    expected = 29893386035180
    result = day_7.part2("input.txt")
    assert result == expected
