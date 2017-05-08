#!/usr/bin/python3
# Author: Claudio <3261958605@qq.com>
# Created: 2017-05-06 12:45:25
# Commentary:
# Code:

'''
允许在所有元素字典中赋值和删除的ChainMap子类
'''

from collections import ChainMap


class ClaudioDeepChainMap(ChainMap):
    '''允许在所有元素字典中赋值和删除的ChainMap子类.'''

    def __setitem__(self, key, val):
        for mapping in self.maps:
            if key in mapping:
                mapping[key] = val
                return
        self.maps[0][key] = val

    def __delitem__(self, key):
        for mapping in self.maps:
            if key in mapping:
                del mapping[key]
                return
        raise KeyError(key)


if __name__ == '__main__':
    d = ClaudioDeepChainMap({'zebra': 'black'},
                            {'elephant': 'blue'},
                            {'lion': 'yellow'})

    d['lion'] = 'orange'
    print(d)
    d['snake'] = 'blue'
    print(d)
    del d['zebra']
    print(d)
