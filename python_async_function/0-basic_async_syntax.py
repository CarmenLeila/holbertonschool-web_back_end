#!/usr/bin/env python3
"""Write an asynchronous coroutine that takes an integer argument """

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """ return random delay """
    random_delay = random.uniform(0, max_delay)
    await asyncio.sleep(random_delay)
    return random_delay
