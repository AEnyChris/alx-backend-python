#!/usr/bin/env python3
"""Defines an asynchronous generator"""
from typing import Generator
import asyncio
import random


async def async_generator() -> Generator[float, None, None]:
    """returns a list of random float numbers between 0 and 10"""
    for i in range(10):
        yield random.random() * 10
        await asyncio.sleep(1)
