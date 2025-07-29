#!/usr/bin/env python3
"""
It contains a funtion:
measure_time()
"""

import time
import asyncio

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    A function that measures the total execution time for
    wait_n(n, max_delay).

    Args:
        n (int): It's the number times that function called is spawn
        max_delay (int): It's specified of wait_random

    Return:
        The total execution time
    """
    departure = time.time()
    asyncio.run(wait_n(n, max_delay))
    end = time.time()
    total_time = end - departure
    return total_time / n
