#!/usr/bin/env python3
"""
It contains a function:
task_wait_random()
"""
import asyncio
from typing import Any
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task[Any]:
    """
    A function that return a asyncio.Task that execut wait_random.

    Arg:
        max_delay (int): The maximum time to wait in wait_random

    Return:
        A asyncio.Task
    """
    task = wait_random(max_delay)
    return asyncio.create_task(task)
