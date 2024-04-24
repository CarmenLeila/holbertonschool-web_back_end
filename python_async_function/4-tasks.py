#!/usr/bin/env python3
"""Transformation in new def task_wait_n and returns list of delays"""

import asyncio
import random
from typing import List


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """calling task_wait_random"""
    tasks = [task_wait_random(max_delay) for index in range(n)]
    delays = await asyncio.gather(*tasks)
    return sorted(delays)
