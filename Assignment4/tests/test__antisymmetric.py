"""
Author: Cody Duong <cody.qd@gmail.com> (https://github.com/codyduong)
KUID: 3050266
Date: 2022-10-13
Lab: Assignment 4
Purpose: Antisymmetry Tests
"""


from typing import Any
import unittest
from src.antisymmetric import antisymmetric, AntisymmetricReturn


class TestAntisymmetricFunction(unittest.TestCase):
    # maxDiff = None

    def __init__(self, *args) -> None:  # type: ignore
        super().__init__(*args)  # type: ignore

        self.tests: list[
            tuple[
                tuple[
                    set[tuple[Any, Any]] | list[tuple[Any, Any]],
                    set[Any] | list[Any],
                ],
                AntisymmetricReturn,
            ]
        ] = [
            # from the slides on poset
            (
                (
                    {(1, 1), (1, 2), (2, 2), (3, 3), (4, 1), (4, 2), (4, 4)},
                    {1, 2, 3, 4},
                ),
                {
                    "r": {(1, 1), (1, 2), (2, 2), (3, 3), (4, 1), (4, 2), (4, 4)},
                    "antisymmetric": True,
                },
            ),
            # modified version of above to be not antisymmetric
            (
                (
                    {(1, 1), (1, 2), (2, 2), (3, 3), (4, 1), (4, 2), (4, 4), (1, 4)},
                    {1, 2, 3, 4},
                ),
                {
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
                    "antisymmetric": False,
                },
            ),
        ]

    def test_inputs(self) -> None:
        for (input, output) in self.tests:
            self.assertDictEqual(antisymmetric(*input), output)
