"""Advent of Code 2025 Day 11 solution helpers."""

from __future__ import annotations

from pathlib import Path
from functools import lru_cache
from typing import Dict, List


def load_input(file_name: str) -> str:
    """Return the raw puzzle input bundled with this module."""
    file_path = Path(__file__).resolve().parent / file_name
    return file_path.read_text(encoding="utf-8")


def parse_input(raw: str) -> Dict[str, List[str]]:
    """Parse the wiring diagram into an adjacency list."""

    graph: Dict[str, List[str]] = {}
    for line in raw.splitlines():
        stripped = line.strip()
        if not stripped:
            continue
        device, outputs = stripped.split(":", maxsplit=1)
        graph[device.strip()] = outputs.split()
    return graph


def part1(file_name: str = "input.txt") -> int:
    """Count the distinct directed paths from `you` to `out`."""

    graph = parse_input(load_input(file_name))

    @lru_cache(maxsize=None)
    def count_paths(node: str) -> int:
        if node == "out":
            return 1
        total = 0
        for target in graph.get(node, []):
            total += count_paths(target)
        return total

    return count_paths("you")


def part2(file_name: str = "input.txt") -> int:
    """Count svr→out paths that visit both dac and fft."""

    graph = parse_input(load_input(file_name))
    required = ("dac", "fft")
    bit_for = {name: 1 << idx for idx, name in enumerate(required)}
    full_mask = (1 << len(required)) - 1

    @lru_cache(maxsize=None)
    def count_paths(node: str, mask: int) -> int:
        new_mask = mask | bit_for.get(node, 0)
        if node == "out":
            return 1 if new_mask & full_mask == full_mask else 0
        total = 0
        for target in graph.get(node, []):
            total += count_paths(target, new_mask)
        return total

    return count_paths("svr", 0)


if __name__ == "__main__":  # pragma: no cover
    print("Test Part 1:", part1("test.txt"))
    print("Test Part 2:", part2("test.txt"))
    print("Part 1:", part1("input.txt"))
    print("Part 2:", part2("input.txt"))
