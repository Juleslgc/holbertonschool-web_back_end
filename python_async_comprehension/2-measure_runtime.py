#!/usr/bin/env python3
"""
This module defines a coroutine to
measure the total runtime of async comprehensions.
"""

import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    An asynchronous function that measure the total
    runtime and return it.

    Arg:
        Nothing

    Return:
        The total runtime in a float number
    """
    start: float = time.time()
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )
    end: float = time.time()
    total_time: float = end - start
    return total_time
