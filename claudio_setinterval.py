#!/usr/bin/python3
# Author: Claudio <3261958605@qq.com>
# Created: 2017-06-25 11:56:23
# Code:
'''
模仿js的SetInterval
'''

import sched
import time


def set_interval(func, interval, *args, **kwds):
    '''间隔一定时间执行函数
    func：需执行的函数
    args：func的位置参数
    kwds：func的关键字参数
    interval：间隔时间
    '''

    s = sched.scheduler(timefunc=time.time, delayfunc=time.sleep)

    def run():
        func(*args, **kwds)
        s.enter(interval, 0, run)

    def main():
        s.enter(0, 0, run)
        s.run()

    main()


if __name__ == '__main__':
    set_interval(print, 0.1, 'hello, world')
