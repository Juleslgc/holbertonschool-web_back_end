#!/usr/bin/env python3
"""
It contains a async function:
wait_n()
"""
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    A function asynchronous that spawn wait_random n time
    with the specified max_delay.

    Args:
        n (int): It's the number times that function called is spawn
        max_delay (int): It's specified of wait_random

    Return:
        A list of all the delays in ascending order
    """
    task = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    return [await completed for completed in asyncio.as_completed(task)]
