#!/usr/bin/python3
# Author: Claudio <3261958605@qq.com>
# Created: 2017-06-04 22:48:06
# Code:
'''
解析Apache服务器访问日志
'''
import re
import sys
from collections import defaultdict
from pathlib import Path

from claudio_file_utils import ClaudioFileUtils


class ClaudioApacheLogAccessParser:
    def __init__(self, logfile):
        self.regex = re.compile(r'''
        (?P<remote_host>\S+)
        \s+
        (?P<remote_logname>\S+)
        \s+
        (?P<remote_user>\S+)
        \s+
        \[(?P<time>.+)\]
        \s+
        "(?P<request>[^"]+)"
        \s+
        (?P<status>\d+)
        \s+
        (?P<bytes>\d+)
        \s+
        "(?P<url>[^"]+)"
        \s+
        "(?P<user_agent>[^"]+)"
        ''', re.VERBOSE)

        self.logfile = logfile
        self._validate_logfile()
        self._result = self._parse_file()

    def _validate_logfile(self):
        claudio_file = ClaudioFileUtils(self.logfile)
        if not claudio_file.exists():
            sys.exit('文件不存在，或无访问权限：{}'.format(self.logfile))
        if not claudio_file.is_file():
            sys.exit('不是普通文本文件：{}'.format(self.logfile))

    def _parse_line(self, line):
        '解析单行日志。返回字典类型。'
        match = self.regex.search(line).groupdict()
        if match:
            if match['bytes'] == '-':
                match['bytes'] = '0'
            return match
        else:
            return None

    def _parse_file(self):
        '解析整个日志文件，返回字典类型组成的链表。'
        result_list = []
        with open(self.logfile) as fp:
            for line in fp:
                line_result = self._parse_line(line)
                # print('行结果为：', line_result)
                if line_result:
                    result_list.append(self._parse_line(line))

        return result_list
        # print('整个解析结果为：', len(result_list))

    def get_ip_bytes(self):
        '获取每个IP的bytes请求数，{remote_host:[bytes]}'
        result_dict = defaultdict(list)
        for line_result in self._result:
            result_dict[line_result['remote_host']].append(
                line_result['bytes'])
        return result_dict

    def get_access_times(self):
        '返回所有访问时间组成的链表。'
        return [line_result.get('time') for line_result in self._result]


if __name__ == '__main__':
    from pathlib import Path
    import argparse
    import sys

    # 从命令行获取日志文件
    parse = argparse.ArgumentParser(description=__doc__,
                                    formatter_class=argparse.RawTextHelpFormatter)
    parse.add_argument('-f', '--file', required=True, help='日志文件')
    parse.add_argument('-m', '--modes', required=True,
                       help='''查看哪些结果：
                       b: ip -> [bytes数]
                       t: time -> [所有访问时间组成的链表]
                       ''',
                       nargs='+')

    ALLOWED_MODES = set('b t'.split())
    ARGS = parse.parse_args()
    MODES = set([m for m in ''.join(ARGS.modes)])
    # print(modes)
    if not MODES.issubset(ALLOWED_MODES):
        parse.print_help()
        sys.exit(1)

    # 缓存结果
    PARSERESULT = ClaudioApacheLogAccessParser(ARGS.file)

    # 打印结果
    if PARSERESULT:
        for m in MODES:
            if m == 'b':
                print('\nIP->请求字节数：')
                for k, v in PARSERESULT.get_ip_bytes().items():
                    print(k, v)
            if m == 't':
                print('\n访问时间：')
                print(PARSERESULT.get_access_times())
