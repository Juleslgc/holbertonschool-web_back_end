#!/usr/bin/env python3
"""
It contains the async function:
wait_random()
"""

import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """
    A function asynchronous that wait random delay
    and return it.

    Arg:
        max_delay (int): Interger with default value of 10

    Return:
        A wait random delay
    """
    time = random.uniform(0, max_delay)
    await asyncio.sleep(time)
    return time
