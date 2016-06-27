# -*- coding: utf-8 -*-


def premmissing(A):
    return sum(xrange(min(A), max(A) + 1)) - sum(A)

premmissing([2, 1, 5, 4])