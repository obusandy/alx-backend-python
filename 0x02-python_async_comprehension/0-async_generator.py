#!/usr/bin/env python3
"""a coroutine called async_generator
that takes no args.
"""

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """ Generate a sequence of random numbers asynchronously.

    Yields:
        float: A random number between 0 and 10.
        """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)