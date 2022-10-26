"""
Author: Cody Duong <cody.qd@gmail.com> (https://github.com/codyduong)
KUID: 3050266
Date: 2022-10-26
Lab: Assignment 5
Purpose: surjective tests
"""


import json
import unittest
from src.function import function
from src.surjective import surjective


class TestSurjective(unittest.TestCase):
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
                (name, problem["args"], problem["answer"]["surjective"])
                for name, problem in (json.load(f) | json.load(h)).items()
                if function(*problem["args"])
            ]

    def test_problems(self) -> None:
        for (name, input, output) in self.tests:
            try:
                self.assertEqual(surjective(input[1], input[2]), output)
            except Exception as e:
                print(name, input, output)
                raise e
