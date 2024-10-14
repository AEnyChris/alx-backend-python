#!/usr/bin/env python3
"""A simple coroutine function"""
import time
import asyncio
from random import uniform as runif


async def wait_random(max_delay: int = 10) -> float:
    '''a coroutine to return delay time'''
    res = runif(0, max_delay)
    await asyncio.sleep(res)
    return res
