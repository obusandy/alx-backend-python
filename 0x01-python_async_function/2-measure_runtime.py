#!/usr/bin/env python3
"""as arguments that measures the total
execution time for wait_n(n, max_delay)
"""
import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measure the total execution time for wait_n(n, max_delay)
    Args:
        n (int): The no of coroutines to run.
        max_delay (int): The maximum delay val.

    returns: the average time per coroutine.
    """
    start_time = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    ttlruntime = time.perf_counter() - start_time

    return ttlruntime / n