"""
Author: Cody Duong <cody.qd@gmail.com> (https://github.com/codyduong)
KUID: 3050266
Date: 2022-10-13
Lab: Assignment 4
Purpose: Symmetry Tests
"""


from typing import Any
import unittest
from src.transitive import transitive, TransitiveReturn


class TestTransitiveFunction(unittest.TestCase):
    maxDiff = None

    def __init__(self, *args) -> None:  # type: ignore
        super().__init__(*args)  # type: ignore

        self.tests: list[
            tuple[
                tuple[
                    set[tuple[Any, Any]] | list[tuple[Any, Any]],
                    set[Any] | list[Any],
                    bool,
                ],
                TransitiveReturn,
            ]
        ] = [
            # 3d
            (
                (
                    {("a", "b"), ("d", "d"), ("b", "c"), ("a", "c")},
                    {"a", "b", "c", "d"},
                    True,
                ),
                {
                    "r": {("a", "b"), ("d", "d"), ("b", "c"), ("a", "c")},
                    "transitive": True,
                    "r_star": None,
                },
            ),
            (
                (
                    {("a", "b"), ("d", "d"), ("b", "c"), ("a", "c")},
                    {"a", "b", "c", "d"},
                    False,
                ),
                {
                    "r": {("a", "b"), ("d", "d"), ("b", "c"), ("a", "c")},
                    "transitive": True,
                    "r_star": None,
                },
            ),
            # 3e
            (
                (
                    {(1, 1), (1, 3), (2, 2), (3, 1), (3, 2)},
                    {1, 2, 3},
                    True,
                ),
                {
                    "r": {(1, 1), (1, 3), (2, 2), (3, 1), (3, 2)},
                    "transitive": False,
                    "r_star": {(1, 1), (1, 3), (2, 2), (3, 1), (3, 2), (3, 3), (1, 2)},
                },
            ),
            (
                ({(1, 1), (1, 3), (2, 2), (3, 1), (3, 2)}, {1, 2, 3}, False),
                {
                    "r": {(1, 1), (1, 3), (2, 2), (3, 1), (3, 2)},
                    "transitive": False,
                    "r_star": {(1, 1), (1, 3), (2, 2), (3, 1), (3, 2), (3, 3), (1, 2)},
                },
            ),
            # other
            (
                (
                    {(1, 2), (3, 2), (2, 3)},
                    {1, 2, 3},
                    True,
                ),
                {
                    "r": {(1, 2), (3, 2), (2, 3)},
                    "transitive": False,
                    "r_star": {(1, 2), (3, 2), (2, 3), (1, 3), (2, 2), (3, 3)},
                },
            ),
            (
                ({(1, 2), (3, 2), (2, 3)}, {1, 2, 3}, False),
                {
                    "r": {(1, 2), (3, 2), (2, 3)},
                    "transitive": False,
                    "r_star": {(1, 2), (3, 2), (2, 3), (1, 3), (2, 2), (3, 3)},
                },
            ),
        ]

    def test_inputs(self) -> None:
        for (input, output) in self.tests:
            self.assertDictEqual(transitive(*input), output)
