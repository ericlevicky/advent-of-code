import os


def some_function(file_name, part_two=False):
    """
    Advent of Code 2025 - Day 4
    Count rolls of paper that can be accessed by a forklift.
    A roll can be accessed if fewer than 4 of its 8 adjacent positions contain paper.
    """
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, file_name)

    with open(file_path, "r") as file:
        lines = file.read().strip().split("\n")

    # Create grid
    grid = [list(line) for line in lines]
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0

    # Directions for 8 adjacent positions (N, NE, E, SE, S, SW, W, NW)
    directions = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]

    if part_two:
        # Part 2: Remove all accessible rolls iteratively
        total_removed = 0

        while True:
            # Find all accessible rolls in current state
            accessible = []

            for r in range(rows):
                for c in range(cols):
                    if grid[r][c] == "@":
                        # Count adjacent rolls
                        adjacent_rolls = 0
                        for dr, dc in directions:
                            nr, nc = r + dr, c + dc
                            if (
                                0 <= nr < rows
                                and 0 <= nc < cols
                                and grid[nr][nc] == "@"
                            ):
                                adjacent_rolls += 1

                        # Roll is accessible if fewer than 4 adjacent rolls
                        if adjacent_rolls < 4:
                            accessible.append((r, c))

            # If no accessible rolls, we're done
            if not accessible:
                break

            # Remove all accessible rolls
            for r, c in accessible:
                grid[r][c] = "."

            total_removed += len(accessible)

        return total_removed
    else:
        # Part 1: Count rolls accessible by forklift
        accessible_count = 0

        for r in range(rows):
            for c in range(cols):
                # Check if current position is a roll of paper
                if grid[r][c] == "@":
                    # Count adjacent rolls
                    adjacent_rolls = 0
                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc
                        # Check if adjacent position is in bounds and contains paper
                        if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == "@":
                            adjacent_rolls += 1

                    # Roll is accessible if fewer than 4 adjacent rolls
                    if adjacent_rolls < 4:
                        accessible_count += 1

        return accessible_count

    return 0


if __name__ == "__main__":
    print("Part 1:", some_function("input.txt"))
    print("Part 2:", some_function("input.txt", True))
