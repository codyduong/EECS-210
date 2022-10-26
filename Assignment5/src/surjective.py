"""
Author: Cody Duong <cody.qd@gmail.com> (https://github.com/codyduong)
KUID: 3050266
Date: 2022-10-26
Lab: Assignment 5
Purpose: Checks if given range (B) with relation R is surjective
"""

from typing import TypeVar, Union, List, Set, Tuple
from src.function import function


T = TypeVar("T", str, int)


def surjective(
    B: Union[Set[T], List[T]],
    R: Union[Set[Tuple[T, T]], List[Tuple[T, T]]],
) -> bool:
    """
    Takes in a relation and determines if it is surjective. The domain is implicitly bound by the relation set.
    The range is required to determine surjectiveness.

    Implicit domain means partial functions from relation R is acceptable input

    :param B: Set of T
    :param R: Relation of Set[Tuple[T, T]]
    :returns bool:
    """
    A_set: Set[T] = {a for a, _ in R}
    B_set: Set[T] = set(B)
    if not function(A_set, B_set, R):
        # Raise a ValueError instead of returning false, since R as a function should be explicitly checked before calling this function
        raise ValueError("Assumed R would be a function, it is not")

    # we need at least the same number of 'a' elements to use every 'b' element
    surjective: bool = len(A_set) >= len(B_set)
    if not surjective:
        return surjective

    for _, b in R:
        B_set = B_set - {b}
        if len(B_set) == 0:
            return True

    # we should've mapped to every entry in the range B, so the remaining length should be 0
    surjective = len(B_set) == 0

    return surjective
