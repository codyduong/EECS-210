"""
Author: Cody Duong <cody.qd@gmail.com> (https://github.com/codyduong)
KUID: 3050266
Date: 2022-10-13
Lab: Assignment 4
Purpose: Poset Tests
"""


from typing import Any
import unittest
from src.poset import poset, PosetReturn


class TestPosetFunction(unittest.TestCase):
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
                PosetReturn,
            ]
        ] = [
            # from the slides on poset
            (
                (
                    {(1, 1), (1, 2), (2, 2), (3, 3), (4, 1), (4, 2), (4, 4)},
                    {1, 2, 3, 4},
                    True,
                ),
                {
                    "s": {1, 2, 3, 4},
                    "r": {(1, 1), (1, 2), (2, 2), (3, 3), (4, 1), (4, 2), (4, 4)},
                    "poset": True,
                    "reflexive": True,
                    "antisymmetric": True,
                    "transitive": True,
                },
            ),
            # modified version of above to be not antisymmetric
            (
                (
                    {(1, 1), (1, 2), (2, 2), (3, 3), (4, 1), (4, 2), (4, 4), (1, 4)},
                    {1, 2, 3, 4},
                    True,
                ),
                {
                    "s": {1, 2, 3, 4},
                    "r": {
                        (1, 1),
                        (1, 2),
                        (2, 2),
                        (3, 3),
                        (4, 1),
                        (4, 2),
                        (4, 4),
                        (1, 4),
                    },
                    "poset": False,
                    "reflexive": True,
                    "antisymmetric": False,
                    "transitive": True,
                },
            ),
            # modified version of above to be not reflexive
            (
                (
                    {(1, 1), (1, 2), (2, 2), (4, 1), (4, 2), (4, 4)},
                    {1, 2, 3, 4},
                    True,
                ),
                {
                    "s": {1, 2, 3, 4},
                    "r": {
                        (1, 1),
                        (1, 2),
                        (2, 2),
                        (4, 1),
                        (4, 2),
                        (4, 4),
                    },
                    "poset": False,
                    "reflexive": False,
                    "antisymmetric": True,
                    "transitive": True,
                },
            ),
            # modified version of above to be not transitive
            (
                (
                    {(1, 1), (1, 2), (2, 2), (2, 3), (3, 3)},
                    {1, 2, 3},
                    True,
                ),
                {
                    "s": {1, 2, 3},
                    "r": {(1, 1), (1, 2), (2, 2), (2, 3), (3, 3)},
                    "poset": False,
                    "reflexive": True,
                    "antisymmetric": True,
                    "transitive": False,
                },
            ),
            # check non-warshall
            (
                (
                    {(1, 1), (1, 2), (2, 2), (2, 3), (3, 3)},
                    {1, 2, 3},
                    False,
                ),
                {
                    "s": {1, 2, 3},
                    "r": {(1, 1), (1, 2), (2, 2), (2, 3), (3, 3)},
                    "poset": False,
                    "reflexive": True,
                    "antisymmetric": True,
                    "transitive": False,
                },
            ),
            # 5e
            (
                (
                    {(1, 1), (1, 2), (2, 2), (3, 3), (4, 1), (4, 2), (4, 4)},
                    {1, 2, 3, 4},
                    True,
                ),
                {
                    "s": {1, 2, 3, 4},
                    "r": {(1, 1), (1, 2), (2, 2), (3, 3), (4, 1), (4, 2), (4, 4)},
                    "poset": True,
                    "reflexive": True,
                    "antisymmetric": True,
                    "transitive": True,
                },
            ),
            # 5f
            (
                (
                    {
                        (0, 0),
                        (0, 1),
                        (0, 2),
                        (0, 3),
                        (1, 0),
                        (1, 1),
                        (1, 2),
                        (1, 3),
                        (2, 0),
                        (2, 2),
                        (3, 3),
                    },
                    {0, 1, 2, 3},
                    True,
                ),
                {
                    "s": {0, 1, 2, 3},
                    "r": {
                        (0, 0),
                        (0, 1),
                        (0, 2),
                        (0, 3),
                        (1, 0),
                        (1, 1),
                        (1, 2),
                        (1, 3),
                        (2, 0),
                        (2, 2),
                        (3, 3),
                    },
                    "poset": False,
                    "reflexive": True,
                    "antisymmetric": False,
                    "transitive": False,
                },
            ),
        ]

    def test_inputs(self) -> None:
        for (input, output) in self.tests:
            self.assertDictEqual(poset(*input), output)
