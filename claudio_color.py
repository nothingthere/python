#!/usr/bin/python3
# Author: Claudio <3261958605@qq.com>
# Created: 2017-05-21 22:34:24
# Code:
'''
将字符串转换为带颜色的命令行字符串。
'''

__all__ = ['colorful']

COLORS = {
    'black': '\033[0;30m',
    'red': '\033[0;31m',
    'green': '\033[0;32m',
    'brown': '\033[0;33m',
    'blue': '\033[0;34m',
    'purple': '\033[0;35m',
    'dark-gray': '\033[1;30m',
    'light-red': '\033[1;31m',
    'light-green': '\033[1;32m',
    'yellow': '\033[1;33m',
    'light-blue': '\033[1;34m',
    'light-purple': '\033[1;35m'
}

COLOR_END = '\033[0;0m'


def colorful(string, color='green'):
    '将字符串STRING变为COLOR颜色。'
    if color not in COLORS:
        return string
    return COLORS[color] + string + COLOR_END


def list_all():
    '列出所有颜色。'
    for k in COLORS.keys():
        print(colorful(k, k))


if __name__ == '__main__':
    list_all()
