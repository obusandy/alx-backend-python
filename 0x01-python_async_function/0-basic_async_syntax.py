#!/usr/bin/env python3
"""an asynchronous coroutine that takes in
an integer argument (max_delay)"""

import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """
    waits for a random delay.

    Args:
        max_delay: maximum delay value(10)
    Returns:
        float: The randomly awaited value
    """
    rndmdelay = random.uniform(0, max_delay)
    await asyncio.sleep(rndmdelay)
    return rndmdelay