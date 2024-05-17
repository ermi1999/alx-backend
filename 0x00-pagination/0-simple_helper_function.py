#!/usr/bin/env python3
"""
module for calculating a pagination.
"""


def index_range(page: int, page_size: int) -> tuple[int, int]:
    """
    function for calculating a pagination.
    """
    return ((page_size * page) - page_size, page_size * page)
