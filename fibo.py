#!/usr/bin/python3
# Author: Claudio <3261958605@qq.com>
# Created: 2017-05-02 15:03:48
# Commentary:
# Code:


def fib(n):
    a, b = 0, 1
    while b < n:
        print(b, end=' ')
        a, b = b, a + b
    print()


def fib2(n):
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a + b
    return result
