"""
Author: Cody Duong <cody.qd@gmail.com> (https://github.com/codyduong)
KUID: 3050266
Date: 2022-11-29
Lab: Assignment 7
Purpose: Assignment 7
"""
from math import comb as binomial, factorial, ceil
from functools import reduce
from typing import Generator


def problem1(objects: int, boxes: int, objects_per_box: int) -> int:
    """
    ie. distinguisable objects into distinguisable boxes
    """

    if objects_per_box * boxes > objects:
        raise ValueError(
            f"objects_per_box exceeded maximum value of {objects // boxes}"
        )
        # The formula/code below only works if all boxes are filled to the same amount. No empty or partially empty boxes
        # Of course there are circumstances where we might want to calculate such a thing, but thats a TODO implementation.

    """
    k = boxes
    Π binomial(objects_remaining, objects_per_box)
    i=1
    """
    product: int = reduce(
        lambda x, i: x
        * binomial(objects - ((i - 1) * objects_per_box), objects_per_box),
        list(range(1, boxes + 1)),
        1,
    )
    return product


def problem2(objects: int, boxes: int) -> int:
    """
    ie. indistinguishable objects and distinguisable boxes
    """
    return binomial(boxes + objects - 1, objects)


def problem3(objects: int, boxes: int) -> int:
    """
    ie. distinguisable objects into indistinguishable boxes.
    """

    """
    Stirling numbers of the second kind
    k = boxes     k        j-1
    Σ S(n, j)   = Σ 1/j! * Σ(-1) (-1)^i * binomial(j, i) * (j-i)^n
    j = 1         j = 1    i = 0
    """
    # Lambda functions are so damn unreadable in python -> https://stackoverflow.com/questions/1233448/no-multiline-lambda-in-python-why-not
    sum: int = reduce(
        lambda x, j: x
        + round(
            1
            / factorial(j)
            * reduce(
                lambda y, i: y + ((-1) ** i * binomial(j, i) * (j - i) ** objects),
                list(range(0, j)),
                0,
            )
        ),
        list(range(1, boxes + 1)),
        0,
    )

    return sum


def problem4(objects: int, boxes: int) -> int:
    """
    ie. indistinguishable objects into indistinguisable boxes.
    """

    """
    The number of ways of distributing n indistinguishable objects into k 
    indistinguishable boxes equals pk(n), where pk(n) is the number of 
    partitions of n into at most k positive integers.
    """

    """https://stackoverflow.com/a/44209393/17954209"""

    def partitions(n: int, I: int = 1) -> Generator[list[int], None, None]:
        yield [
            n,
        ]
        for i in range(I, n // 2 + 1):
            for p in partitions(n - i, i):
                yield [
                    i,
                ] + p

    return len([x for x in list(partitions(objects)) if len(x) <= boxes])


if __name__ == "__main__":
    # Example 8: There are 52!/(5!5!5!5!32!) ways to distribute hands of 5 cards each to four players
    print(f"1a: {problem1(52, 4, 5)}")
    # b) A professor packs her collection of 40 issues of a mathematics journal in four boxes with 10 issues per box.
    # How many ways can she distribute the journals if each box is numbered, so that they are distinguishable
    print(f"1b: {problem1(40, 4, 10)}")

    # Example 9: 19,448 ways to place 10 indistinguishable objects into 8 distinguishable boxes.
    print(f"2a: {problem2(10, 8)}")
    # b) How many ways are there to distribute 12 indistinguishable balls into six distinguishable bins?
    print(f"2b: {problem2(12, 6)}")

    # Example 10: There are 14 ways to put four employees into three indistinguishable offices
    print(f"3a: {problem3(4, 3)}")
    # b) How many ways are there to put five temporary employees into four identical offices?
    print(f"3b: {problem3(5, 4)}")

    # Example 11: There are 9 ways to pack six copies of the same book into four identical boxes
    print(f"4a: {problem4(6, 4)}")
    # b) How many ways are there to distribute five indistinguishable objects into three indistinguishable boxes?
    print(f"4b: {problem4(5, 3)}")
