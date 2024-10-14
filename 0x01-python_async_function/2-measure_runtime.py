#!/usr/bin/env python3
"""Measuring the runtime"""

import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """returns the elapse time of a coroutine call"""
    start = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    elapse = time.perf_counter() - start
    return elapse/n
