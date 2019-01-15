#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re


def string_to_color(s):
    """
    Converts color string to tuple.
    '10,20,30' - (10,20,30)
    Returns None when error.
    """
    m = re.match(r"(0|[1-9][0-9]{0,2}),(0|[1-9][0-9]{0,2}),(0|[1-9][0-9]{0,2})", s)
    if not m:
        return None
    a = map(int, m.groups())
    if any(map(lambda v: v > 255, a)):
        return None
    return tuple(a)
