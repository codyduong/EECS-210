"""
Author: Cody Duong <cody.qd@gmail.com> (https://github.com/codyduong)
KUID: 3050266
Date: 2022-11-10
Lab: Assignment 6
Purpose: Util formatter
"""

def format(puzzle: list[list[int | None]]) -> str:
    """
    Nicely formats a board position into an easily representable state
    """
    return "\n".join(
        [
            "".join([f"{char}" if char is not None else "." for char in row])
            for row in puzzle
        ]
    )
