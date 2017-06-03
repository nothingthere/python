#!/usr/bin/python3
# Author: Claudio <3261958605@qq.com>
# Created: 2017-05-21 21:01:02
# Code:

'''
获取磁盘分区情况。
参考地址：http://code.activestate.com/recipes/580737-get-disk-partition-information-with-psutil-cross-p/
'''

if __name__ == '__main__':
    import psutil
    dps = psutil.disk_partitions(all=True)
    fmt_str = '{:<8} {:<7} {:<7}'
    print(fmt_str.format('位置', '文件类型', '属性'))
    for dp in sorted(dps):
        print(fmt_str.format(dp.device, dp.fstype, dp.opts))
