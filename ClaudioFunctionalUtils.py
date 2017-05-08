#!/usr/bin/python3
# Author: Claudio <3261958605@qq.com>
# Created: 2017-05-07 18:36:06
# Commentary: 转抄自Python标准库网页
'''
函数式编程工具
'''

from collections import deque
from itertools import (chain,
                       combinations,
                       count,
                       cycle,
                       filterfalse,
                       groupby,
                       islice,
                       repeat,
                       starmap,
                       tee,
                       zip_longest)
from operator import mul


def take(n, iterable):
    '返回ITERABLE中前N个元素组成的链表。'
    return list(islice(iterable, n))


def tabulate(function, start=0):
    '返回 function(0), function(1)...'
    return map(function, count(start))


def tail(n, iterable):
    """返回ITERABLE最后N个元素组成的迭代器。
    tail(3, 'ABCDEFG') --> E F G
    """
    return iter(deque(iterable, maxlen=n))


def consum(iterator, n=None):
    '将ITERATOR向前推进N个元素，如果N为None，消耗完整个ITERATOR。？？？'
    if n is None:
        deque(iterator, maxlen=0)
    else:
        next(islice(iterator, n, n), None)


def nth(iterable, n, default=None):
    '返回iterable的第N个元素，或DEFAULT'
    return next(islice(iterable, n, None), default)


def all_equal(iterable):
    '如果ITERABLE中所有元素都相等，返回True。'
    g = groupby(iterable)
    return next(g, True) and (not next(g, False))


def quantify(iterable, pred=bool):
    '返回ITERABLE中满足PRED条件的元素个数'
    return sum(map(pred, iterable))


def padnone(iterable):
    """
    返回ITERABLE中的元素，再无限制地返回None。

    可用于模仿内置函数map()？？？
    """
    return chain(iterable, repeat(None))


def ncycles(iterable, n):
    '返回ITERABLE重复N次的迭代器。'
    return chain.from_iterable(repeat(iterable, n))


def dotproduct(vec1, vec2):
    '点乘'
    return sum(map(mul, vec1, vec2))


def flatten(listOfLists):
    '将嵌套拉平一层。'
    return chain.from_iterable(listOfLists)


def repeatfunc(func, times=None, *args):
    '''一直重复调用FUNC，将ARGS作为参数。

    如：repeatfunc(random.random)生成无限多个随机数。
    '''
    if times is None:
        return starmap(func, repeat(args))
    return starmap(func, repeat(args, times))


def parwise(iterable):
    's -> (s0,s1), (s1,s2), (s2,s3),...'
    a, b = tee(iterable, 2)
    next(b, None)
    return zip(a, b)


def grouper(iterable, n, fillvalue=None):
    '''
    将ITERABLE分割为固定长度的块。

    理解方法：args中每个元素间迭代时不独立，即如果第一个调用next后，
    会消耗元素。如果第二个调用next，则为下一个元素。
    '''
    args = [iter(iterable)] * n
    return zip_longest(*args, fillvalue=fillvalue)


def roundrobin(*iterables):
    'roundrobin("ABC", "D", "EF") -> A D B C E F？？？'
    pending = len(iterables)
    nexts = cycle(iter(it).__next__ for it in iterables)
    while pending:
        try:
            for next in nexts:
                yield next()
        except StopIteration:
            pending -= 1
            nexts = cycle(islice(nexts, pending))


def partition(pred, iterable):
    '''使用PRED判断函数，将ITERABLE分割为满足条件和不满足条件的两块。

    partition(is_odd, range(10)) --> 0 2 4 6 8 和 1 3 5 7 9
    '''
    t1, t2 = tee(iterable, 2)
    return filterfalse(pred, t1), filter(pred, t2)


def powerset(iterable):
    'powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2, 3) (1,2,3)'
    s = list(iterable)          # ？？？为何不直接用iterable
    return chain.from_iterable(combinations(s, r) for r in range(len(s) + 1))


if __name__ == '__main__':
    data = powerset([1, 2, 3])
    for x in data:
        print(list(x))
