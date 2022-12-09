"""
Author: Cody Duong <cody.qd@gmail.com> (https://github.com/codyduong)
KUID: 3050266
Date: 2022-12-8
Lab: Assignment 8
Purpose: Problem 1

  Write a program for finding an Euler circuit, if one exists, using the algorithm
  from the lecture on Euler circuits and paths. If an Euler circuit does not exist,
  print out the vertices with odd degrees (see Theorem 1). If an Euler circuit does
  exist, print it out with the vertices of the circuit in order, separated by dashes, e.g.,
  a-b-c.

"""


from typing import List, Tuple, TypeAlias
from src.sharedTypes import Graph


EulerCircuitReturn: TypeAlias = Tuple[bool, List[str]]


def solve_euler_circuit(
    graph: Graph,
) -> EulerCircuitReturn:
    """
    Takes in an input graph
    :param graph: Graph
    :returns EulerCircuitReturn:
    """
    graph_keys: list[str] = list(graph.keys())

    # A connected multigraph with at least two vertices has an Euler
    # circuit if and only if: each of its vertices has an even degree
    if len(graph_keys) >= 2:
        odd_degreed_vertices: List[str] = []
        for key, value in graph.items():
            # 🤔
            degree: int = len(list(filter(lambda x: x != key, value)))
            degree += value.count(key) * 2
            if degree % 2 != 0:
                odd_degreed_vertices.append(key)

        if len(odd_degreed_vertices) > 0:
            return (False, odd_degreed_vertices)

    # Hierholzer's algorithm
    adjacency_graph: Graph = graph
    current_path: list[str] = [graph_keys[0]]
    circuit: list[str] = []

    while current_path:
        current_vertex: str = current_path[-1]
        other_vertex: List[str] | None = None
        try:
            other_vertex = adjacency_graph[current_vertex]
            # prevent using same edge twice
            other_vertex.remove(current_path[-2])
        except (KeyError, ValueError, IndexError):
            pass
        if other_vertex:
            next_vertex: str = other_vertex.pop()
            current_path.append(next_vertex)
        else:
            circuit.append(current_path.pop())

    return (True, circuit)


def pretty_print_euler(f: EulerCircuitReturn) -> None:
    print(
        "\t"
        + f"Has {'' if f[0] else 'no '}euler ciruit:"
        + "\n\t"
        + ("circuit: " if f[0] else "odd vertices: ")
        + ("-" if f[0] else " ").join(f[1])
        + "\n"
    )


def solve_euler_circuit_pretty(graph: Graph) -> None:
    pretty_print_euler(solve_euler_circuit(graph))


e4g1: Graph = {
    "a": ["b", "d"],
    "b": ["a", "d", "c"],
    "d": ["a", "b", "c"],
    "c": ["b", "d"],
}
e4g2: Graph = {
    "a": ["b", "g"],
    "b": ["a", "g", "c"],
    "g": ["a", "b", "c", "f"],
    "c": ["b", "g", "f", "d"],
    "f": ["g", "c", "d", "e"],
    "d": ["c", "f", "e"],
    "e": ["f", "d"],
}
e4g3: Graph = {
    "g": ["a", "b", "c", "d", "e", "f"],
    "a": ["b", "g", "f"],
    "b": ["a", "g", "c"],
    "c": ["b", "g", "d"],
    "d": ["c", "g", "e"],
    "e": ["d", "g", "f"],
    "f": ["e", "g", "a"],
}


def problem1() -> None:
    print("1a:")
    # example 4 G1
    print("\tG_1")
    solve_euler_circuit_pretty(e4g1)

    # example 4 G2
    print("\tG_2")
    solve_euler_circuit_pretty(e4g2)

    # example 4 G3
    print("\tG_3")
    solve_euler_circuit_pretty(e4g3)

    print("1b:")
    solve_euler_circuit_pretty(
        {
            "a": ["b", "d"],
            "b": ["a", "d", "e", "c"],
            "c": ["b", "f"],
            "d": ["a", "b", "e", "g"],
            "e": ["b", "f", "h", "d"],
            "f": ["c", "e", "h", "i"],
            "g": ["d", "h"],
            "h": ["e", "f", "g", "i"],
            "i": ["f", "h"],
        }
    )
