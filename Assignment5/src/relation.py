"""
Author: Cody Duong <cody.qd@gmail.com> (https://github.com/codyduong)
KUID: 3050266
Date: 2022-10-26
Lab: Assignment 5
Purpose: Relation class and function analyzer
"""

from typing import Generic, List, Set, Tuple, TypeVar, Union
from src.function import function
from src.injective import injective
from src.surjective import surjective

T = TypeVar("T", str, int)


class Relation(Generic[T]):
    """
    A relation instance can check on the specified domain/range if a relation is:
     * a total function
     * injective
     * surjective
     * bijective
     * inverse (if bijective)
    """

    def __init__(
        self,
        A: Union[Set[T], List[T]],
        B: Union[Set[T], List[T]],
        R: Union[Set[Tuple[T, T]], List[Tuple[T, T]]],
    ) -> None:
        self._A: Set[T] = set(A)
        self._B: Set[T] = set(B)
        self._R: Set[Tuple[T, T]] = {(a, b) for a, b in R}
        self.function: bool = function(self._A, self._B, self._R)
        self.injective: Union[bool, None] = (
            injective(self._R) if self.function else None
        )
        self.surjective: Union[bool, None] = (
            surjective(self._B, self._R) if self.function else None
        )
        self.bijective: Union[bool, None] = (
            self.injective and self.surjective if self.function else None
        )
        self.inverse: Union[Set[Tuple[T, T]], None] = (
            self._inverse(self._R) if self.bijective else None
        )

    def _inverse(self, R: Set[Tuple[T, T]]) -> Set[Tuple[T, T]]:
        return {(b, a) for a, b in R}

    def __str__(self) -> str:
        return (
            "\n"
            + "\n".join([f"A: {self._A}", f"B: {self._B}", f"R: {self._R}"])
            + "\n\t"
            + (
                "R is not a total function"
                if not self.function
                else "\n\t".join(
                    [
                        i
                        for i in [
                            f"R is a total function",
                            f"Injective?: {self.injective}",
                            f"Surjective?: {self.surjective}",
                            f"Bijective?: {self.bijective}",
                            f"Inverse: {self.inverse}" if self.bijective else "",
                        ]
                        if i
                    ]
                )
            )
        )
