"""
Author: Cody Duong <cody.qd@gmail.com> (https://github.com/codyduong)
KUID: 3050266
Date: 2022-10-13
Lab: Assignment 4
Purpose: Symmetry Tests
"""


from typing import Any
import unittest
from src.symmetric import symmetric, SymmetricReturn


class TestSymmetricFunction(unittest.TestCase):
    # maxDiff = None

    def __init__(self, *args) -> None:  # type: ignore
        super().__init__(*args)  # type: ignore

        max = 1000000
        large_set: list[int] = [*range(max + 1)]
        large_relation_symmetric: set[tuple[int, int]] = {
            (x, max - x) for x in large_set
        }
        large_relation_symmetric_almost: set[
            tuple[int, int]
        ] = large_relation_symmetric | {(250000, 500000)}
        large_relation_symmetric_2: set[
            tuple[int, int]
        ] = large_relation_symmetric_almost | {(500000, 250000)}

        self.tests: list[
            tuple[
                tuple[
                    set[tuple[Any, Any]] | list[tuple[Any, Any]], set[Any] | list[Any]
                ],
                SymmetricReturn,
            ]
        ] = [
            # 2d
            (
                ({(1, 2), (4, 4), (2, 1), (3, 3)}, {1, 2, 3, 4}),
                {
                    "r": {(1, 2), (2, 1), (3, 3), (4, 4)},
                    "symmetric": True,
                    "r_star": None,
                },
            ),
            # 2e
            (
                ({(1, 2), (3, 3)}, {1, 2, 3, 4}),
                {
                    "r": {(1, 2), (3, 3)},
                    "symmetric": False,
                    "r_star": {(1, 2), (2, 1), (3, 3)},
                },
            ),
            (
                ({(1, 2)}, {1, 2, 3}),
                {
                    "r": {(1, 2)},
                    "symmetric": False,
                    "r_star": {(1, 2), (2, 1)},
                },
            ),
            (
                ({(1, 2), (2, 1)}, {1, 2, 3}),
                {"r": {(1, 2), (2, 1)}, "symmetric": True, "r_star": None},
            ),
            (
                ({(1, 2)}, {1, 2, 3}),
                {
                    "r": {(1, 2)},
                    "symmetric": False,
                    "r_star": {(1, 2), (2, 1)},
                },
            ),
            (
                (large_relation_symmetric, large_set),
                {
                    "r": large_relation_symmetric,
                    "symmetric": True,
                    "r_star": None,
                },
            ),
            (
                (large_relation_symmetric_almost, large_set),
                {
                    "r": large_relation_symmetric_almost,
                    "symmetric": False,
                    "r_star": large_relation_symmetric_2,
                },
            ),
            (
                (large_relation_symmetric_2, large_set),
                {
                    "r": large_relation_symmetric_2,
                    "symmetric": True,
                    "r_star": None,
                },
            ),
            (
                (large_relation_symmetric_2, {250000, 500000}),
                {
                    "r": {(250000, 500000), (500000, 250000), (500000, 500000)},
                    "symmetric": True,
                    "r_star": None,
                },
            ),
        ]

    def test_inputs(self) -> None:
        for (input, output) in self.tests:
            self.assertDictEqual(symmetric(*input), output)
