#!/usr/bin/env python3
""" a coroutine called async_comprehension
that takes no
arguments
"""

from typing import List
async_generator = __import__('0-async_generator').async_generator
async def async_comprehension() -> List[float]:
    """Collect 10 random numbers using an asynchronous comprehension
    Returns:
        List[float]: A list of 10 random numbers."""
    return [intgr async for intgr in async_generator()]