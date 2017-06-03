#!/usr/bin/python3
# Author: Claudio <3261958605@qq.com>
# Created: 2017-05-12 17:18:40
# Commentary:
# 使用bisect实现完整二分查找对象的例子，可参考：https://code.activestate.com/recipes/577197-sortedcollection/
# Code:

'''
利用bisect模块实现对已排序链表元素查找。（摘抄自标准库文档）
可提升大型链表的查找速度。
'''

from bisect import bisect_left, bisect_right


def index(a, x):
    '定位最左边等于X的元素。'
    i = bisect_left(a, x)
    if i != len(a) and a[i] == x:
        return i
    raise ValueError


def find_lt(a, x):
    '获取<X的最右边的元素。'
    i = bisect_left(a, x)
    if i != 0:
        return a[i - 1]
    raise ValueError


def find_le(a, x):
    '获取<=X的最右边的元素。'
    i = bisect_right(a, x)
    if i != 0:
        return a[i - 1]
    raise ValueError


def find_gt(a, x):
    '获取>X的最左边的元素。'
    i = bisect_right(a, x)
    if i != len(x):
        return a[i]
    raise ValueError


def find_ge(a, x):
    '获取>=X最左边的元素。'
    i = bisect_left(a, x)
    if i != len(a):
        return a[i]
    raise ValueError
