#!/usr/bin/env python3
"""
It contains an async function:
async_comprehension()
"""

from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    An asynchronous function that collect 10 random numbers using
    an async comprehensing over async_generator then return.

    Arg:
        Nothing

    Return:
        A list of 10 random numbers
    """
    result: List[float] = []
    async for num in async_generator():
        result.append(num)
    return result
