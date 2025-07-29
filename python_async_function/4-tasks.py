#!/usr/bin/env python3
"""
It contains a async function:
task_wait_random()
"""

import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    A function asynchronous that spawn task_wait_random n time
    with the specified max_delay.

    Args:
        n (int): It's the number times that function called is spawn
        max_delay (int): It's specified of task_wait_random

    Return:
        A list of all the delays in ascending order
    """
    task = [task_wait_random(max_delay) for _ in range(n)]
    return [await completed for completed in asyncio.as_completed(task)]
