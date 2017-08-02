#!/usr/bin/python3
# claudio_detab.py
# Author: Claudio <3261958605@qq.com>
# Created: 2017-08-01 21:48:02
# Code:
'''
将文件中的tab替换为空白字符
'''
import sys

FILE_IN = sys.argv[1]
FILE_OUT = sys.argv[2]


with open(FILE_IN, 'r') as fi:
    string = fi.read()
    string = string.replace('\t', ' ' * 4)

    with open(FILE_OUT, 'w') as fo:
        fo.write(string)
