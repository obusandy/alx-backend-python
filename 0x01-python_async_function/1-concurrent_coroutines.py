#!/usr/bin/env python3
"""
wait_n that takes in 2 int arguments.
"""
import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Wait for n random delays and return a sorted list of results.

    Args:
        n (int): The number of random delays to wait for.
        max_delay (int): The maximum delay val
    returns: List[float]: A sorted list.
    """
    # to Wait for Multiple Random Delays
    respns = await asyncio.gather(*(wait_random(max_delay) for _ in range(n)))

    for rndmdelay in range(len(respns)):
        for j in range(rndmdelay+1, len(respns)):
            if (respns[rndmdelay] > respns[j]):
                respns[rndmdelay], respns[j] = respns[j], respns[rndmdelay]

    return respns