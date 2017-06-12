#!/usr/bin/python3
# Author: Claudio <3261958605@qq.com>
# Created: 2017-06-05 16:12:37
# Code:
'''
汉字相关工具
'''

import re


def format_han(string, columns, align='<'):
    '格式化有汉字的字符串。'
    han_nums = len(re.findall(r'[\u4e00-\u9fa5]', string))
    # print(han_nums)
    spec = '{:' + '{}{}'.format(align, columns - han_nums) + '}'
    return spec.format(string)


if __name__ == '__main__':
    print(repr(format_han('2', 3)))
    print(repr(format_han('二', 3)))
