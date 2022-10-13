"""
Author: Cody Duong <cody.qd@gmail.com> (https://github.com/codyduong)
KUID: 3050266
Date: 2022-10-13
Lab: Assignment 4
Purpose: Utility to running the program
"""

from typing import Any, Literal, overload
from src.reflexive import ReflexiveReturn
from src.symmetric import SymmetricReturn
from src.transitive import TransitiveReturn
from src.equivalence import EquivalenceReturn
from src.poset import PosetReturn


@overload
def pretty_print(
    s: ReflexiveReturn, problem_number: str, type: Literal["reflexive"]
) -> None:
    ...


@overload
def pretty_print(
    s: SymmetricReturn, problem_number: str, type: Literal["symmetric"]
) -> None:
    ...


@overload
def pretty_print(
    s: TransitiveReturn, problem_number: str, type: Literal["transitive"]
) -> None:
    ...


@overload
def pretty_print(
    s: EquivalenceReturn, problem_number: str, type: Literal["equivalence"]
) -> None:
    ...


@overload
def pretty_print(s: PosetReturn, problem_number: str, type: Literal["poset"]) -> None:
    ...


def pretty_print(
    s: ReflexiveReturn
    | SymmetricReturn
    | TransitiveReturn
    | EquivalenceReturn
    | PosetReturn,
    problem_number: str,
    type: str,
) -> None:
    """Pretty print the relations"""

    if type in ["equivalence", "poset"]:
        s1: EquivalenceReturn | PosetReturn = s  # type: ignore
        sym_asym: Any = "symmetric" if type == "equivalence" else "antisymmetric"
        # LOL @ pyright
        any_key: Any = "s"
        s_line = "\t S = " + f"{s1[any_key]}" + "\n" if any_key in s1 else ""
        print(
            f"""
Problem {problem_number}
{s_line}\t R = {s1['r']}
\t R is {'a ' + type if s1[type] else 'not a '+type} relation
\t\t R is {'reflexive' if s1['reflexive'] else 'not reflexive'}
\t\t R is {'transitive' if s1['transitive'] else 'not transitive'}
\t\t R is {sym_asym if s1[sym_asym] else 'not '+sym_asym} 
"""
        )
    else:
        s2: ReflexiveReturn | SymmetricReturn | TransitiveReturn = s  # type: ignore
        print(
            f"""
Problem {problem_number}
\t R = {s2['r']}
\t R is {'a ' + type if s2[type] else 'not a '+type} relation
\t R* = {s2['r_star']}
"""
        )
