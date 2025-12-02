import os


def some_function(file_name: str = "input.txt", part_two: bool = False) -> int:
    """
    Day 1: Secret Entrance
    
    You're at the North Pole and need to enter a safe — but the password is hidden, 
    and the entrance is locked. The safe has a circular dial with numbers 0 through 99. 
    It starts pointing at 50.
    
    Your puzzle input contains a sequence of rotations (one per line):
    - Each rotation starts with L (left/toward lower numbers) or R (right/toward higher numbers), 
      followed by the number of clicks.
    - When rotating, if you go past 0 left, it wraps to 99, and from 99 right, it wraps to 0.
    
    Part 1: Count the number of times the dial ends up pointing at 0 after any rotation.
    Part 2: Count every time the dial "touches" zero during a move (including crossing zero).
    """
    return_me: int = 0
    directory = os.path.dirname(os.path.realpath(__file__))
    with open(os.path.join(directory, file_name), "r") as file:
        all_lines = file.readlines()

    # TODO: Implement solution

    return return_me
