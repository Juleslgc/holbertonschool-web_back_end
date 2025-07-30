#!/usr/bin/env python3
"""
It contains an async function:
measure_runtime()
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
    start = time.perf_counter()
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )
    end = time.perf_counter()
    total_time = end - start
    return total_time
