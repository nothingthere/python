#!/usr/bin/python3
# Author: Claudio <3261958605@qq.com>
# Created: 2017-06-04 12:56:55
# Code:
'''
替换Apache配置文件DocumentRoot标签内容
'''

import re

VHOST_START = re.compile(r'<VirtualHost\s+(.*?)')
VHOST_END = re.compile(r'</VirtualHost')
DOCROOT_RE = re.compile(r'(DocumentRoot\s+)(\S+)')


def replace_docroot(config_file_path, vhost, new_docroot):
    '''替换apache配置文件CONFIG_FILE_PATH中，虚拟主机名为VHOST的
    DocumentRoot标签内容为new_docroot
    '''
    in_vhost = False
    curr_vhost = None

    with open(config_file_path) as fp:
        for line in fp:
            vhost_start_match = VHOST_START.search(line)
            if vhost_start_match:
                curr_vhost = vhost_start_match.groups()[0]
                in_vhost = True
            if in_vhost and (curr_vhost == vhost):
                docroot_match = DOCROOT_RE.search(line)
                if docroot_match:
                    line = docroot_match.expand(r'\1{}'.format(new_docroot))
                    # line = DOCROOT_RE.sub(r'\1{}'.format(new_docroot), line)
            if VHOST_END.search(line):
                in_vhost = False

            yield line


if __name__ == '__main__':
    import argparse
    parse = argparse.ArgumentParser(description='替换Apache配置文件DocumentRoot标签内容')
    parse.add_argument('-f', '--file', required=True, help='原配置文件路径')
    parse.add_argument('-v', '--vhost', required=True, help='虚拟主机地址')
    parse.add_argument('-d', '--docroot', required=True, help='新的docroot路径')
    args = parse.parse_args()
    # print(args.file)
    # print(args.vhost)
    # print(args.docroot)
    for line in replace_docroot(args.file, args.vhost, args.docroot):
        print(line, end='')
