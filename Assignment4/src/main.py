"""
Author: Cody Duong <cody.qd@gmail.com> (https://github.com/codyduong)
KUID: 3050266
Date: 2022-10-13
Lab: Assignment 4
Purpose: Run all problems
"""


from src.reflexive import ReflexiveReturn, reflexive as rf
from src.symmetric import SymmetricReturn, symmetric as sf
from src.transitive import TransitiveReturn, transitive as tf
from src.equivalence import EquivalenceReturn, equivalence as ef
from src.poset import PosetReturn, poset as pf
from src.util import pretty_print


def problem1() -> None:
    """
    Write code that determines if a relation (R) of ordered pairs is reflexive or not
    & then if it is not, finds the reflexive closure of R (R*). The output should be:
    a) R = {...}
    b) R is or is not reflexive
    c) R* if it is not reflexive
    d) Show the code works for the relation {(1,1), (4,4), (2,2), (3,3)} on the
    set {1,2,3,4}.
    e) Show the code works for the relation {(a,a), (c,c)} on the set {a,b,c,d}.
    """
    # 1d
    p1d: ReflexiveReturn = rf({(1, 1), (4, 4), (2, 2), (3, 3)}, {1, 2, 3, 4})
    pretty_print(p1d, "1d", "reflexive")

    # 1e
    p1e: ReflexiveReturn = rf({("a", "a"), ("c", "c")}, {"a", "b", "c", "d"})
    pretty_print(p1e, "1e", "reflexive")


def problem2() -> None:
    """
    Write code that determines if a relation (R) of ordered pairs is symmetric or
    not & then if it is not, finds the symmetric closure of R (R*). The output
    should be:
    a) R = {...}
    b) R is or is not symmetric
    c) R* if it is not symmetric
    d) Show the code works for the relation {(1,2), (4,4), (2,1), (3,3)} on the
    set {1,2,3,4}.
    e) Show the code works for the relation {(1,2), (3,3)} on the set
    {1,2,3,4}.
    """
    # 2d
    p2d: SymmetricReturn = sf({(1, 2), (4, 4), (2, 1), (3, 3)}, {1, 2, 3, 4})
    pretty_print(p2d, "2d", "symmetric")

    # 2e
    p2e: SymmetricReturn = sf({(1, 2), (3, 3)}, {1, 2, 3, 4})
    pretty_print(p2e, "2d", "symmetric")


def problem3() -> None:
    """
    Write code that determines if a relation (R) of ordered pairs is transitive or not
    & then if it is not, finds the transitive closure of R (R*) using Warshall’s
    Algorithm. The output should be:
    a) R = {...}
    b) R is or is not transitive
    c) R* if it is not transitive
    d) Show the code works for the relation {(a,b), (d,d), (b,c), (a,c)} on the
    set {a,b,c,d}.
    e) Show the code works for the relation {(1,1),(1,3),(2,2),(3,1),(3,2)} on
    the set {1,2,3}.
    """
    # 3d
    p3d: TransitiveReturn = tf(
        {("a", "b"), ("d", "d"), ("b", "c"), ("a", "c")}, {"a", "b", "c", "d"}
    )
    pretty_print(p3d, "3d", "transitive")

    # 3e
    p3e: TransitiveReturn = tf({(1, 1), (1, 3), (2, 2), (3, 1), (3, 2)}, {1, 2, 3})
    pretty_print(p3e, "3d", "transitive")


def problem4() -> None:
    """
    Write code that determines if a relation (R) of ordered pairs is an equivalence
    relation or not and the reason why. The output should be:
    a) R = {...}
    b) R is or is not an equivalence relation
    c) The reasons why, if it is not an equivalence relation (i.e., it is not
    reflexive, and/or it is not symmetric, and/or it is not transitive).
    d) Show the code works for the relation {(1,1),(2,2),(2,3)} on the set
    {1,2,3}.
    e) Show the code works for the relation {(a,a),(b,b),(c,c),(b,c),(c,b)} on
    the set {a,b,c}.
    """
    # 4d
    p4d: EquivalenceReturn = ef({(1, 1), (2, 2), (2, 3)}, {1, 2, 3})
    pretty_print(p4d, "4d", "equivalence")

    # 4e
    p4e: EquivalenceReturn = ef(
        {("a", "a"), ("b", "b"), ("c", "c"), ("b", "c"), ("c", "b")}, {"a", "b", "c"}
    )
    pretty_print(p4e, "4e", "equivalence")


def problem5() -> None:
    """
    Write code that determines if a relation (R) of ordered pairs is a poset of the
    set (S) or not and the reason why. The output should be:
    a) S = {...}
    b) R = {...}
    c) (S,R) is or is not a poset
    d) The reason why, if it is not poset (i.e., it is not reflexive, and/or it is
    not antisymmetric, and/or it is not transitive.
    e) Show the code works for the relation {(1,1), (1,2), (2,2), (3,3), (4,1),
    (4,2), (4,4)} on the set {1, 2, 3, 4}.
    f) Show the code works for the relation {(0, 0), (0, 1), (0, 2), (0, 3), (1,
    0), (1, 1), (1, 2), (1, 3), (2, 0), (2, 2), (3, 3)} on the set {0, 1, 2, 3}.
    """
    p5e: PosetReturn = pf(
        {(1, 1), (1, 2), (2, 2), (3, 3), (4, 1), (4, 2), (4, 4)}, {1, 2, 3, 4}
    )
    pretty_print(p5e, "5e", "poset")

    p5f: PosetReturn = pf(
        {
            (0, 0),
            (0, 1),
            (0, 2),
            (0, 3),
            (1, 0),
            (1, 1),
            (1, 2),
            (1, 3),
            (2, 0),
            (2, 2),
            (3, 3),
        },
        {0, 1, 2, 3},
    )
    pretty_print(p5f, "5f", "poset")


problem1()
problem2()
problem3()
problem4()
problem5()
