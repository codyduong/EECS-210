"""
Author: Cody Duong <cody.qd@gmail.com> (https://github.com/codyduong)
KUID: 3050266
Date: 2022-12-8
Lab: Assignment 8
Purpose: Problem 2

  Write a program that uses Dirac’s theorem to determine if a graph has a Hamilton 
  circuit. You do not have to find the circuit. 

"""


from typing import Literal
from src.sharedTypes import Graph
from src.data import *


def has_hamilton_circuit_dirac(graph: Graph) -> Literal[True, None]:
    """
    Dirac’s Theorem: If G is a simple graph with n ≥ 3 vertices such that the
    degree of every vertex in G is ≥ n/2, then G has a Hamilton circuit.

    returns True | None: Can only prove hamiliton circuit, not disprove
    """
    n: int = len(list(graph.keys()))
    if n >= 3:
        for key, value in graph.items():
            degree: int = len(list(filter(lambda x: x != key, value)))
            degree += value.count(key) * 2
            if not degree >= (n / 2):
                return None
        return True

    return None


def dirac_pretty(label: str, graph: Graph) -> None:
    print(
        f"\t{label}Has Hamilton Circuit {'True' if has_hamilton_circuit_dirac(graph) else 'Maybe'}"
    )


def problem2() -> None:
    print("2a:")
    dirac_pretty("G_1: ", e5g1)
    dirac_pretty("G_2: ", e5g2)
    dirac_pretty("G_3: ", e5g3)
    print("2b:")
    dirac_pretty(
        "",
        problem2and3graph,
    )
    print("")
