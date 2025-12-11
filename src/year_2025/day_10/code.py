"""
Advent of Code 2025 - Day 10

Factory initialization with indicator lights and buttons.
"""

import math
import os
import re
from fractions import Fraction


def parse_machine(line: str):
    """Parse a machine line into target state, button configurations, and joltage requirements."""
    # Extract indicator lights target state
    lights_match = re.search(r"\[([.#]+)\]", line)
    target = [1 if c == "#" else 0 for c in lights_match.group(1)]

    # Extract button configurations
    buttons = []
    for match in re.finditer(r"\(([0-9,]+)\)", line):
        button = [int(x) for x in match.group(1).split(",")]
        buttons.append(button)

    # Extract joltage requirements
    joltage_match = re.search(r"\{([0-9,]+)\}", line)
    joltage = [int(x) for x in joltage_match.group(1).split(",")]

    return target, buttons, joltage


def solve_machine(target, buttons):
    """Find minimum button presses to achieve target state using Gaussian elimination over GF(2)."""
    n_lights = len(target)
    n_buttons = len(buttons)

    # Build the matrix where each column represents a button
    # and each row represents a light
    matrix = [[0] * n_buttons for _ in range(n_lights)]

    for btn_idx, button in enumerate(buttons):
        for light_idx in button:
            matrix[light_idx][btn_idx] = 1

    # Augmented matrix [A | b] for Ax = b (mod 2)
    aug = [row[:] + [target[i]] for i, row in enumerate(matrix)]

    # Gaussian elimination with partial pivoting
    pivot_cols = []
    row = 0

    for col in range(n_buttons):
        # Find pivot
        pivot_row = None
        for r in range(row, n_lights):
            if aug[r][col] == 1:
                pivot_row = r
                break

        if pivot_row is None:
            continue

        # Swap rows
        aug[row], aug[pivot_row] = aug[pivot_row], aug[row]
        pivot_cols.append(col)

        # Eliminate
        for r in range(n_lights):
            if r != row and aug[r][col] == 1:
                for c in range(n_buttons + 1):
                    aug[r][c] ^= aug[row][c]

        row += 1

    # Check for inconsistency
    for r in range(row, n_lights):
        if aug[r][n_buttons] == 1:
            return float("inf")  # No solution

    # Find minimum solution by trying all combinations of free variables
    n_free = n_buttons - len(pivot_cols)
    free_vars = [i for i in range(n_buttons) if i not in pivot_cols]

    min_presses = float("inf")

    # Try all 2^n_free combinations of free variables
    for mask in range(1 << n_free):
        solution = [0] * n_buttons

        # Set free variables
        for i, var in enumerate(free_vars):
            solution[var] = (mask >> i) & 1

        # Back-substitute for pivot variables
        for i in range(len(pivot_cols) - 1, -1, -1):
            col = pivot_cols[i]
            val = aug[i][n_buttons]
            for j in range(col + 1, n_buttons):
                val ^= aug[i][j] * solution[j]
            solution[col] = val

        # Count button presses
        presses = sum(solution)
        min_presses = min(min_presses, presses)

    return min_presses


