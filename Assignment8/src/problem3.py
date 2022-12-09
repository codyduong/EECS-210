"""
Author: Cody Duong <cody.qd@gmail.com> (https://github.com/codyduong)
KUID: 3050266
Date: 2022-12-8
Lab: Assignment 8
Purpose: Problem 3

  Write a program that uses Ore’s theorem to determine if a graph has a Hamilton 
  circuit. You do not have to find the circuit.

"""


from typing import Dict, List, Literal, Tuple, TypeAlias
from src.sharedTypes import Graph
from src.data import *


GraphDegreesItem: TypeAlias = Tuple[str, Tuple[int, List[str]]]
GraphDegreesItems: TypeAlias = List[Tuple[str, Tuple[int, List[str]]]]


def has_hamilton_circuit_ore(graph: Graph) -> Literal[True, None]:
    """
    Ore’s Theorem: If G is a simple graph with n ≥ 3 vertices such that deg(u) + deg(v) ≥ n
    for every pair of nonadjacent vertices, then G has a Hamilton circuit.

    returns True | None: Can only prove hamiliton circuit, not disprove
    """
    n: int = len(list(graph.keys()))
    graph_degrees: Dict[str, Tuple[int, List[str]]] = {}
    if n >= 3:
        for key, value in graph.items():
            degree: int = len(list(filter(lambda x: x != key, value)))
            degree += value.count(key) * 2
            graph_degrees[key] = (degree, value)
        for current_key, data in graph_degrees.items():
            current_degree: int = data[0]
            non_adjacent_vertices: GraphDegreesItems = list(
                filter(
                    lambda x: current_key not in x[1][1] and current_key != x[0],
                    graph_degrees.items(),
                )
            )

            # print(current_key, current_degree, "\n", non_adjacent_vertices)
            for _, other_data in non_adjacent_vertices:
                other_degree: int = other_data[0]
                if not ((current_degree + other_degree) >= n):
                    return None
        return True

    return None


def ore_pretty(label: str, graph: Graph) -> None:
    print(
        f"\t{label}Has Hamilton Circuit {'True' if has_hamilton_circuit_ore(graph) else 'Maybe'}"
    )


def problem3() -> None:
    print("3a:")
    ore_pretty("G_1: ", e5g1)
    ore_pretty("G_2: ", e5g2)
    ore_pretty("G_3: ", e5g3)
    print("3b:")
    ore_pretty(
        "",
        problem2and3graph,
    )
    print("")
