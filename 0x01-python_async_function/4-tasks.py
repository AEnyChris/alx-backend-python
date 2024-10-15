#!/usr/bin/env python3
"""This script Take the code from wait_n
and alter it into a new function task_wait_n.
The code is nearly identical to wait_n except
task_wait_random is being called.
"""

import asyncio


from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    '''returns a list of the outputs of wait_random'''
    res = await asyncio.gather(
            *(task_wait_random(max_delay) for i in range(n)))
    return sorted(res)
