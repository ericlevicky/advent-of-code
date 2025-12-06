import os


def solve_worksheet(file_name, part_two=False):
    """
    Advent of Code 2025 - Day 6: Trash Compactor
    Parse cephalopod math worksheet and calculate the grand total.

    Part 1: Read numbers horizontally (left-to-right rows)
    Part 2: Read numbers vertically in columns (right-to-left, top-to-bottom)
    """
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, file_name)

    with open(file_path, "r") as file:
        lines = file.read().splitlines()

    # Parse the worksheet
    # Remove empty lines
    data_rows = [line for line in lines if line.strip()]

    if not data_rows:
        return 0

    # Last row contains operators
    operator_row = data_rows[-1]
    number_rows = data_rows[:-1]

    # Pad all rows to the same length
    max_length = max(len(row) for row in data_rows)
    padded_rows = [row.ljust(max_length) for row in data_rows]
    operator_row = padded_rows[-1]
    number_rows = padded_rows[:-1]

    if part_two:
        # Part 2: Read right-to-left in columns
        # Each number is in its own column, read top-to-bottom
        problems = []
        col = 0

        while col < max_length:
            # Skip columns that are all spaces
            if all(row[col] == " " for row in padded_rows):
                col += 1
                continue

            # Found the start of a problem - collect all columns until we hit all spaces
            problem_start = col
            problem_end = col

            # Extend to include all adjacent non-all-space columns
            while problem_end < max_length:
                if all(row[problem_end] == " " for row in padded_rows):
                    break
                problem_end += 1

            # Extract the operator for this problem
            operator_text = operator_row[problem_start:problem_end].strip()
            operator = None
            for char in operator_text:
                if char in ["+", "*"]:
                    operator = char
                    break

            # Extract numbers by reading each column right-to-left, top-to-bottom
            numbers = []
            for c in range(problem_end - 1, problem_start - 1, -1):  # Right-to-left
                # Read this column top-to-bottom to form a number
                digits = []
                for row in number_rows:
                    if c < len(row) and row[c].isdigit():
                        digits.append(row[c])

                if digits:
                    # Combine digits top-to-bottom to form number
                    number = int("".join(digits))
                    numbers.append(number)

            if operator and numbers:
                problems.append((operator, numbers))

            col = problem_end

    else:
        # Part 1: Read left-to-right horizontally (original logic)
        # Identify problem columns by finding where operators are
        # and grouping adjacent non-space columns
        problems = []
        col = 0

        while col < max_length:
            # Skip columns that are all spaces
            if all(row[col] == " " for row in padded_rows):
                col += 1
                continue

            # Found the start of a problem - collect all columns until we hit all spaces
            problem_start = col
            problem_end = col

            # Extend to include all adjacent non-all-space columns
            while problem_end < max_length:
                if all(row[problem_end] == " " for row in padded_rows):
                    break
                problem_end += 1

            # Extract the problem from this column range
            problem_text = [row[problem_start:problem_end] for row in number_rows]
            operator_text = operator_row[problem_start:problem_end].strip()

            # Find the operator
            operator = None
            for char in operator_text:
                if char in ["+", "*"]:
                    operator = char
                    break

            # Extract numbers from the problem text
            numbers = []
            for row_text in problem_text:
                # Extract all numbers from this row
                row_text = row_text.strip()
                if row_text and row_text.replace(" ", "").isdigit():
                    # Could be one or more numbers separated by spaces
                    parts = row_text.split()
                    for part in parts:
                        if part.isdigit():
                            numbers.append(int(part))

            if operator and numbers:
                problems.append((operator, numbers))

            col = problem_end

    # Calculate answers for each problem
    grand_total = 0

    for operator, numbers in problems:
        if operator == "+":
            result = sum(numbers)
        else:  # operator == '*'
            result = 1
            for num in numbers:
                result *= num

        grand_total += result

    return grand_total


if __name__ == "__main__":
    # Test with example
    test_result = solve_worksheet("test.txt")
    print(f"Part 1 Test result: {test_result}")

    # Solve with actual input
    result = solve_worksheet("input.txt")
    print(f"Part 1 result: {result}")

    # Part 2
    test_result_2 = solve_worksheet("test.txt", True)
    print(f"Part 2 Test result: {test_result_2}")

    result_2 = solve_worksheet("input.txt", True)
    print(f"Part 2 result: {result_2}")
