#!/usr/bin/python3
# Author: Claudio <3261958605@qq.com>
# Created: 2017-05-07 18:36:06
# Commentary: 转抄自Python标准库页面：
# https://docs.python.org/3/library/itertools.html#itertools-recipes
'''
函数式编程工具
'''

import operator
import random
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
    return sum(map(operator.mul, vec1, vec2))


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


def unique_everseen(iterable, key=None):
    '''返回去重元素，保持原来顺序。记忆所有出现过的元素

    unique_everseen('AAABBCCCDDAABB') --> A B C D
    unique_everseen('ABCcAaD', str.lower) --> A B C D
    '''
    seen = set()
    seen_add = seen.add
    if key is None:
        for element in filterfalse(seen.__contains__, iterable):
            seen_add(element)
            yield element
    else:
        for element in iterable:
            k = key(element)
            if k not in seen:
                seen_add(k)
                yield element


def unique_justseen(iterable, key=None):
    '''返回去重元素，保持原来顺序。只记忆当前出现过的元素

    unique_everseen('AAABBCCCDDAABB') --> A B C D A B
    unique_everseen('ABCcAaD', str.lower) --> A B C A D
    '''
    return map(next, map(operator.itemgetter(1), groupby(iterable, key)))


def iter_except(func, exception, first=None):  # ？？？
    try:
        if first is not None:
            yield first()
        while True:
            print('...')
            yield func()
    except exception:
        print('!!!')
        pass


def random_product(*args, repeat=1):
    '随机笛卡尔乘积元素。即相当于itertools.product(*args, **kwds)中的随机元素。'
    pools = [tuple(pool) for pool in args] * repeat
    print(list(pools))
    return tuple(random.choice(pool)for pool in pools)


def random_permutation(iterable, r=None):
    pool = tuple(iterable)
    r = len(pool) if r is None else r
    return tuple(random.sample(pool, r))


def random_combination(iterable, r):
    '从itertools.combinations(iterable, r)中随机获取元素。'
    pool = tuple(iterable)
    n = len(pool)
    indices = sorted(random.sample(range(n), r))
    return tuple(pool[i] for i in indices)


def random_combination_with_replacement(iterable, r):
    '从itertools.combinations_with_replacement(iterable, r)中随机获取元素。'
    pool = tuple(iterable)
    n = len(pool)
    indices = sorted(random.randrange(n) for i in range(r))
    return tuple(pool[i] for i in indices)


def mappend(fn, args):
    "与CL同名函数用法相同。"
    return [item for result in map(fn, args)
            for item in result]


if __name__ == '__main__':
    print(list(unique_everseen('AAABBCCCDDAABB')))
    print(list(unique_everseen('ABCcAaD', str.lower)))
