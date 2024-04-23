#!/usr/bin/python3
"""
Annotate the below function’s parameters and return
values with the appropriate types

"""


from typing import List, Tuple, Iterable, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ return list of tuple of item & item length"""
    return [(index, len(index)) for index in lst]
