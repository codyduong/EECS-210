"""
Author: Cody Duong <cody.qd@gmail.com> (https://github.com/codyduong)
KUID: 3050266
Date: 2022-10-13
Lab: Assignment 4
Purpose: Reflexivity
"""

from typing import Any, List, Set, Tuple, TypedDict


class ReflexiveReturn(TypedDict):
    """
    R = {...}
    R is (reflexive | not reflexive)
    R* if is is not reflexive
    """

    r: Set[Tuple[Any, Any]]
    reflexive: bool
    r_star: None | Set[Tuple[Any, Any]]


def reflexive(
    R: List[Tuple[Any, Any]] | Set[Tuple[Any, Any]],
    s: List[Any] | Set[Any] | None = None,
) -> ReflexiveReturn:
    """
    Takes in a set of ordered pairs in the format List[Tuple[Any, Any]] and returns a ReflexiveReturn

    :param R: Relation of List[Tuple[Any, Any]]
    :param A: Set of elements to check for
    :returns ReflexiveReturn:
    """
    if s is None:
        s = set(x for x, _ in R) | set(y for _, y in R)

    a_set: set[Any] = set(s)
    r_set: set[tuple[Any, Any]] = set(
        (x, y) for x, y in R if x in a_set and y in a_set and x == y
    )
    reflexive: bool = len(a_set) == len(r_set)

    r_star: None | Set[Tuple[Any, Any]] = None
    if not reflexive:
        # just generate the reflexive closure directly from A
        r_star = set((a, a) for a in a_set)

    return {
        "r": r_set,
        "reflexive": reflexive,
        "r_star": r_star,
    }
