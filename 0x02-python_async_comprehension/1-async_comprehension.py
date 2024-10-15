#!/usr/bin/env python3
"""collects 10 random numbers from async generator"""

from typing import List
import asyncio


async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """returns a list of 10 random numbers comprehensively"""
    res = [n async for n in async_generator()]
    return res
