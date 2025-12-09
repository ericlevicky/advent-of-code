"""
Advent of Code 2025 - Day 8: Playground

Connect junction boxes with the shortest connections using Union-Find algorithm.
"""

import os
import math


class UnionFind:
    """Union-Find data structure for tracking connected components."""

    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, x):
        """Find the root of the set containing x."""
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]

    def union(self, x, y):
        """Union the sets containing x and y. Returns True if they were different sets."""
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return False  # Already in the same set

        # Union by size
        if self.size[root_x] < self.size[root_y]:
            root_x, root_y = root_y, root_x

        self.parent[root_y] = root_x
        self.size[root_x] += self.size[root_y]
        return True

    def get_component_sizes(self):
        """Get the sizes of all connected components."""
        component_sizes = {}
        for i in range(len(self.parent)):
            root = self.find(i)
            component_sizes[root] = self.size[root]
        return list(component_sizes.values())


def parse_input(input_text: str):
    """Parse the input text into a list of 3D coordinates."""
    lines = input_text.strip().split("\n")
    points = []
    for line in lines:
        x, y, z = map(int, line.split(","))
        points.append((x, y, z))
    return points


def distance(p1, p2):
    """Calculate Euclidean distance between two 3D points."""
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2 + (p1[2] - p2[2]) ** 2)


def part1(file_name: str) -> int:
    """Solve part 1: Connect 1000 closest pairs and multiply 3 largest circuit sizes."""
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, file_name)

    with open(file_path, encoding="utf-8") as f:
        input_text = f.read()

    points = parse_input(input_text)
    n = len(points)

    # Create all possible edges with their distances
    edges = []
    for i in range(n):
        for j in range(i + 1, n):
            dist = distance(points[i], points[j])
            edges.append((dist, i, j))

    # Sort edges by distance
    edges.sort()

    # Use Union-Find to connect closest pairs
    uf = UnionFind(n)

    # For test case, try 10 connections; for real input, try 1000
    # Note: "try" means attempt, even if already connected
    max_attempts = 10 if file_name == "test.txt" else 1000

    for idx in range(max_attempts):
        dist, i, j = edges[idx]
        uf.union(i, j)  # Attempt to union (may not merge if already connected)

    # Get sizes of all circuits
    circuit_sizes = uf.get_component_sizes()
    circuit_sizes.sort(reverse=True)

    # Multiply the three largest circuit sizes
    result = circuit_sizes[0] * circuit_sizes[1] * circuit_sizes[2]
    return result


def part2(file_name: str) -> int:
    """Solve part 2: Connect all junction boxes and return product of X coordinates of last connection."""
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, file_name)

    with open(file_path, encoding="utf-8") as f:
        input_text = f.read()

    points = parse_input(input_text)
    n = len(points)

    # Create all possible edges with their distances
    edges = []
    for i in range(n):
        for j in range(i + 1, n):
            dist = distance(points[i], points[j])
            edges.append((dist, i, j))

    # Sort edges by distance
    edges.sort()

    # Use Union-Find to connect closest pairs
    uf = UnionFind(n)
    last_connection = None

    # Keep connecting until all junction boxes are in one circuit
    for dist, i, j in edges:
        if uf.union(i, j):
            # Check if all are now connected (only 1 component)
            component_sizes = uf.get_component_sizes()
            if len(component_sizes) == 1:
                # This was the last connection needed
                last_connection = (i, j)
                break

    # Return the product of X coordinates of the last two junction boxes
    if last_connection:
        i, j = last_connection
        return points[i][0] * points[j][0]

    return 0


if __name__ == "__main__":
    print("Test Part 1:", part1("test.txt"))
    print("Test Part 2:", part2("test.txt"))
    print("Part 1:", part1("input.txt"))
    print("Part 2:", part2("input.txt"))
