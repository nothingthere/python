#!/usr/bin/python3
# Author: Claudio <3261958605@qq.com>
# Created: 2017-06-05 12:52:38
# Code:
'''
Excel文件处理工具
'''


from collections import namedtuple

import xlrd

from claudio_file_utils import ClaudioFileUtils


class ClaudioXLSUtils:
    'Excel文件处理工具。'

    def __init__(self, filename):
        claudio_file = ClaudioFileUtils(filename)
        if not claudio_file.exists():
            raise FileNotFoundError('文件不存在：{}'.format(filename))
        if not claudio_file.is_excel_file():
            raise TypeError('不为Excel文件：{}'.format(filename))
        self._book = xlrd.open_workbook(filename, on_demand=True)

    def get_nsheets(self):
        '返回所有sheets组成的链表。'
        return self._book.nsheets

    def get_headers(self, index=0):
        '获取第INDEX和sheet中的头信息。'
        if index < 0 or index >= self._book.nsheets:
            return []

        sheet = self._book.sheet_by_index(index)
        try:                    # 可能sheet中只有1行
            headers = [sheet.cell_value(1, i) for i in range(sheet.ncols)]

            def normalize_header(header, replace='X'):
                '将没有任何实际字符的项目转换为X。'
                if not header.strip():
                    return replace
                else:
                    return header.strip()

            return [normalize_header(header) for header in headers]
        except IndexError:
            return []

    def get_values(self, index=0):
        '获取第INDEX和sheet中所有值组成的链表。'
        headers = self.get_headers(index=index)
        Item = namedtuple('Item', headers)
        # print(Item._fields)
        result = []
        sheet = self._book.sheet_by_index(index)
        for row in range(sheet.nrows):
            item = []
            for col in range(sheet.ncols):
                item.append(sheet.cell_value(row, col))
            # print(item)
            # print(Item._make(item))
            result.append(Item._make(item))
        return result


if __name__ == '__main__':
    filename = '/home/claudio/身份证.xls'
    xls = ClaudioXLSUtils(filename)
    # xls.test()
    # print(xls.get_sheets())
    # print(xls.get_headers())
    # print(xls._book.nsheets)
    # xls.get_values(index=0)
