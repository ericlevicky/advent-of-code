import src.year_2025.day_8.code as day_8


def test_part1_example():
    """Test part 1 with the example from the problem description.

    After making 10 shortest connections, multiply together the sizes
    of the three largest circuits (5, 4, and 2) to get 40.
    """
    expected = 40
    result = day_8.part1("test.txt")
    assert result == expected


def test_part1_input():
    """Test part 1 with actual puzzle input"""
    expected = 42840
    result = day_8.part1("input.txt")
    assert result == expected


def test_part2_example():
    """Test part 2 with the example from the problem description.

    The last connection to unify all circuits is between 216,146,977 and 117,168,530.
    Multiplying X coordinates: 216 * 117 = 25272
    """
    expected = 25272
    result = day_8.part2("test.txt")
    assert result == expected


def test_part2_input():
    """Test part 2 with actual puzzle input"""
    expected = 170629052
    result = day_8.part2("input.txt")
    assert result == expected
