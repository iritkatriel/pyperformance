"""Microbenchmark for Python's sequence unpacking."""

import perf
from six.moves import xrange


def do_unpacking(loops, to_unpack):
    range_it = xrange(loops)
    t0 = perf.perf_counter()

    for _ in range_it:
        # 400 unpackings
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack
        a, b, c, d, e, f, g, h, i, j = to_unpack

    return perf.perf_counter() - t0


def bench_tuple_unpacking(loops):
    x = tuple(range(10))
    return do_unpacking(loops, x)


def bench_list_unpacking(loops):
    x = list(range(10))

    return do_unpacking(loops, x)


def bench_all(loops):
    dt1 = bench_tuple_unpacking(loops)
    dt2 = bench_list_unpacking(loops)
    return dt1 + dt2


def add_cmdline_args(cmd, args):
    if args.benchmark:
        cmd.append(args.benchmark)


if __name__ == "__main__":
    benchmarks = {"tuple": bench_tuple_unpacking,
                  "list": bench_list_unpacking}

    runner = perf.Runner(add_cmdline_args=add_cmdline_args)
    runner.metadata['description'] = ("Microbenchmark for "
                                      "Python's sequence unpacking.")

    runner.argparser.add_argument("benchmark", nargs="?",
                                  choices=sorted(benchmarks))

    options = runner.parse_args()
    name = 'unpack_sequence'
    if options.benchmark:
        func = benchmarks[options.benchmark]
        name += "_%s" % options.benchmark
    else:
        func = bench_all

    runner.bench_sample_func(name, func, inner_loops=400)
