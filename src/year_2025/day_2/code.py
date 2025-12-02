import os


def is_repeated_sequence(num: int) -> bool:
    """
    Check if a number consists of a repeated digit sequence.
    
    Examples:
        55 -> True (5 repeated)
        1010 -> True (10 repeated)
        123123 -> True (123 repeated)
        12 -> False
        123 -> False
    """
    s = str(num)
    length = len(s)
    for i in range(1, length // 2 + 1):
        if length % i == 0 and s == s[:i] * (length // i):
            return True
    return False


def some_function(file_name: str = "input.txt", part_two: bool = False) -> int:
    """
    Day 2: Gift Shop

    Find invalid product IDs in ranges. An invalid product ID is any number
    that consists of a digit sequence repeated (e.g., 55, 6464, 123123).

    Part 1: Sum all invalid product IDs across all ranges.
    Part 2: Count all invalid product IDs across all ranges.
    """
    return_me: int = 0
    directory = os.path.dirname(os.path.realpath(__file__))
    with open(os.path.join(directory, file_name), "r") as file:
        content = file.read().strip()

    # Parse ranges from the input (comma-separated, format: start-end)
    ranges = []
    for range_str in content.split(","):
        range_str = range_str.strip()
        if "-" in range_str:
            # Use rsplit to handle potential edge cases with negative numbers
            parts = range_str.rsplit("-", 1)
            if len(parts) == 2:
                start = int(parts[0])
                end = int(parts[1])
                ranges.append((start, end))

    invalid_ids = set()

    for start, end in ranges:
        for num in range(start, end + 1):
            if is_repeated_sequence(num):
                invalid_ids.add(num)

    if part_two:
        # Part 2: Count of invalid IDs
        return_me = len(invalid_ids)
    else:
        # Part 1: Sum of invalid IDs
        return_me = sum(invalid_ids)

    return return_me
