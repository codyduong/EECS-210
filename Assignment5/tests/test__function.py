"""
Author: Cody Duong <cody.qd@gmail.com> (https://github.com/codyduong)
KUID: 3050266
Date: 2022-10-26
Lab: Assignment 5
Purpose: is_function tests
"""


import json
import unittest
from src.function import function


class TestIsFunction(unittest.TestCase):
    # maxDiff = None

    def __init__(self, *args) -> None:  # type: ignore
        super().__init__(*args)  # type: ignore

        with open("_problems.json") as f, open("tests/mocks/extra.json") as h:
            self.tests: list[
                tuple[
                    str,
                    tuple[
                        set[str],
                        set[str],
                        set[tuple[str, str]],
                    ],
                    bool,
                ]
            ] = [
                (name, problem["args"], problem["answer"]["is_function"])
                for name, problem in (json.load(f) | json.load(h)).items()
            ]

    def test_problems(self) -> None:
        for (name, input, output) in self.tests:
            try:
                self.assertEqual(function(*input), output)
            except Exception as e:
                print(name, input, output)
                raise e
