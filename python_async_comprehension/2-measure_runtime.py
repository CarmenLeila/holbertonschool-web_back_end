#!/usr/bin/env python3
"""
measure_runtime coroutine that will execute async_comprehension
four times in parallel using asyncio.gather
"""

import asyncio
import time


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    coroutine that executes async_comprehension four
    times in parallel using asyncio.gather
    """
    start_time = time.time()
    random = [async_comprehension() for index in range(4)]
    result = await asyncio.gather(*random)
    end_time = time.time()
    return end_time - start_time
