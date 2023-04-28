#!/usr/bin/python3

'''Complex types - functions'''

from typing import Callable

def make_multiplier(multiplier: float) -> Callable[[float], float]:
    def multiplier_func(num: float) -> float:
        return num * multiplier
    return multiplier_func

