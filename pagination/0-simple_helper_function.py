#!/usr/bin/env python3
"""takes two integer arguments page and page_size"""


def index_range(page, page_size):
    """returns a tuple of size two containing a start index"""
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return (start_index, end_index)
