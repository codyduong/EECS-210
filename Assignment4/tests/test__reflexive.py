"""
Author: Cody Duong <cody.qd@gmail.com> (https://github.com/codyduong)
KUID: 3050266
Date: 2022-10-13
Lab: Assignment 4
Purpose: Reflexivity Tests
"""


from typing import Any
import unittest
from src.reflexive import reflexive, ReflexiveReturn


class TestReflexiveFunction(unittest.TestCase):
    # maxDiff = None

    def __init__(self, *args) -> None:  # type: ignore
        super().__init__(*args)  # type: ignore

        # this should be fast if done correctly
        large_list: list[int] = [*range(1000000)]
        large_relation: set[tuple[int, int]] = {(x, x) for x in large_list}
        large_relation_almost: set[tuple[int, int]] = {(x, x) for x in large_list[:-1]}

        self.tests: list[
            tuple[
                tuple[
                    set[tuple[Any, Any]] | list[tuple[Any, Any]], set[Any] | list[Any]
                ],
                ReflexiveReturn,
            ]
        ] = [
            # 1d
            (
                ({(1, 1), (4, 4), (2, 2), (3, 3)}, {1, 2, 3, 4}),
                {
                    "r": {(1, 1), (4, 4), (2, 2), (3, 3)},
                    "reflexive": True,
                    "r_star": None,
                },
            ),
            # 1e
            (
                ({("a", "a"), ("c", "c")}, {"a", "b", "c", "d"}),
                {
                    "r": {("a", "a"), ("c", "c")},
                    "reflexive": False,
                    "r_star": {("a", "a"), ("b", "b"), ("c", "c"), ("d", "d")},
                },
            ),
            (
                ({(1, 1), (2, 2), (3, 3)}, {1, 2, 3}),
                {"r": {(1, 1), (2, 2), (3, 3)}, "reflexive": True, "r_star": None},
            ),
            (
                ({(1, 1), (3, 3)}, {1, 2, 3}),
                {
                    "r": {(1, 1), (3, 3)},
                    "reflexive": False,
                    "r_star": {(1, 1), (2, 2), (3, 3)},
                },
            ),
            (
                (large_relation, large_list),
                {"r": large_relation, "reflexive": True, "r_star": None},
            ),
            (
                (large_relation_almost, large_list),
                {
                    "r": large_relation_almost,
                    "reflexive": False,
                    "r_star": large_relation,
                },
            ),
            (
                (large_relation, {1}),
                {
                    "r": {(1, 1)},
                    "reflexive": True,
                    "r_star": None,
                },
            ),
        ]

    def test_inputs(self) -> None:
        for (input, output) in self.tests:
            self.assertDictEqual(reflexive(*input), output)
