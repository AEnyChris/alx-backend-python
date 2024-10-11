#!/usr/bin/env python3
'''
More involved type annotations
'''
from typing import TypeVar, Union, Any, Mapping


T = TypeVar('T')
dt = Union[T, None]
rt = Union[Any, T]


def safely_get_value(dct: Mapping, key: Any, default: dt = None) -> rt:
    '''safely get value of key or none'''
    if key in dct:
        return dct[key]
    else:
        return default
