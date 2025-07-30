#!/usr/bin/env python3
"""
This module defines an asynchronous
function that collects values from an async generator.
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
    return [num async for num in async_generator()]
