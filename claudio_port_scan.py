#!/usr/bin/python3
# Author: Claudio <3261958605@qq.com>
# Created: 2017-06-27 18:31:18
# Code:
'''
端口扫描
'''

import concurrent.futures
import socket
import time

# 常见端口号和含义
# 参考自：https://en.wikipedia.org/wiki/Port_(computer_networking)#Common_port_numbers
PORTS_MAP = {
    21: 'FTP',
    22: 'SSH',
    23: 'Telnet remote login',
    25: 'SMTP',
    53: 'DNS',
    80: 'HTTP',
    110: 'POP3',
    119: 'NNTP',
    123: 'NTP',
    143: 'IMAP',
    161: 'SNMP',
    194: 'IRC',
    443: 'HTTPS'
}


def scan_port(server, port):
    time.sleep(0.5)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((server, port))
        return True
    except:
        return False


def main():
    server = 'sdhsscgs.com'
    ports = PORTS_MAP
    result = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=len(ports)) as executor:
        future_to_port = {executor.submit(
            scan_port, server, port): port for port in ports}
        for future in concurrent.futures.as_completed(future_to_port):
            port = future_to_port[future]
            try:
                is_open = future.result()
            except Exception as exc:
                print('{!r}抛出错误：{}'.format(port, exc))
            else:
                if is_open:
                    # print('开启：', port, '!' * 10)
                    print('开启：', PORTS_MAP[port])
                    result.append(port)
                else:
                    print('关闭：', port)

        return result


if __name__ == '__main__':
    opened_port = main()
    print('-' * 10)
    print('开启的端口有：', opened_port)
    print('主线程结束！')
