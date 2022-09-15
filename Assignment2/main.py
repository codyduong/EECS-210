"""
Author: Cody Duong <cody.qd@gmail.com> (https://github.com/codyduong)
KUID: 3050266
Date: 2022-09-15
Lab: Assignment 2
Purpose: Evaluates logical expressions
"""

import os
import sys
from typing import Callable, Tuple


def disable_stdout() -> None:
    """
    A refactor seems a bit verbose for such a small file... w/e
    use this lazy technique
    """
    sys.stdout = open(os.devnull, "w")


def enable_stdout() -> None:
    sys.stdout = sys.__stdout__


def check_all_truthy(
    title: str, fn: Callable[[int], bool], d: Tuple[int, ...] = range(11)
) -> bool:
    """
    Prints the resulting truth value

    :param fn: Function to test all element of d
    :param d: Domain
    :return: Truthy value
    """
    universal = all(fn(e) for e in d)
    print(f"{title}: {universal}")
    return universal


def check_any_truthy(
    title: str, fn: Callable[[int], bool], d: Tuple[int, ...] = range(11)
) -> bool:
    """
    Prints the resulting truth value

    :param fn: Function to test any element of d
    :param d: Domain
    :return: Truthy value
    """
    existential = any(fn(e) for e in d)
    print(f"{title}: {existential}")
    return existential


def problem_one() -> None:
    """
    1. Prove (true) or disprove (false) the following assertions for the domain of
    {0,1,2,3,4,5,6,7,8,9,10}. For the universal quantifier, show at least one of the
    numbers in the domain that disproves the assertion. For the existential
    quantifier, show at least one number in the domain that proves the assertion:
    """
    # a. ∃x P(x), where P(x) is the statement “x<2”
    check_any_truthy("1a", lambda x: x < 2)
    # b. ∀x P(x), where P(x) is the statement “x<2”
    check_all_truthy("1b", lambda x: x < 2)
    # c. ∃x (P(x) ∨ Q(x)) where P(x) is the statement “x<2” and where Q(x) is the statement “x>7”
    check_any_truthy("1c", lambda x: x < 2 or x > 7)
    # d. ∀x (P(x) ∨ Q(x)) where P(x) is the statement “x<2” and where Q(x) is the statement “x>7”
    check_all_truthy("1d", lambda x: x < 2 or x > 7)

    disable_stdout()

    # e. Prove De Morgan’s Law for the Existential Quantifier where P(x) is the statement “x<5”
    existential_quantifier_negated = not check_any_truthy("", lambda x: x < 5)
    existential_quantifier_universal_equivalent = check_all_truthy(
        "", lambda x: not x < 5
    )

    # f. Prove De Morgan’s Law for the Universal Quantifier where P(x) is the statement “x<5”
    universal_quantifier_negated = not check_all_truthy("", lambda x: x < 5)
    universal_quantifier_existential_equivalent = check_any_truthy(
        "", lambda x: not x < 5
    )

    enable_stdout()

    print(
        f"1e: ¬∃x P(x) <=> ∀x ¬P(x): {existential_quantifier_negated == existential_quantifier_universal_equivalent}"
    )
    print(
        f"1f: ¬∀x P(x) <=> ∃x ¬P(x): {universal_quantifier_negated == universal_quantifier_existential_equivalent}"
    )


def problem_two() -> None:
    """
    Find the following truth values for the domain of {0,1,2,3,4,5,6,7,8,9,10}
    where P(x,y): x ∙ y = 0. Show the values in the domain that either make the
    assertions true or false.
    """

    disable_stdout()
    # a. ∀x∀yP(x,y)
    two_a = check_all_truthy("", lambda x: check_all_truthy("", lambda y: x * y == 0))

    # b. ∀x∃yP(x,y)
    two_b = check_all_truthy("", lambda x: check_any_truthy("", lambda y: x * y == 0))

    # c. ∃x∀yP(x,y)
    two_c = check_any_truthy("", lambda x: check_all_truthy("", lambda y: x * y == 0))

    # d. ∃x∃yP(x,y)
    two_d = check_any_truthy("", lambda x: check_any_truthy("", lambda y: x * y == 0))

    enable_stdout()

    print(f"2a: {two_a}")
    print(f"2a: {two_b}")
    print(f"2a: {two_c}")
    print(f"2a: {two_d}")


if __name__ == "__main__":
    problem_one()
    problem_two()
