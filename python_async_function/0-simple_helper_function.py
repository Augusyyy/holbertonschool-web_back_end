#!/usr/bin/env python3

from typing import Tuple
def index_range(page: int, page_size: int) -> Tuple[int, int]:
    return ((page_size * (page - 1)), page_size * page)
