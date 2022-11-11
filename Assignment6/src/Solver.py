"""
Author: Cody Duong <cody.qd@gmail.com> (https://github.com/codyduong)
KUID: 3050266
Date: 2022-11-10
Lab: Assignment 6
Purpose: Recursively solve sudoku puzzle
"""


from copy import deepcopy
from typing import Literal
# from src.formatter import format


class Solver:
    def _solve(
        self, puzzle: list[list[int | None]], row: int, col: int
    ) -> list[list[list[int | None]]]:
        solutions: list[list[list[int | None]]] = []

        newCol: int = col + 1
        newRow: int = row
        if newCol > 8:
            # end of col, move to next row
            newCol = 0
            newRow += 1

        try:
            if puzzle[row][col] is not None:
                # move onto next row/col
                return self._solve(deepcopy(puzzle), newRow, newCol)
            else:
                for i in range(1, 10):
                    modifiedPuzzle: list[list[int | None]] = deepcopy(
                        puzzle
                    )  # this is dumb
                    # try every possible number to replace
                    modifiedPuzzle[row][col] = i
                    # validate if it's a good iteration
                    if self.validate(modifiedPuzzle):
                        # print(f"good iteration {i} found for char at: {row} {col}")
                        # print(format(modifiedPuzzle))
                        # if it is try searching deeper
                        potential_sol: list[
                            list[list[int | None]]
                        ] | None = self._solve(modifiedPuzzle, newRow, newCol)

                        solutions += potential_sol
                    else:
                        pass
                        # print(f"validation failed trying {i} at {row} {col}")
                        # print(format(modifiedPuzzle))
        except IndexError:
            # we went past the end of the puzzle, which means we solved it
            return [puzzle]

        return solutions

    def solve(self, puzzle: list[list[int | None]]) -> list[list[list[int | None]]]:
        return self._solve(puzzle, 0, 0)

    def validate(self, puzzle: list[list[int | None]]) -> bool:
        for i in range(9):
            row: dict[int, Literal[True]] = {}
            column: dict[int, Literal[True]] = {}
            block: dict[int, Literal[True]] = {}
            row_cube: int = 3 * (i // 3)
            column_cube: int = 3 * (i % 3)
            for j in range(9):
                if puzzle[i][j] is not None and puzzle[i][j] in row:
                    return False
                row[puzzle[i][j]] = True  # type: ignore
                if puzzle[j][i] is not None and puzzle[j][i] in column:
                    return False
                column[puzzle[j][i]] = True  # type: ignore
                rc: int = row_cube + j // 3
                cc: int = column_cube + j % 3
                if puzzle[rc][cc] in block and puzzle[rc][cc] is not None:
                    return False
                block[puzzle[rc][cc]] = True  # type: ignore
        return True
