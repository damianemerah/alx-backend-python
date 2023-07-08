#!/usr/bin/env python3
"""Python typing annotation"""
from typing import Tuple, List, Sequence, Iterable


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Return a list of tuples"""
    return [(i, len(i)) for i in lst]
