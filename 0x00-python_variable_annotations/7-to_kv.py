#!/usr/bin/env python3
"""A function that returns a tuple"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Return  tuple with variable(str) k and square of value(float) v"""
    return k, float(v ** 2)
