#!/usr/bin/env python 3
'''task 8 module
'''

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    def multiply(value: float) -> float:
        '''creates multiplier function
        '''
        return value * multiplier
    return multiply
