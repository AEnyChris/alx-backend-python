#!/usr/bin/env python3
"""
Defines a function to test the
runtime of an asynchronous generator
"""
import asyncio
import time


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """returns the runtime of execting
    async_comprehension four times in parallel"""
    start = time.perf_counter()
    await asyncio.gather(*(async_comprehension() for i in range(4)))
    elapse = time.perf_counter() - start
    return elapse
