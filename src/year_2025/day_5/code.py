import os


def some_function(file_name, part_two=False):
    """
    Advent of Code 2025 - Day 5: Cafeteria
    Determine which ingredient IDs are fresh based on the given ranges.
    """
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, file_name)

    with open(file_path, "r") as file:
        content = file.read().strip()

    # Split into ranges section and ingredient IDs section
    sections = content.split("\n\n")
    ranges_section = sections[0].split("\n")
    ingredient_ids = [int(x) for x in sections[1].split("\n")]

    # Parse the ranges
    ranges = []
    for line in ranges_section:
        start, end = map(int, line.split("-"))
        ranges.append((start, end))

    if part_two:
        # Part 2: Count total unique ingredient IDs covered by all ranges
        # Merge overlapping ranges for efficiency
        if not ranges:
            return 0

        # Sort ranges by start position
        sorted_ranges = sorted(ranges)

        # Merge overlapping/adjacent ranges
        merged = [sorted_ranges[0]]
        for start, end in sorted_ranges[1:]:
            last_start, last_end = merged[-1]
            if start <= last_end + 1:  # Overlapping or adjacent
                merged[-1] = (last_start, max(last_end, end))
            else:
                merged.append((start, end))

        # Count total IDs in merged ranges
        total = sum(end - start + 1 for start, end in merged)
        return total

    # Part 1: Count how many ingredient IDs are fresh
    fresh_count = 0
    for ingredient_id in ingredient_ids:
        is_fresh = False
        for start, end in ranges:
            if start <= ingredient_id <= end:
                is_fresh = True
                break
        if is_fresh:
            fresh_count += 1

    return fresh_count
