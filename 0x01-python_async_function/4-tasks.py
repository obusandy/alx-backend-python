#!/usr/bin/env python3
"""
Task n
"""
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random
task_wait_random = __import__('3-tasks').task_wait_random

async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Execute task_wait_random
    Args:
        n (int): The number of times task wait random
        max_delay (int): The maximum delay val
    Returns: a sorted list of the results.

    """
    respns = await asyncio.gather(*(task_wait_random(max_delay)
                               for _ in range(n)))

    # sort ascending oredr
    for rndmdelay in range(len(respns)):
        for j in range(rndmdelay+1, len(respns)):
            if (respns[rndmdelay] > respns[j]):
                respns[rndmdelay], respns[j] = respns[j], respns[rndmdelay]

    return respns