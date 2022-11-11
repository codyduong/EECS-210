"""
Author: Cody Duong <cody.qd@gmail.com> (https://github.com/codyduong)
KUID: 3050266
Date: 2022-11-10
Lab: Assignment 6
Purpose: Reads input file in specified format

EXAMPLE:
5 _ _ _ _ _ 1 7 _
1 _ 6 5 _ 9 _ 4 _
4 7 2 1 _ 6 _ _ _
9 _ _ _ _ _ 5 _ _
_ 1 8 _ 9 5 4 _ _
6 _ _ 4 _ 2 3 8 9
_ 4 _ _ _ _ 9 3 _
_ 9 _ 7 _ 3 _ 5 _
2 6 3 9 5 8 7 1 4
"""

from os import listdir
from os.path import isfile, join


def reader(filename: str) -> list[list[int | None]]:
    with open(filename, encoding="utf8") as f:
        return [
            [int(char) if char != "_" else None for char in line.strip().split(" ")]
            for line in f.readlines()
        ]


def read_all(directory: str) -> dict[str, list[list[int | None]]]:
    files: list[str] = [f for f in listdir(directory) if isfile(join(directory, f))]
    puzzles: dict[str, list[list[int | None]]] = {file: reader(f"puzzles/{file}") for file in files}
    return puzzles
