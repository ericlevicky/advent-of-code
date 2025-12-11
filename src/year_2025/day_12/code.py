"""Advent of Code 2025 Day 12 scaffolding."""

from __future__ import annotations

from pathlib import Path
from typing import List


def load_input(file_name: str) -> str:
    """Return the raw puzzle input bundled with this module."""
    file_path = Path(__file__).resolve().parent / file_name
    return file_path.read_text(encoding="utf-8")


def parse_input(raw: str) -> List[str]:
    """Turn the raw text into a structured representation.

    Update this function as soon as you know how the puzzle encodes its data.
    """
    return [line for line in raw.splitlines() if line]


def part1(file_name: str = "input.txt") -> int:
    """Solve part 1 of the puzzle."""
    data = parse_input(load_input(file_name))
    raise NotImplementedError("Day 12 part 1 has not been implemented yet.")


def part2(file_name: str = "input.txt") -> int:
    """Solve part 2 of the puzzle."""
    data = parse_input(load_input(file_name))
    raise NotImplementedError("Day 12 part 2 has not been implemented yet.")


if __name__ == "__main__":  # pragma: no cover
    print("Part 1:", part1("test.txt"))
    print("Part 2:", part2("test.txt"))
