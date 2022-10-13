"""
Author: Cody Duong <cody.qd@gmail.com> (https://github.com/codyduong)
KUID: 3050266
Date: 2022-10-13
Lab: Assignment 4
Purpose: Poset
"""

from typing import Any, List, Set, Tuple, TypedDict

from src.reflexive import reflexive as rf
from src.antisymmetric import antisymmetric as asf
from src.transitive import transitive as tf


class PosetReturn(TypedDict):
    """
    R = {...}
    R is (symmetric | not symmetric)
    R* if is is not symmetric
    """

    r: Set[Tuple[Any, Any]]
    s: Set[Any]
    poset: bool
    reflexive: bool
    antisymmetric: bool
    transitive: bool


def poset(
    R: List[Tuple[Any, Any]] | Set[Tuple[Any, Any]],
    s: List[Any] | Set[Any] | None = None,
    use_warshall_closure: bool = True,
) -> PosetReturn:
    """
    Takes in a set of ordered pairs in the format List[Tuple[Any, Any]] and returns a EquivalenceReturn

    :param R: Relation of List[Tuple[Any, Any]]
    :param s: Set of elements to check for
    :param use_warshall_closure: Defaults to True. This algorithim will be used for transitive closures.
        it blow up on reserved values that cannot be put in a dictionary index.
        Will also incorrectly coerce to integer (if possible)... I'm sure I could fix this... w/e...
    :returns PosetReturn:
    """
    r_set: set[Tuple[Any, Any]] = set(R)
    if s is None:
        s = set(x for x in R) | set(y for y in R)
    s = set(s)

    reflexive: bool = rf(r_set, s)["reflexive"]
    antisymmetric: bool = asf(r_set, s)["antisymmetric"]
    transitive: bool = tf(r_set, s, use_warshall_closure)["transitive"]

    return {
        "r": r_set,
        "s": s,
        "poset": reflexive and antisymmetric and transitive,
        "reflexive": reflexive,
        "antisymmetric": antisymmetric,
        "transitive": transitive,
    }
