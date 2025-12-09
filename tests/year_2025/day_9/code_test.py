import src.year_2025.day_9.code as day_9


def test_part1_example():
    """Test part 1 with the example from the problem description."""
    expected = 50  # Largest rectangle area from the example
    result = day_9.part1("test.txt")
    if expected is not None:
        assert result == expected


def test_part1_input():
    """Test part 1 with actual puzzle input"""
    expected = 4741848414
    result = day_9.part1("input.txt")
    assert result == expected


def test_part2_example():
    """Test part 2 with the example from the problem description."""
    expected = 24  # Largest rectangle area using only red and green tiles
    result = day_9.part2("test.txt")
    assert result == expected


def test_part2_input():
    """Test part 2 with actual puzzle input"""
    expected = 1508918480
    result = day_9.part2("input.txt")
    assert result == expected
