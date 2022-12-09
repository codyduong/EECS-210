"""
Author: Cody Duong <cody.qd@gmail.com> (https://github.com/codyduong)
KUID: 3050266
Date: 2022-12-8
Lab: Assignment 8
Purpose: Tests
"""


import unittest
from src.problem1 import solve_euler_circuit, e4g1, e4g2, e4g3
from src.problem2 import has_hamilton_circuit_dirac, e5g1, e5g2, e5g3


class TestSurjective(unittest.TestCase):
    # maxDiff = None

    def __init__(self, *args) -> None:  # type: ignore
        super().__init__(*args)  # type: ignore

    def test_euler_circuits(self) -> None:
        # example 4 G1
        self.assertEqual(
            solve_euler_circuit(e4g1),
            (False, ["b", "d"]),
        )

        # example 4 G2
        self.assertEqual(
            solve_euler_circuit(e4g2),
            (False, ["b", "d"]),
        )

        # example 4 G3
        self.assertEqual(
            solve_euler_circuit(e4g3),
            (False, ["a", "b", "c", "d", "e", "f"]),
        )

    def test_hamiliton(self) -> None:
        # example 5 G1
        self.assertEqual(
            has_hamilton_circuit_dirac(e5g1),
            None,
        )

        # example 5 G2
        self.assertEqual(
            has_hamilton_circuit_dirac(e5g2),
            None,
        )

        # example 5 G3
        self.assertEqual(
            has_hamilton_circuit_dirac(e5g3),
            None,
        )


if __name__ == "__main__":
    unittest.main()
