#!/usr/bin/env python3
"""a coroutine called async_generator that takes no arguments"""


from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    coroutine that collects 10 random numbers using an
    async comprehensing then return the 10 random numbers
    """
    return [number async for number in async_generator()]