def solve_joltage(joltage, buttons):
    """Find minimum button presses by solving Ax = b over the integers."""

    def small_problem():
        """Use Dijkstra search when the total demand is tiny."""
        import heapq

        target = tuple(joltage)
        pq = [(0, tuple([0] * len(joltage)))]
        seen = set()

        while pq:
            cost, state = heapq.heappop(pq)
            if state in seen:
                continue
            seen.add(state)
            if state == target:
                return cost

            for button in buttons:
                new_state = list(state)
                for counter in button:
                    new_state[counter] += 1
                    if new_state[counter] > target[counter]:
                        break
                else:
                    tup = tuple(new_state)
                    if tup not in seen:
                        heapq.heappush(pq, (cost + 1, tup))

        return float("inf")

    def build_matrix():
        rows = len(joltage)
        cols = len(buttons)
        mat = [[Fraction(0) for _ in range(cols)] for _ in range(rows)]
        for col, button in enumerate(buttons):
            for row in button:
                mat[row][col] = Fraction(1)
        return mat

    def to_rref(matrix, rhs):
        rows = len(matrix)
        cols = len(matrix[0]) if rows else 0
        aug = [matrix[r][:] + [Fraction(rhs[r])] for r in range(rows)]
        pivot_cols = []
        pivot_row = 0

        for col in range(cols):
            pivot = None
            for r in range(pivot_row, rows):
                if aug[r][col] != 0:
                    pivot = r
                    break
            if pivot is None:
                continue

            aug[pivot_row], aug[pivot] = aug[pivot], aug[pivot_row]
            pivot_val = aug[pivot_row][col]
            for c in range(col, cols + 1):
                aug[pivot_row][c] /= pivot_val

            for r in range(rows):
                if r != pivot_row and aug[r][col] != 0:
                    factor = aug[r][col]
                    for c in range(col, cols + 1):
                        aug[r][c] -= factor * aug[pivot_row][c]

            pivot_cols.append(col)
            pivot_row += 1
            if pivot_row == rows:
                break

        # Check for inconsistency
        for r in range(pivot_row, rows):
            if all(aug[r][c] == 0 for c in range(cols)) and aug[r][cols] != 0:
                return None, None

        return [aug[i][:] for i in range(pivot_row)], pivot_cols

    def construct_solution(pivot_rows, pivot_cols, free_cols, free_vals):
        total_vars = len(buttons)
        sol = [Fraction(0) for _ in range(total_vars)]
        for idx, col in enumerate(free_cols):
            sol[col] = Fraction(free_vals[idx])

        for row_idx, col in enumerate(pivot_cols):
            row = pivot_rows[row_idx]
            val = row[-1]
            for free_idx, free_col in enumerate(free_cols):
                coeff = row[free_col]
                if coeff != 0:
                    val -= coeff * sol[free_col]
            sol[col] = val

        ints = []
        for value in sol:
            if value.denominator != 1 or value < 0:
                return None
            ints.append(int(value))

        # Verify the solution exactly meets the targets
        achieved = [0] * len(joltage)
        for btn_idx, presses in enumerate(ints):
            if presses == 0:
                continue
            for counter_idx in buttons[btn_idx]:
                achieved[counter_idx] += presses

        if achieved != list(joltage):
            return None

        return ints

    if sum(joltage) <= 50:
        return small_problem()

    matrix = build_matrix()
    pivot_rows, pivot_cols = to_rref(matrix, joltage)
    if pivot_rows is None:
        return float("inf")

    n_buttons = len(buttons)
    free_cols = [col for col in range(n_buttons) if col not in pivot_cols]

    if not free_cols:
        solution = construct_solution(pivot_rows, pivot_cols, [], [])
        return sum(solution) if solution is not None else float("inf")

    rhs_values = [row[-1] for row in pivot_rows]
    coeff_matrix = [[row[col] for col in free_cols] for row in pivot_rows]

    def floor_fraction(frac: Fraction) -> int:
        return math.floor(frac)

    bounds = []
    for col in free_cols:
        if buttons[col]:
            bound = min(joltage[idx] for idx in buttons[col])
        else:
            bound = 0
        bounds.append(max(bound, 0))

    order = sorted(range(len(free_cols)), key=lambda idx: bounds[idx])
    free_vals = [0] * len(free_cols)
    assigned = [False] * len(free_cols)
    best_cost = float("inf")
    best_solution = None

    def feasible_partial():
        for row_idx, rhs in enumerate(rhs_values):
            expr = rhs
            for idx, coeff in enumerate(coeff_matrix[row_idx]):
                if assigned[idx]:
                    expr -= coeff * free_vals[idx]

            max_possible = expr
            for idx, coeff in enumerate(coeff_matrix[row_idx]):
                if assigned[idx]:
                    continue
                if coeff < 0:
                    max_possible -= coeff * bounds[idx]

            if max_possible < 0:
                return False
        return True

    def dfs(pos, current_sum):
        nonlocal best_cost, best_solution
        if current_sum >= best_cost:
            return
        if pos == len(order):
            candidate = construct_solution(
                pivot_rows,
                pivot_cols,
                free_cols,
                free_vals,
            )
            if candidate is None:
                return
            cost = sum(candidate)
            if cost < best_cost:
                best_cost = cost
                best_solution = candidate
            return

        idx = order[pos]
        max_val = bounds[idx]
        if max_val < 0:
            return
        for value in range(max_val + 1):
            free_vals[idx] = value
            assigned[idx] = True
            if feasible_partial():
                dfs(pos + 1, current_sum + value)
            assigned[idx] = False
        free_vals[idx] = 0

    dfs(0, 0)
    if best_solution is None:
        return float("inf")
    return sum(best_solution)


def parse_input(input_text: str):
    """Parse the input text."""
    lines = input_text.strip().split("\n")
    machines = []
    for line in lines:
        if line.strip():
            target, buttons, joltage = parse_machine(line)
            machines.append((target, buttons, joltage))
    return machines


def part1(file_name: str) -> int:
    """Solve part 1."""
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, file_name)

    with open(file_path, encoding="utf-8") as f:
        input_text = f.read()

    machines = parse_input(input_text)

    total = 0
    for target, buttons, _ in machines:
        presses = solve_machine(target, buttons)
        total += presses

    return total


def part2(file_name: str) -> int:
    """Solve part 2."""
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, file_name)

    with open(file_path, encoding="utf-8") as f:
        input_text = f.read()

    machines = parse_input(input_text)

    total = 0
    for _, buttons, joltage in machines:
        presses = solve_joltage(joltage, buttons)
        total += presses

    return total


if __name__ == "__main__":
    print("Test Part 1:", part1("test.txt"))
    print("Test Part 2:", part2("test.txt"))
    print("Part 1:", part1("input.txt"))
    print("Part 2:", part2("input.txt"))
