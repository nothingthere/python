#!/usr/bin/python3
# Author: Claudio <3261958605@qq.com>
# Created: 2017-05-21 18:01:00
# Code:
'''
阶乘函数。尝试doctest用法。

>>> factorial(5)
120
'''
from functools import lru_cache


@lru_cache()
def factorial(integer):
    '''返回INTEGER的阶乘，INTEGER为>=0的整数。

    >>> [factorial(n) for n in range(6)]
    [1, 1, 2, 6, 24, 120]

    >>> factorial(30)
    265252859812191058636308480000000

    >>> factorial(-1)
    Traceback (most recent call last):
    ....
    ValueError: integer需>=0

    >>> factorial(30.1)
    Traceback (most recent call last):
    ....
    ValueError: integer需为整数

    >>> factorial(1e100)
    Traceback (most recent call last):
    ....
    OverflowError: integer值太大

    '''
    import math
    # 参数过滤
    if not integer >= 0:
        raise ValueError('integer需>=0')

    if math.floor(integer) != integer:
        raise ValueError('integer需为整数')

    if integer + 1 == integer:
        raise OverflowError('integer值太大')
    # 正式执行
    if integer <= 1:
        return 1
    return integer * factorial(integer - 1)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    # print(factorial(-1))
