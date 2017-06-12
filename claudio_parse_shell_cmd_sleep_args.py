#!/usr/bin/python3
# Author: Claudio <3261958605@qq.com>
# Created: 2017-05-31 16:49:56
# Code:
'''
解析Linux系统命令sleep参数
'''

import re


def parse(string):
    '解析函数'
    result = 0
    token_specification = [
        ('number', r'\d+(?:\.\d*)?'),  # 整数或分数
        ('type', r'[SsMmHh]?'),       # 代表时、分、秒的字符
    ]

    tok_regex = ''.join('(?P<{}>{})'.format(
        pair[0], pair[1]) for pair in token_specification)
    # tok_regex = '({})'.format(tok_regex)
    # print(tok_regex)
    for mo in re.finditer(tok_regex, string):
        t = mo.group('type')
        v = mo.group('number')
        # print(t, v)
        if not t:
            result += float(v)

        if t.lower() == 's':
            result += float(v)
        if t.lower() == 'm':
            result += float(v) * 60
        if t.lower() == 'h':
            result += float(v) * 60 * 60

    return float(result)


if __name__ == '__main__':
    print(parse('1m20>'))
