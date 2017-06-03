#!/usr/bin/python3
# Author: Claudio <3261958605@qq.com>
# Created: 2017-05-23 16:20:54
# Code:

'''
文件夹遍历工具。
'''

import os
from pathlib import Path


class ClaudioWalkTree:
    '文件夹遍历类。'

    def __init__(self, path):
        '初始化路径。'
        path = Path(path)
        if not (path.exists() and path.is_dir()):
            raise TypeError('{} 不是文件夹，或不存在'.format(path))
        self.path = str(path)

    def all_paths(self, resolve=False):
        """返回PATH中所有文件组成的链表"""
        path_collection = []
        for dirpath, dirnames, filenames in os.walk(self.path):
            for file in filenames:
                fullpath = os.path.join(dirpath, file)
                if resolve:
                    fullpath = str(Path(fullpath).resolve())
                path_collection.append(fullpath)

        return path_collection

    def all_files(self):
        '返回当前文件夹中的所有文件名，组成的链表。'
        file_collection = []

        for dirpath, dirnames, filenames in os.walk(self.path):
            for file in filenames:
                file_collection.append(file)

        return file_collection

    def all_dirs(self):
        '返回当前文件夹中所有子文件夹组成的链表。'
        dir_collections = []
        for dirpath, dirnames, filenames in os.walk(self.path):
            for dirname in dirnames:
                dir_collections.append(dirname)

        return dir_collections


if __name__ == '__main__':
    import os
    os.chdir('/tmp')
    WP = ClaudioWalkTree('.')
    # print(WP)
    print(WP.all_paths(resolve=True))
