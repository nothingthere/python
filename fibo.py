#!/usr/bin/python3
# Author: Claudio <3261958605@qq.com>
# Created: 2017-05-02 15:03:48
# Commentary:
# Code:

'''
Fibonacci
'''

import functools


@functools.lru_cache(maxsize=None)
def fib(n):
    if n <= 2:
        return n
    else:
        return fib(n - 1) + fib(n - 2)


fn = fib

for i in range(1000):
    print(fib(i))
