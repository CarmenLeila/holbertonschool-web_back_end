#!/usr/bin/env python3
"""a coroutine called async_generator that takes no arguments"""

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """async_generator that takes no arguments"""
    for num in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
