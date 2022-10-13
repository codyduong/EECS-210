"""
Author: Cody Duong <cody.qd@gmail.com> (https://github.com/codyduong)
KUID: 3050266
Date: 2022-10-13
Lab: Assignment 4
Purpose: Antisymmetry
"""


from typing import Any, List, Set, Tuple, TypedDict


class AntisymmetricReturn(TypedDict):
    """
    R = {...}
    R is (antisymmetric | not antisymmetric)
    """

    r: Set[Tuple[Any, Any]]
    antisymmetric: bool


def antisymmetric(
    R: List[Tuple[Any, Any]] | Set[Tuple[Any, Any]],
    s: List[Any] | Set[Any] | None = None,
) -> AntisymmetricReturn:
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

    # set of nonequal x,y
    xy_set: set[tuple[Any, Any]] = set((x, y) for x, y in r_set if x != y)
    yx_set: set[tuple[Any, Any]] = set((y, x) for x, y in r_set if x != y)

    # this seems rather intuitive LOL
    antisymmetric = (
        len(xy_set) == len(xy_set - yx_set) == len(yx_set - xy_set) == len(yx_set)
    )

    return {"r": r_set, "antisymmetric": antisymmetric}
