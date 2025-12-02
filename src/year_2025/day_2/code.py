import os
from bisect import bisect_left


def is_repeated_sequence(num: int) -> bool:
    """
    Check if a number consists of a digit sequence repeated at least twice.
    No leading zero allowed in the sequence.
    Examples:
        55 -> True (5 twice)
        1010 -> True (10 twice)
        123123 -> True (123 twice)
        121212 -> True (12 three times)
        1111111 -> True (1 seven times)
        12 -> False
        123 -> False
    """
    s = str(num)
    length = len(s)
    # Try all possible pattern lengths that divide the total length
    for k in range(1, length // 2 + 1):
        if length % k != 0:
            continue
        repeats = length // k
        if repeats < 2:
            continue
        first = s[:k]
        if first[0] == "0":
            continue
        if first * repeats == s:
            return True
    return False


def _parse_ranges(content: str) -> list[tuple[int, int]]:
    ranges: list[tuple[int, int]] = []
    for range_str in content.split(","):
        range_str = range_str.strip()
        if not range_str:
            continue
        if "-" in range_str:
            a, b = range_str.split("-", 1)
            try:
                start = int(a)
                end = int(b)
            except ValueError:
                continue
            if start > end:
                start, end = end, start
            ranges.append((start, end))
    return ranges


def _merge_ranges(ranges: list[tuple[int, int]]) -> list[tuple[int, int]]:
    if not ranges:
        return []
    ranges.sort()
    merged: list[tuple[int, int]] = []
    cur_start, cur_end = ranges[0]
    for s, e in ranges[1:]:
        if s <= cur_end + 1:
            if e > cur_end:
                cur_end = e
        else:
            merged.append((cur_start, cur_end))
            cur_start, cur_end = s, e
    merged.append((cur_start, cur_end))
    return merged


def _number_in_ranges(num: int, merged: list[tuple[int, int]]) -> bool:
    # Binary search on starts
    starts = [r[0] for r in merged]
    i = bisect_left(starts, num)
    # Check previous range
    if i > 0:
        s, e = merged[i - 1]
        if s <= num <= e:
            return True
    # Check current range candidate
    if i < len(merged):
        s, e = merged[i]
        if s <= num <= e:
            return True
    return False


def _generate_repeated_numbers(max_len: int) -> set[int]:
    """Generate all numbers up to max_len digits that are repeated patterns (>=2 repeats)."""
    repeated: set[int] = set()
    for total_len in range(2, max_len + 1):
        # For each possible pattern length that divides total_len
        for k in range(1, total_len // 2 + 1):
            if total_len % k != 0:
                continue
            repeats = total_len // k
            if repeats < 2:
                continue
            start = 10 ** (k - 1)  # pattern cannot start with 0
            end = 10**k - 1
            for pattern in range(start, end + 1):
                s = str(pattern) * repeats
                num = int(s)
                repeated.add(num)
    return repeated


def some_function(file_name: str = "input.txt", part_two: bool = False) -> int:
    """Day 2: Gift Shop (double-repeat criterion)

    Invalid product IDs are numbers that consist of a digit sequence repeated exactly twice.

    Part 1: Sum all invalid product IDs across all ranges.
    Part 2: Count all invalid product IDs across all ranges.
    """
    directory = os.path.dirname(os.path.realpath(__file__))
    with open(os.path.join(directory, file_name), "r", encoding="utf-8") as file:
        content = file.read().strip()

    ranges = _parse_ranges(content)
    if not ranges:
        return 0

    merged = _merge_ranges(ranges)
    max_value = max(r[1] for r in merged)
    max_len = len(str(max_value))

    candidates = _generate_repeated_numbers(max_len)

    # For Part 2 under new rules, sum invalid IDs (unique within merged ranges)
    if part_two:
        invalid_ids: set[int] = set()
        for num in candidates:
            if _number_in_ranges(num, merged):
                invalid_ids.add(num)
        return sum(invalid_ids)

    # Part 1: Sum unique invalid IDs within merged ranges using double-repeat criterion (backwards-compatible)
    invalid_ids: set[int] = set()
    for num in candidates:
        if _number_in_ranges(num, merged):
            # Filter to only exactly two repeats for Part 1
            s = str(num)
            L = len(s)
            if L % 2 == 0:
                half = L // 2
                if s[:half][0] != '0' and s[:half] == s[half:]:
                    invalid_ids.add(num)
    return sum(invalid_ids)
