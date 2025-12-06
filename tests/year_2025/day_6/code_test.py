import src.year_2025.day_6.code as day_6


def test_solve_worksheet():
    """Test the example from the problem description."""
    expected = 4277556  # 33210 + 490 + 4243455 + 401
    result = day_6.solve_worksheet("test.txt")
    assert result == expected


def test_input_solve_worksheet():
    """Test with actual puzzle input"""
    expected = 4405895212738
    result = day_6.solve_worksheet("input.txt")
    assert result == expected


def test_part_two_solve_worksheet():
    """Test part two with the example - reading right-to-left in columns"""
    expected = 3263827  # 1058 + 3253600 + 625 + 8544
    result = day_6.solve_worksheet("test.txt", True)
    assert result == expected


def test_input_part_two_solve_worksheet():
    """Test part two with actual puzzle input"""
    expected = 7450962489289
    result = day_6.solve_worksheet("input.txt", True)
    assert result == expected
