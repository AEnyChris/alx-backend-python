#!/usr/bin/env python3
'''Defines a function that returns a function'''
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''returns a multiplier function'''
    return lambda n: n * multiplier
