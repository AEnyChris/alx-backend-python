#!/usr/bin/env python3
'''
A function as a Chained coroutines
'''
import asyncio
from typing import List

wait_ran = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[int]:
    '''returns a list of the outputs of wait_random'''
    res = await asyncio.gather(
        *tuple(map(lambda _: wait_ran(max_delay), range(n)))
    )
    return sorted(res)
