#!/usr/bin/env python3
""" Measure the total execution time
for running four parallel
asynchronous comprehensions."""
import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension

# main point of execution
async def measure_runtime() -> float:
    """ Returns:
        float: The total runtime in seconds.
    """
    start_time = time.perf_counter()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    ttlruntime = time.perf_counter() - start_time
    return ttlruntime