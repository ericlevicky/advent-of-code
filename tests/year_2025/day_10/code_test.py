import src.year_2025.day_10.code as day_10


def test_part1_example():
    """Test part 1 with the example from the problem description."""
    expected = 7  # 2 + 3 + 2 = 7 button presses
    result = day_10.part1("test.txt")
    if expected is not None:
        assert result == expected


def test_part1_input():
    """Test part 1 with actual puzzle input"""
    expected = 432
    result = day_10.part1("input.txt")
    if expected is not None:
        assert result == expected


def test_part2_example():
    """Test part 2 with the example from the problem description."""
    expected = 33  # 10 + 12 + 11 = 33 button presses
    result = day_10.part2("test.txt")
    if expected is not None:
        assert result == expected


def test_part2_input():
    """Test part 2 with actual puzzle input"""
    expected = 18011
    result = day_10.part2("input.txt")
    if expected is not None:
        assert result == expected
