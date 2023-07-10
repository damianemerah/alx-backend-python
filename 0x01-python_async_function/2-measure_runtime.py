#!/usr/bin/env python3
"""Import wait_n() and measures time ti run it"""
import time
import asyncio

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Measure time to run wait_n()"""
    start = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    elapsed_time = time.perf_counter() - start

    return elapsed_time
