import pytest

import src.year_2025.day_11.code as day_11


def test_part1_counts_paths_from_sample():
    assert day_11.part1("test.txt") == 5


def test_part1_real_input():
    expected = 511
    result = day_11.part1("input.txt")
    assert result == expected


def test_part2():
    expected = 0
    result = day_11.part2("test.txt")
    assert result == expected


def test_part2_real_input():
    expected = 458618114529380
    result = day_11.part2("input.txt")
    assert result == expected
