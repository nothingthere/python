#!/usr/bin/python3
# Author: Claudio <3261958605@qq.com>
# Created: 2017-06-05 11:41:32
# Code:
'''
从网上获取别人身份证号码。
'''

import re

from claudio_chinese_utils import format_han
from claudio_xls_utils import ClaudioXLSUtils


class ClaudioGetIDCardNumbers:
    '从网上获取别人身份证号码。'

    def __init__(self):
        self.IDENTIFY_RE = re.compile('.*身份证.*')
        self.NAME_RE = re.compile('.*姓名.*')
        self._parse_result_headers = None
        self._parse_result = self.parse_xls_file(self.get_xls_file())

    @staticmethod
    def get_xls_file():
        '将Excel文件下载到本地'
        return '/home/claudio/身份证.xls'

    def parse_xls_file(self, name):
        '解析Excel文件，返回字典。'
        xls = ClaudioXLSUtils(name)
        nsheets = xls.get_nsheets()
        index = None
        found_sheet = False
        for i in range(nsheets):
            if found_sheet:
                break
            headers = xls.get_headers(index=i)
            for header in headers:
                if self.IDENTIFY_RE.match(header):
                    found_sheet = True
                    index = i
                    self._parse_result_headers = headers
                    break

        if not index == None:
            return xls.get_values(index=index)
        else:
            return None

    def show_parse_result(self):
        '打印parse_xls_file的返回结果'
        print(self._parse_result)

    def dump_parse_result(self, outfile):
        '将解析结果存储到本地文件OUTFILEE中。'
        with open(outfile, 'w') as fp:
            for item in self._parse_result:
                for header in self._parse_result_headers:
                    if self.NAME_RE.match(header):
                        name = item[self._parse_result_headers.index(header)]
                        # print(repr(format_han(name, 13)))
                        fp.write(format_han(name, 13))  # 可能有少数民族名字
                        fp.write(' ')
                    if self.IDENTIFY_RE.match(header):
                        num = item[self._parse_result_headers.index(header)]
                        fp.write('{:17}'.format(num))
                        fp.write('\n')


if __name__ == '__main__':
    result = ClaudioGetIDCardNumbers()
    # result.show_parse_result()
    result.dump_parse_result('/home/claudio/result.txt')
    print('done')
