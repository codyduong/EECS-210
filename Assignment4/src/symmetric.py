"""
Author: Cody Duong <cody.qd@gmail.com> (https://github.com/codyduong)
KUID: 3050266
Date: 2022-10-13
Lab: Assignment 4
Purpose: Symmetry
"""


from typing import Any, List, Set, Tuple, TypedDict


class SymmetricReturn(TypedDict):
    """
    R = {...}
    R is (symmetric | not symmetric)
    R* if is is not symmetric
    """

    r: Set[Tuple[Any, Any]]
    symmetric: bool
    r_star: None | Set[Tuple[Any, Any]]


def symmetric(
    R: List[Tuple[Any, Any]] | Set[Tuple[Any, Any]],
    s: List[Any] | Set[Any] | None = None,
) -> SymmetricReturn:
    """
    Takes in a set of ordered pairs in the format List[Tuple[Any, Any]] and returns a SymmetricReturn

    :param R: Relation of List[Tuple[Any, Any]]
    :param s: Set of elements to check for
    :returns SymmetricReturn:
    """
    if s is None:
        s = set(x for x in R) | set(y for y in R)

    a_set: set[Any] = set(s)
    r_set: set[Tuple[Any, Any]] = set((x, y) for x, y in R if x in a_set and y in a_set)

    xy_set: set[tuple[Any, Any]] = r_set
    yx_set: set[tuple[Any, Any]] = set((y, x) for x, y in r_set)

    # set symmetric difference the two sets, it should be {} if it is symmetric
    subbed_set: set[tuple[Any, Any]] = xy_set ^ yx_set
    symmetric: bool = len(subbed_set) == 0
    r_star: None | Set[Tuple[Any, Any]] = None
    if not symmetric:
        # reverse the remaining sets in the differenced_set and union them all
        r_star = subbed_set | set((y, x) for x, y in subbed_set) | r_set
    return {"r": r_set, "symmetric": symmetric, "r_star": r_star}
