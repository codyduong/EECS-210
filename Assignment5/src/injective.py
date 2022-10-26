"""
Author: Cody Duong <cody.qd@gmail.com> (https://github.com/codyduong)
KUID: 3050266
Date: 2022-10-26
Lab: Assignment 5
Purpose: Checks if relation R is injective
"""

from typing import TypeVar, Union, List, Set, Tuple
from src.function import function


T = TypeVar("T", str, int)


def injective(
    R: Union[Set[Tuple[T, T]], List[Tuple[T, T]]],
) -> bool:
    """
    Takes in a relation and determines if it is injective. It is implicitly bound by all elements included in the relation set.

    Implicit domain means partial functions from relation R is acceptable input

    :param R: Relation of Set[Tuple[T, T]]
    :returns bool:
    """
    A_set: Set[T] = {a for a, _ in R}
    B_set: Set[T] = {b for _, b in R}
    if not function(A_set, B_set, R):
        # Raise a ValueError instead of returning false, since R as a function should be explicitly checked before calling this function
        raise ValueError("Assumed R would be a function, it is not")

    injective: bool = True

    for _, b in R:
        if b not in B_set:
            injective = False
            break
        else:
            # we cannot have two different A mapped to the same B
            B_set = B_set - {b}
            pass

    return injective
