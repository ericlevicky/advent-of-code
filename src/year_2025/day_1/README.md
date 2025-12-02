# Day 1: Secret Entrance

## Problem Description

You're at the North Pole and need to enter a safe — but the password is hidden, and the entrance is locked. The safe has a circular dial with numbers 0 through 99. It starts pointing at 50.

Your puzzle input contains a sequence of rotations (one per line):
- Each rotation starts with `L` (left/toward lower numbers) or `R` (right/toward higher numbers), followed by the number of clicks.
- When rotating, if you go past 0 left, it wraps to 99, and from 99 right, it wraps to 0.

### Examples

Starting at 11:
- `R8` puts you at 19
- Then `L19` would give you 0

From 5:
- `L10` leads to 95

### Part 1

Follow the instruction sequence. The password is the **number of times the dial ends up pointing at 0 after any rotation**.

### Part 2

Count each "click" where the dial points at 0, not just the final position — including intermediate passes through 0 if the dial wraps multiple times in a rotation.

### Sample Input

```
L68
L30
R48
L5
R60
L55
L1
L99
R14
L82
```

With this, the dial starts at 50 and you perform rotations you're given. Count how many times you end at 0 after a rotation.

### Solution Notes

For the solution, use modular arithmetic to handle the "circular" dial:
- For a right rotation: `(position + steps) % 100`
- For a left rotation: `(position - steps) % 100`

For each step, update position and increment your counter if you land on 0.

---

Source: [Advent of Code 2025 Day 1](https://adventofcode.com/2025/day/1)
