#!/usr/bin/env python3
'''Annotated function with a list argument'''

from typing import List


def sum_list(input_list: List[float]) -> float:
    '''return the sum of a list'''
    return sum(input_list)
