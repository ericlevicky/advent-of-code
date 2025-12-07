"""
Advent of Code 2025 - Day 7: Laboratories

Simulates tachyon beam splitting through a manifold.
Part 1: Count unique splitters hit by classical beams.
Part 2: Count unique timelines using quantum many-worlds interpretation.
"""

import os
from typing import Optional


def parse_input(input_text: str) -> tuple[list[list[str]], int, int]:
    """Parse the input text into a grid and find the starting position."""
    lines = input_text.strip().split("\n")
    grid = [list(line) for line in lines]

    # Find the starting position (S)
    start_row: Optional[int] = None
    start_col: Optional[int] = None
    for r, row in enumerate(grid):
        for c, cell in enumerate(row):
            if cell == "S":
                start_row, start_col = r, c
                break
        if start_row is not None:
            break

    if start_row is None or start_col is None:
        raise ValueError("Starting position 'S' not found in grid")

    return grid, start_row, start_col


def part1(file_name: str) -> int:
    """Solve part 1: Count how many times the beam is split."""
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, file_name)

    with open(file_path, encoding="utf-8") as f:
        input_text = f.read()

    grid, start_row, start_col = parse_input(input_text)

    # Track active beams: list of (row, col) positions
    beams = [(start_row + 1, start_col)]  # Start from the row below S

    # Track which splitters have been hit
    hit_splitters: set[tuple[int, int]] = set()

    # Track which beam positions we've processed to avoid infinite loops
    processed: set[tuple[int, int]] = set()

    while beams:
        new_beams = []

        for row, col in beams:
            # Skip if we've already processed this beam position
            if (row, col) in processed:
                continue
            processed.add((row, col))

            # Move down until we hit a splitter or exit the grid
            current_row = row
            while current_row < len(grid):
                cell = grid[current_row][col]

                if cell == "^":
                    # Hit a splitter! Mark it as hit
                    hit_splitters.add((current_row, col))

                    # Add left beam if within bounds
                    if col > 0:
                        new_beams.append((current_row + 1, col - 1))

                    # Add right beam if within bounds
                    if col < len(grid[0]) - 1:
                        new_beams.append((current_row + 1, col + 1))

                    break  # This beam stops at the splitter

                # Move down to the next row
                current_row += 1

        beams = new_beams

    return len(hit_splitters)


def part2(file_name: str) -> int:
    """Solve part 2: Count the number of unique timelines (paths) through the manifold."""
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, file_name)

    with open(file_path, encoding="utf-8") as f:
        input_text = f.read()

    grid, start_row, start_col = parse_input(input_text)

    # Find all splitters and build a map of their positions
    splitters: dict[int, list[int]] = {}
    for r, row in enumerate(grid):
        for c, cell in enumerate(row):
            if cell == "^":
                if c not in splitters:
                    splitters[c] = []
                splitters[c].append(r)

    # Sort splitter rows for each column
    for _col, rows in splitters.items():
        rows.sort()

    # Use memoization: for each (row, col) position, calculate how many paths
    # lead from that position to the bottom of the grid
    memo: dict[tuple[int, int], int] = {}

    def count_paths(row: int, col: int) -> int:
        """Count the number of unique paths from (row, col) to the bottom."""
        if row >= len(grid):
            # Exited the grid - this is one complete path
            return 1

        if (row, col) in memo:
            return memo[(row, col)]

        # Check if there's a splitter in this column at or below this row
        if col in splitters:
            # Find the next splitter in this column
            next_splitter: Optional[int] = None
            for splitter_row in splitters[col]:
                if splitter_row >= row:
                    next_splitter = splitter_row
                    break

            if next_splitter is not None:
                # We'll hit this splitter
                # Count paths going left and right from the splitter
                paths = 0

                # Left path
                if col > 0:
                    paths += count_paths(next_splitter + 1, col - 1)

                # Right path
                if col < len(grid[0]) - 1:
                    paths += count_paths(next_splitter + 1, col + 1)

                memo[(row, col)] = paths
                return paths

        # No splitter, beam exits at the bottom
        memo[(row, col)] = 1
        return 1

    return count_paths(start_row + 1, start_col)


if __name__ == "__main__":
    print("Test Part 1:", part1("test.txt"))
    print("Test Part 2:", part2("test.txt"))
    print("Part 1:", part1("input.txt"))
    print("Part 2:", part2("input.txt"))
