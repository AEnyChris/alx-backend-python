#!/usr/bin/env python3
"""Defines an asynchronous generator"""
from typing import AsyncGenerator
import asyncio
import random


async def async_generator() -> AsyncGenerator[float, None]:
    """returns a random number between 0 and 10 but float"""
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
