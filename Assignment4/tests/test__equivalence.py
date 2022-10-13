"""
Author: Cody Duong <cody.qd@gmail.com> (https://github.com/codyduong)
KUID: 3050266
Date: 2022-10-13
Lab: Assignment 4
Purpose: Symmetry Tests
"""


from typing import Any
import unittest
from src.equivalence import equivalence, EquivalenceReturn


class TestEquivalenceFunction(unittest.TestCase):
    # maxDiff = None

    def __init__(self, *args) -> None:  # type: ignore
        super().__init__(*args)  # type: ignore

        self.tests: list[
            tuple[
                tuple[
                    set[tuple[Any, Any]] | list[tuple[Any, Any]],
                    set[Any] | list[Any],
                    bool,
                ],
                EquivalenceReturn,
            ]
        ] = [
            # 4d
            (
                (
                    {(1, 1), (2, 2), (2, 3)},
                    {1, 2, 3},
                    False,
                ),
                {
                    "r": {(1, 1), (2, 2), (2, 3)},
                    "equivalence": False,
                    "reflexive": False,
                    "symmetric": False,
                    "transitive": True,
                },
            ),
            (
                (
                    {(1, 1), (2, 2), (2, 3)},
                    {1, 2, 3},
                    True,
                ),
                {
                    "r": {(1, 1), (2, 2), (2, 3)},
                    "equivalence": False,
                    "reflexive": False,
                    "symmetric": False,
                    "transitive": True,
                },
            ),
            # 4e
            (
                (
                    {("a", "a"), ("b", "b"), ("c", "c"), ("b", "c"), ("c", "b")},
                    {"a", "b", "c"},
                    False,
                ),
                {
                    "r": {("a", "a"), ("b", "b"), ("c", "c"), ("b", "c"), ("c", "b")},
                    "equivalence": True,
                    "reflexive": True,
                    "symmetric": True,
                    "transitive": True,
                },
            ),
            # other
        ]

    def test_inputs(self) -> None:
        for (input, output) in self.tests:
            self.assertDictEqual(equivalence(*input), output)
