"""
Author: Cody Duong <cody.qd@gmail.com> (https://github.com/codyduong)
KUID: 3050266
Date: 2022-10-26
Lab: Assignment 5
Purpose: Checks if given sets (A and B) with relation R is a function
"""

from typing import TypeVar, Union, List, Set, Tuple


T = TypeVar("T", str, int)


def function(
    A: Union[Set[T], List[T]],
    B: Union[Set[T], List[T]],
    R: Union[Set[Tuple[T, T]], List[Tuple[T, T]]],
) -> bool:
    """
    Takes in two sets, A and B, a relation R, and determines whether or not R is a function of A and B

    :param A: Set of T
    :param B: Set of T
    :param R: Relation of Set[Tuple[T, T]]
    :returns bool: A relation of a total function
    """

    is_function: bool = True
    A_set: Set[T] = set(A)
    B_set: Set[T] = set(B)
    for a, b in R:
        if a not in A_set:
            is_function = False
            break
        else:
            # we cannot have two of the same A mapped to different B
            A_set = A_set - {a}
        if b not in B_set:
            is_function = False
            break
        else:
            # we can have two different A mapped to the same B
            # B_clone = B_clone - {b}
            pass

    # we must use every element a∈A to constitute a total function
    is_function = is_function if len(A_set) == 0 else False

    return is_function
