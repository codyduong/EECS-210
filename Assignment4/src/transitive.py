"""
Author: Cody Duong <cody.qd@gmail.com> (https://github.com/codyduong)
KUID: 3050266
Date: 2022-10-13
Lab: Assignment 4
Purpose: Transitive
"""

from itertools import product
from typing import Any, Dict, List, Set, Tuple, TypedDict


class TransitiveReturn(TypedDict):
    """
    R = {...}
    R is (symmetric | not transitive)
    R* if is is not transitive
    """

    r: Set[Tuple[Any, Any]]
    transitive: bool
    r_star: None | Set[Tuple[Any, Any]]


def transitive(
    R: List[Tuple[Any, Any]] | Set[Tuple[Any, Any]],
    s: List[Any] | Set[Any] | None = None,
    use_warshall_closure: bool = True,
) -> TransitiveReturn:
    """
    Takes in a set of ordered pairs in the format List[Tuple[Any, Any]] and returns a TransitiveReturn

    :param R: Relation of List[Tuple[Any, Any]]
    :param s: Set of elements to check for
    :param use_warshall_closure: Defaults to True. This algorithim will
        blow up on reserved values that cannot be put in a dictionary index.
        Will also incorrectly coerce to integer (if possible)... I'm sure I could fix this... w/e...
    :returns SymmetricReturn:
    """
    if s is None:
        s = set(x for x in R) | set(y for y in R)

    a_set: set[Any] = set(s)
    r_set: set[Tuple[Any, Any]] = set((x, y) for x, y in R if x in a_set and y in a_set)

    if use_warshall_closure:
        """
        post-script: didn't see the req for warshall algo. so here it is...

        it is also extraordinarily unergo for pyright... w/e

        * matrixes have stupid restrictions for a dynamic duck language
        * dictionaries have stupid restrictions for a dynamic duck language

        so this is really ugly...
        """
        # use a dict so we can index with strings... a psuedo-matrix...
        closured_set: Dict[str, bool] = {}

        for (x, y) in r_set:
            closured_set[f"{x},{y}"] = True
        for k in a_set:
            for i in a_set:
                try:
                    closured_set[f"{i},{k}"]
                except KeyError:
                    closured_set[f"{i},{k}"] = False
                for j in a_set:
                    try:
                        closured_set[f"{i},{j}"]
                    except KeyError:
                        closured_set[f"{i},{j}"] = False
                    try:
                        closured_set[f"{k},{j}"]
                    except KeyError:
                        closured_set[f"{k},{j}"] = False

                    closured_set[f"{i},{j}"] = closured_set[f"{i},{j}"] or (
                        closured_set[f"{i},{k}"] and closured_set[f"{k},{j}"]
                    )

        # this is extra unergo if we actually use a set of f"{int}"
        # in which case our entry set will vary from our output set
        # >:(
        def convert_to_int(s: str) -> int | str:
            try:
                return int(s)
            except ValueError:
                return s

        r_star = set(
            tuple(convert_to_int(s) for s in e.split(","))
            for e, value in closured_set.items()
            if value
        )
        transitive = r_set == r_star

        return {
            "r": r_set,
            "transitive": transitive,
            "r_star": None if transitive else r_star,
        }
    else:
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
            a_c_permutations: set[tuple[Any, Any]] = {*product(a, c)}
            this_b_is_transitive: bool = all(v in r_set for v in a_c_permutations)
            transitive_list.append(this_b_is_transitive)
            if not this_b_is_transitive:
                r_to_append.extend([*a_c_permutations])

        transitive: bool = all(transitive_list)
        r_star: set[Tuple[Any, Any]] = r_set | set(r_to_append)

        return {
            "r": r_set,
            "transitive": transitive,
            "r_star": None if transitive else r_star,
        }
