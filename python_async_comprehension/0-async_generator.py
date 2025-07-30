#!/usr/bin/env python3
"""
It contains a async function:
async_generator()
"""
import random
import asyncio
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None, ]:
    """
    An asynchronous function that generates a random number
    between 0 and 10, waiting one second between each loop.

    Arg:
        Nothing

    Return:
        A async Generator of float number
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
