"""
Author: Cody Duong <cody.qd@gmail.com> (https://github.com/codyduong)
KUID: 3050266
Date: 2022-12-8
Lab: Assignment 8
Purpose: Problem 4

  Write a program that creates a min-max strategy for the game of Nim. Display the 
  strategy in a manner that will be clear to the grader and includes all of the 
  elements shown in the “Minmax Strategy for Nim (11.2.5)” slide in the 
  “Application of Trees” lecture.

"""

from distutils.util import strtobool
from typing import List, Literal, Self, Tuple, TypeAlias

GameState: TypeAlias = Tuple[int, int, int] | Tuple[int, int] | Tuple[int]


class NimNode:
    def __init__(self, value: GameState, depth: int) -> None:
        self._value: GameState = value
        self._derivative: List[List[Self] | None] = [None] * 3
        self._depth = depth

    @property
    def value(self) -> GameState:
        return self._value

    @property
    def derivative(self) -> List[List[Self] | None]:
        return self._derivative

    def __setitem__(self, indice: int, value: List[Self]) -> None:
        self._derivative[indice] = value

    def __getitem__(self, indice: int) -> List[Self] | None:
        return self._derivative[indice]

    def __repr__(self) -> str:
        return (
            f"{self._value}"
            + "\n"
            + f"{'': <{self._depth*2}}"
            + "".join(["".join([f"{e}" for e in d]) for d in self._derivative if d])
        )


class Nim:
    def __init__(self, initial_state: Tuple[int, int, int]) -> None:
        self._initial_state: Tuple[int, int, int] = initial_state
        self._game_tree: NimNode = NimNode(initial_state, 1)
        self._player1_points = 0
        self._player2_points = 0

    def _recursive_calculate_game_tree(
        self, node: NimNode, depth: int = 0
    ) -> NimNode | None:
        game_state: GameState = node.value
        if len(game_state) == 1 and game_state[0] == 1:
            return node

        # each stone can't generate a unique combo, filter out reused stones
        used_stone: list[int] = []
        for stone_index, stone in enumerate(game_state):
            if stone in used_stone:
                continue
            used_stone.append(stone)

            this_stones_valid_moves: List[NimNode | None] = []
            for i in range(1, stone + 1):
                new_game_state: list[int] = list(game_state)
                new_game_state[stone_index] -= i
                new_game_state = [s for s in new_game_state if s >= 1]
                new_game_state.sort(reverse=True)
                if len(new_game_state) > 0:
                    # print(game_state, new_game_state)
                    this_stones_valid_moves.append(
                        self._recursive_calculate_game_tree(
                            NimNode(tuple(new_game_state), depth + 2), depth + 1
                        )
                    )
                    # this_stones_valid_moves.append(NimNode(tuple(new_game_state)))
            # this_stones_valid_moves = list(filter(lambda e: e, this_stones_valid_moves))
            # print(this_stones_valid_moves)
            node[stone_index] = this_stones_valid_moves  # type: ignore

        # print(node.derivative)
        return node

    def calculate_game_tree(self) -> None:
        self._recursive_calculate_game_tree(self._game_tree)

    def _calculate_min_max_recursive(self, node: NimNode, depth: int) -> int:
        if len(node.value) == 1 and node.value[0] == 1:
            return -1 if depth % 2 == 0 else 1
        else:
            for i in node.derivative:
                if i:
                    recursed: list[int] = [
                        self._calculate_min_max_recursive(j, depth + 1) for j in i
                    ]
                    return max(recursed) if depth % 2 == 0 else max(recursed)

        raise RuntimeError

    def calculate_min_max(self) -> int:
        return self._calculate_min_max_recursive(self._game_tree, 0)

    def winner(self) -> str:
        return f"Player {1 if self.calculate_min_max() == 1 else 2} wins"

    @property
    def game_tree(self) -> NimNode:
        return self._game_tree


def problem4() -> None:
    print("4a:")
    game0: Nim = Nim((2, 2, 1))
    game0.calculate_game_tree()
    print(game0.game_tree)

    display4b: Literal[0, 1] = 0
    input_str: str = ""
    try:
        input_str = input(
            "Display problem 4b game trees? Console output is verbose (N/y): "
        )
        display4b = strtobool(input_str)
    except ValueError:
        if input_str != "":
            print("Error parsing input, ignoring...")

    game1: Nim = Nim((1, 1, 1))
    game2: Nim = Nim((2, 2, 2))
    game3: Nim = Nim((3, 3, 3))

    game1.calculate_game_tree()
    game2.calculate_game_tree()
    game3.calculate_game_tree()
    if display4b:
        print("4b: Game 1")
        print(game1.game_tree)

        print("4b: Game 2")
        print(game2.game_tree)

        print("4c: Game 3")
        print(game3.game_tree)

    print("4c:")
    print(f"Game 0 winner: {game0.winner()}")
    print(f"Game 1 winner: {game1.winner()}")
    print(f"Game 2 winner: {game2.winner()}")
    print(f"Game 3 winner: {game3.winner()}")
