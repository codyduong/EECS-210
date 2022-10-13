"""
Author: Cody Duong <cody.qd@gmail.com> (https://github.com/codyduong)
KUID: 3050266
Date: 2022-10-13
Lab: Assignment 4
Purpose: Transitive
"""

from itertools import product
from typing import Any, List, Set, Tuple, TypedDict


class TransitiveReturn(TypedDict):
    """
    R = {...}
    R is (symmetric | not symmetric)
    R* if is is not symmetric
    """

    r: None | Set[Tuple[Any, Any]]
    transitive: bool
    r_star: None | Set[Tuple[Any, Any]]


def transitive(
    R: List[Tuple[Any, Any]] | Set[Tuple[Any, Any]], A: List[Any] | Set[Any]
) -> TransitiveReturn:
    a_set: set[Any] = set(A)
    r_set: set[Tuple[Any, Any]] = set((x, y) for x, y in R if x in a_set and y in a_set)

    x_set: set[Any] = set(x for x, _ in r_set)
    y_set: set[Any] = set(y for _, y in r_set)

    transitive_list: list[bool] = []
    r_to_append: List[Tuple[Any, Any]] = []

    # we only need to check values where we can have (a, b) (b, c) -> (a, c)
    # so check for y=b, x=b, ie. intersect y&b
    x_intersect_y: set[Any] = y_set & x_set
    for b in x_intersect_y:
        # get a from b
        a: set[Any] = set(x for x, y in r_set if y == b)
        # get c from b
        c: set[Any] = set(y for x, y in r_set if x == b)

        # i would use itertools.product but the behavior doesn't seem right...
        # {*product(a, c)} !== {(ea, ec) for ea in a for ec in c}
        a_c_permutations = {*product(a, c)}
        this_b_is_transitive = all(v in r_set for v in a_c_permutations)
        transitive_list.append(this_b_is_transitive)
        if not this_b_is_transitive:
            r_to_append.extend([*a_c_permutations])
    # in retrospect this is could just be a warshall algo...

    transitive: bool = all(transitive_list)
    r_star: set[Tuple[Any, Any]] = r_set | set(r_to_append)

    return {
        "r": r_set,
        "transitive": transitive,
        "r_star": None if transitive else r_star,
    }
