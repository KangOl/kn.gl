#!/usr/bin/env python

def rowify(iterable, max_per_row=4):
    """yield slices of `iterable` with a maximum of `max_per_row` per slice"""
    # I'm sure there is better algorithm...
    n = len(iterable)
    x = 1.0
    while (n / x) > max_per_row:
        x += 1.0
    x = int(round(n / x))

    for y in range(0, n, x):
        yield iterable[y:y + x]

if __name__ == '__main__':
    import string
    for r in rowify(string.ascii_lowercase[:18], 7):
        print r
