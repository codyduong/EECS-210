"""
Author: Cody Duong <cody.qd@gmail.com> (https://github.com/codyduong)
KUID: 3050266
Date: 2022-11-10
Lab: Assignment 6
Purpose: Entry file
"""

from src.reader import *
from src.Solver import Solver
from src.formatter import format

puzzles: dict[str, list[list[int | None]]] = read_all("puzzles")
solver: Solver = Solver()
for name, puzzle in puzzles.items():
    print(name)
    solutions = solver.solve(puzzle)
    if len(solutions) > 0:
        for solution in solutions:
            print(format(solution) + "\n")
        print(f"Solutions Found: {len(solutions)}" + "\n")
    else:
        print("No solutions\n")
