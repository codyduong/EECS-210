"""
Author: Cody Duong <cody.qd@gmail.com> (https://github.com/codyduong)
KUID: 3050266
Date: 2022-11-29
Lab: Assignment 7
Purpose: tests
"""


import unittest
from main import *


class TestSurjective(unittest.TestCase):
    # maxDiff = None

    def __init__(self, *args) -> None:  # type: ignore
        super().__init__(*args)  # type: ignore

    def test_distinguisable_objects_and_boxes(self) -> None:
        # Example 8: There are 52!/(5!5!5!5!32!) ways to distribute hands of 5 cards each to four players
        self.assertEqual(problem1(52, 4, 5), 1478262843475644020034240)

        # b) A professor packs her collection of 40 issues of a mathematics journal in four boxes with 10 issues per box.
        # How many ways can she distribute the journals if each box is numbered, so that they are distinguishable
        self.assertEqual(problem1(40, 4, 10), 4705360871073570227520)

    def test_indistinguisable_objects_and_distinguisable_boxes(self) -> None:
        # Example 9: 19,448 ways to place 10 indistinguishable objects into 8 distinguishable boxes.
        self.assertEqual(problem2(10, 8), 19448)

        # b) How many ways are there to distribute 12 indistinguishable balls into six distinguishable bins?
        self.assertEqual(problem2(12, 6), 6188)

    def test_distinguisable_objects_and_indistinguisable_boxes(self) -> None:
        # Example 10: There are 14 ways to put four employees into three indistinguishable offices
        self.assertEqual(problem3(4, 3), 14)
        # b) How many ways are there to put five temporary employees into four identical offices?
        self.assertEqual(problem3(5, 4), 51)

        # other tests extrapolated from S(n,k)
        self.assertEqual(problem3(4, 2), 8)
        self.assertEqual(problem3(5, 3), 41)
        self.assertEqual(problem3(5, 2), 16)

    def test_indistinguisable_objects_and_indistinguisable_boxes(self) -> None:
        # Example 11: There are 9 ways to pack six copies of the same book into four identical boxes
        self.assertEqual(problem4(6, 4), 9)
        # b) How many ways are there to distribute five indistinguishable objects into three indistinguishable boxes?
        self.assertEqual(problem4(5, 3), 5)


if __name__ == "__main__":
    unittest.main()
