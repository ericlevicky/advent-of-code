"""
Advent of Code 2025 - Day 9

Placeholder for Day 9 puzzle.
"""

import os


def parse_input(input_text: str):
    """Parse the input text."""
    lines = input_text.strip().split("\n")
    return lines


def part1(file_name: str) -> int:
    """Solve part 1."""
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, file_name)

    with open(file_path, encoding="utf-8") as f:
        input_text = f.read()

    data = parse_input(input_text)
    return 0


def part2(file_name: str) -> int:
    """Solve part 2."""
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, file_name)

    with open(file_path, encoding="utf-8") as f:
        input_text = f.read()

    data = parse_input(input_text)
    return 0


if __name__ == "__main__":
    print("Test Part 1:", part1("test.txt"))
    print("Test Part 2:", part2("test.txt"))
    print("Part 1:", part1("input.txt"))
    print("Part 2:", part2("input.txt"))
