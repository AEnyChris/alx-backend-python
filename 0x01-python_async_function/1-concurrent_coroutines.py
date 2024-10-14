#!/usr/bin/env python3
'''Chained coroutines'''
import asyncio
import random


wait_ran = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int):
    res = [await wait_ran(max_delay) for i in range(n)]
    return res
