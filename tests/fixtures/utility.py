from mesa_behaviors.utility.utility import BaseUtility
from typing import Sequence, Callable


class DummyUtility(BaseUtility[int, Sequence[int], int]):
    def utility_score(self, strategies: int, history: Callable[[], Sequence[int]]):
        return 99


class DummyUtility1(BaseUtility[int, Sequence[int], int]):
    def utility_score(self, strategies: int, history: Callable[[], Sequence[int]]):
        return 101
