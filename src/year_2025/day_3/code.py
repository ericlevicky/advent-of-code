from pathlib import Path

INPUT_DIR = Path(__file__).parent


def read_input(filename: str) -> list[str]:
    path = INPUT_DIR / filename
    return [line.strip() for line in path.read_text().splitlines()]


def _max_joltage_for_bank(digits: list[int], k: int) -> int:
    """Pick exactly k digits (preserving order) to form the maximum integer."""
    n = len(digits)
    if k <= 0 or n == 0:
        return 0
    if k > n:
        # Not enough digits; cannot form k-length number
        return 0
    result: list[int] = []
    start = 0
    for i in range(k):
        remaining = k - i
        end = n - remaining  # last index we can search to ensure enough digits remain
        max_digit = -1
        max_idx = start
        for j in range(start, end + 1):
            d = digits[j]
            if d > max_digit:
                max_digit = d
                max_idx = j
                if max_digit == 9:
                    # Early exit: can't beat 9
                    break
        result.append(max_digit)
        start = max_idx + 1
    # Convert selected digits to integer
    val = 0
    for d in result:
        val = val * 10 + d
    return val


def some_function(filename: str, part_two: bool = False) -> int:
    lines = read_input(filename)
    total = 0
    k = 12 if part_two else 2
    for raw in lines:
        if not raw or raw.startswith("//"):
            continue
        digits = [int(ch) for ch in raw if ch.isdigit()]
        total += _max_joltage_for_bank(digits, k)
    return total
