"""
Author: Cody Duong <cody.qd@gmail.com> (https://github.com/codyduong)
KUID: 3050266
Date: 2022-10-13
Lab: Assignment 4
Purpose: Equivalence
"""

from typing import Any, List, Set, Tuple, TypedDict

from src.reflexive import reflexive as rf
from src.symmetric import symmetric as sf
from src.transitive import transitive as tf


class EquivalenceReturn(TypedDict):
    """
    R = {...}
    R is (symmetric | not symmetric)
    R* if is is not symmetric
    """

    r: Set[Tuple[Any, Any]]
    equivalence: bool
    reflexive: bool
    symmetric: bool
    transitive: bool


def equivalence(
    R: List[Tuple[Any, Any]] | Set[Tuple[Any, Any]],
    s: List[Any] | Set[Any] | None = None,
    use_warshall_closure: bool = True,
) -> EquivalenceReturn:
    """
    Takes in a set of ordered pairs in the format List[Tuple[Any, Any]] and returns a EquivalenceReturn

    :param R: Relation of List[Tuple[Any, Any]]
    :param s: Set of elements to check for
    :param use_warshall_closure: Defaults to True. This algorithim will be used for transitive closures.
        it blow up on reserved values that cannot be put in a dictionary index.
        Will also incorrectly coerce to integer (if possible)... I'm sure I could fix this... w/e...
    :returns EquivalenceReturn:
    """
    r_set: set[Tuple[Any, Any]] = set(R)
    if s is None:
        s = set(x for x in R) | set(y for y in R)

    reflexive: bool = rf(r_set, s)["reflexive"]
    symmetric: bool = sf(r_set, s)["symmetric"]
    transitive: bool = tf(r_set, s, use_warshall_closure)["transitive"]

    return {
        "r": r_set,
        "equivalence": reflexive and symmetric and transitive,
        "reflexive": reflexive,
        "symmetric": symmetric,
        "transitive": transitive,
    }
