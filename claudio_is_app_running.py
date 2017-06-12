#!/usr/bin/python3
# Author: Claudio <3261958605@qq.com>
# Created: 2017-06-08 09:29:57
# Code:
'''
指定应用是否正在执行
'''

import subprocess
import sys
from collections import namedtuple


def is_app_running(app):
    'APP是否正在运行。返回[(PID1, USER1, COMMAND1), (PID2, USER1, COMMAND2)...]'
    result = []
    proc1 = subprocess.Popen(
        ['ps', 'aux'], stdout=subprocess.PIPE, universal_newlines=True)
    proc2 = subprocess.Popen(
        ['grep', app], stdin=proc1.stdout, stdout=subprocess.PIPE, universal_newlines=True)
    proc1.stdout.close()
    output = proc2.communicate()[0]
    app_lines = output.splitlines()

    if len(app_lines) <= 1:          # 只包含grep app的行
        return result

    for line in app_lines:
        Running = parse_grep_result(line)

        if Running.command == 'grep ' + app:  # 当前grep命令
            continue
        if sys.argv[0] in Running.command:            # 当前脚本进程
            continue

        if app in Running.command:
            result.append((Running.pid, Running.user, Running.command))

    return result


def parse_grep_result(line):
    '解析grep命令结果，排除有"grep app"的行，返回'
    Running = namedtuple(
        'Running', 'user pid cpu mem vsz rss tty stat start time command ')
    return Running._make(line.split(maxsplit=len(Running._fields) - 1))


if __name__ == '__main__':
    import argparse
    parse = argparse.ArgumentParser(description='判断系统中是否正在运行某个APP')
    parse.add_argument('app', nargs=argparse.REMAINDER, help='APP名称')
    args = parse.parse_args()
    # print(' '.join(args.app))
    app = ' '.join(args.app)
    # print(app)
    for item in is_app_running(app):
        print('PID：', item[0])
        print('User：', item[1])
        print('Cmd：', item[2])
        print('-' * 80)
