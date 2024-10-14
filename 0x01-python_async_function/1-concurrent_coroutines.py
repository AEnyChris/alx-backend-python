#!/usr/bin/env python3
'''
A function as a Chained coroutines
'''
import asyncio


wait_ran = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> list:
    '''returns a list of the outputs of wait_random'''
    res = [await wait_ran(max_delay) for i in range(n)]
    return res
