#!/usr/bin/env python3
'''Annotated function with a list argument'''

from typing import List, Union


def sum_mixed_list(input_list: List[Union[int, float]]) -> float:
    '''return the sum of a list'''
    return sum(input_list)
