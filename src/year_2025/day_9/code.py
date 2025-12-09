"""
Advent of Code 2025 - Day 9

Placeholder for Day 9 puzzle.
"""

import os


def parse_input(input_text: str):
    """Parse the input text into a list of coordinate tuples."""
    lines = input_text.strip().split("\n")
    coordinates = []
    for line in lines:
        x, y = map(int, line.split(","))
        coordinates.append((x, y))
    return coordinates


def part1(file_name: str) -> int:
    """Solve part 1: Find the largest rectangle with red tiles at opposite corners."""
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, file_name)

    with open(file_path, encoding="utf-8") as f:
        input_text = f.read()

    red_tiles = parse_input(input_text)

    # Group tiles by x-coordinate for efficient searching
    x_groups = {}
    for x, y in red_tiles:
        if x not in x_groups:
            x_groups[x] = []
        x_groups[x].append(y)

    # Sort y-values within each x-group
    for x, _y in x_groups.items():
        x_groups[x].sort()

    max_area = 0

    # Sort tiles by x, then y for systematic processing
    sorted_tiles = sorted(red_tiles)

    # For each tile, look for other tiles with different x and y
    for x1, y1 in sorted_tiles:
        # Only check tiles to the right (larger x) to avoid duplicate checks
        for x2, _y2 in x_groups.items():
            if x2 <= x1:
                continue
            for y2 in x_groups[x2]:
                if y2 == y1:
                    continue
                # Calculate area
                width = abs(x2 - x1) + 1
                height = abs(y2 - y1) + 1
                area = width * height
                max_area = max(max_area, area)

    return max_area


def build_boundary_structure(red_tiles):
    """Build efficient boundary structure without materializing all interior tiles."""
    # Build the boundary edges - just track which rows exist and their x-ranges
    boundary_by_row = {}

    for i, (x1, y1) in enumerate(red_tiles):
        x2, y2 = red_tiles[(i + 1) % len(red_tiles)]

        if x1 == x2:  # Vertical edge - same column
            min_y, max_y = min(y1, y2), max(y1, y2)
            for y in range(min_y, max_y + 1):
                if y not in boundary_by_row:
                    boundary_by_row[y] = set()
                boundary_by_row[y].add(x1)
        elif y1 == y2:  # Horizontal edge - same row
            min_x, max_x = min(x1, x2), max(x1, x2)
            if y1 not in boundary_by_row:
                boundary_by_row[y1] = set()
            for x in range(min_x, max_x + 1):
                boundary_by_row[y1].add(x)

    # For each row, just store min and max x (representing continuous range)
    boundary_ranges = {}
    for y, xs in boundary_by_row.items():
        min_x = min(xs)
        max_x = max(xs)
        boundary_ranges[y] = (min_x, max_x)

    return boundary_ranges


def is_rectangle_valid(min_x, max_x, min_y, max_y, boundary_ranges):
    """Check if rectangle contains only tiles within or on the boundary."""
    for y in range(min_y, max_y + 1):
        if y not in boundary_ranges:
            return False

        row_min, row_max = boundary_ranges[y]

        # Rectangle needs all x from min_x to max_x to be valid
        # Valid tiles are from row_min to row_max (inclusive, continuous)
        if min_x < row_min or max_x > row_max:
            return False

    return True


def part2(file_name: str) -> int:
    """Solve part 2: Find largest rectangle with red corners using only red/green tiles."""
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, file_name)

    with open(file_path, encoding="utf-8") as f:
        input_text = f.read()

    red_tiles = parse_input(input_text)
    boundary_ranges = build_boundary_structure(red_tiles)

    max_area = 0

    # Check all pairs of red tiles as corners
    # Process in order that favors finding large rectangles early
    candidates = []
    for i, (x1, y1) in enumerate(red_tiles):
        for j in range(i + 1, len(red_tiles)):
            x2, y2 = red_tiles[j]

            if x1 == x2 or y1 == y2:  # Same row or column, skip
                continue

            # Pre-calculate area
            width = abs(x2 - x1) + 1
            height = abs(y2 - y1) + 1
            area = width * height
            candidates.append((area, x1, y1, x2, y2))

    # Sort by area descending - check largest first
    candidates.sort(reverse=True)

    for area, x1, y1, x2, y2 in candidates:
        # Skip if this can't beat current max
        if area <= max_area:
            break  # All remaining are smaller

        min_x, max_x = min(x1, x2), max(x1, x2)
        min_y, max_y = min(y1, y2), max(y1, y2)

        # Optimized validation: check extremes first, then sample middle
        # Most failures happen at edges
        all_valid = True

        # Check corners and edges first (most likely to fail)
        critical_ys = [min_y, max_y, (min_y + max_y) // 2]
        for y in critical_ys:
            if y not in boundary_ranges:
                all_valid = False
                break
            row_min, row_max = boundary_ranges[y]
            if min_x < row_min or max_x > row_max:
                all_valid = False
                break

        # If extremes pass, check all remaining y values
        if all_valid:
            for y in range(min_y, max_y + 1):
                if y in critical_ys:
                    continue
                if y not in boundary_ranges:
                    all_valid = False
                    break

                row_min, row_max = boundary_ranges[y]
                if min_x < row_min or max_x > row_max:
                    all_valid = False
                    break

        if all_valid:
            max_area = area

    return max_area


if __name__ == "__main__":
    print("Test Part 1:", part1("test.txt"))
    print("Test Part 2:", part2("test.txt"))
    print("Part 1:", part1("input.txt"))
    print("Part 2:", part2("input.txt"))
