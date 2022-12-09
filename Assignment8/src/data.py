"""
Author: Cody Duong <cody.qd@gmail.com> (https://github.com/codyduong)
KUID: 3050266
Date: 2022-12-8
Lab: Assignment 8
Purpose: Shared Data
"""

from src.sharedTypes import Graph

e5g1: Graph = {
    "a": ["b", "c", "e"],
    "b": ["a", "e", "c"],
    "e": ["a", "b", "c", "d"],
    "c": ["a", "b", "e", "d"],
    "d": ["e", "c"],
}
e5g2: Graph = {"a": ["b"], "b": ["a", "d", "c"], "c": ["b", "d"], "d": ["b", "c"]}
e5g3: Graph = {
    "a": ["b"],
    "b": ["a", "g", "c"],
    "g": ["b", "e"],
    "d": ["c"],
    "c": ["d", "b", "e"],
    "e": ["c", "g", "f"],
}
problem2and3graph: Graph = {
    "a": ["c", "b"],
    "b": ["a", "c"],
    "c": ["a", "b", "f"],
    "f": ["c", "d", "e"],
    "d": ["f", "e"],
    "e": ["f", "d"],
}
