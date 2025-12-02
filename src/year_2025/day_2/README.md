# Day 2: Gift Shop

## Problem Description

You are tasked with finding **invalid product IDs** in a series of ranges. An invalid product ID is any number that consists of a digit sequence repeated (for example: 55, 6464, or 123123 — all are invalid because they repeat their pattern).

The input is a list of ranges formatted as `start-end`, separated by commas.

### Examples

- `11` is invalid (1 repeated)
- `22` is invalid (2 repeated)
- `99` is invalid (9 repeated)
- `1010` is invalid (10 repeated)
- `123123` is invalid (123 repeated)
- `446446` is invalid (446 repeated)
- `12` is valid (not a repeated pattern)
- `123` is valid (not a repeated pattern)

### Part 1

For each range in the input, find all invalid product IDs (numbers made of a repeated sequence of digits), then sum them.

### Part 2

Find the count of invalid product IDs across all ranges.

### Sample Input

```
11-22,95-115,998-1012
```

In this example:
- Range 11-22: Invalid IDs are 11, 22 (both are repeated digits)
- Range 95-115: Invalid IDs are 99, 1010, 1111
- Range 998-1012: Invalid IDs are 99, 1010, 1111, etc.

### Solution Notes

To check if a number is a "repeated sequence":
1. Convert the number to a string
2. For each possible divisor of the string length, check if the string equals the first substring repeated

```python
def is_repeated_sequence(num):
    s = str(num)
    l = len(s)
    for i in range(1, l // 2 + 1):
        if l % i == 0 and s == s[:i] * (l // i):
            return True
    return False
```

---

Source: [Advent of Code 2025 Day 2](https://adventofcode.com/2025/day/2)
