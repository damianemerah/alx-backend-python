#!/usr/bin/env python3
"""Task 10"""
from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Return lst[0] or None"""
    if lst:
        return lst[0]
    else:
        return None
