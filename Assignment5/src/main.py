"""
Author: Cody Duong <cody.qd@gmail.com> (https://github.com/codyduong)
KUID: 3050266
Date: 2022-10-26
Lab: Assignment 5
Purpose: Def call for assignment5
"""


import json
from typing import List
from src.relation import Relation


def problems() -> None:
    """
    Read the problemset from the json file (_problems.json)
    """
    problems = None  # type: ignore
    with open("_problems.json") as f:
        problems: List[
            tuple[
                str,
                tuple[
                    set[str],
                    set[str],
                    set[tuple[str, str]],
                ],
            ]
        ] = [(name, problem["args"]) for name, problem in json.load(f).items()]

    for name, args in problems:
        print(f"{name}", Relation(*args), "\n")
