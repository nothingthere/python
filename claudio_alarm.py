#!/usr/bin/python3
# Author: Claudio <3261958605@qq.com>
# Created: 2017-05-31 15:18:05
# Code:
'''
闹钟实现
'''

import shutil
import subprocess
import sys
import tempfile
from pathlib import Path
from time import sleep


def main(soundfile=None, duration=1, player='mplayer'):
    '主函数'

    # 确定声音文件
    if not soundfile:
        soundfile = '~/Music/豆瓣/All-Your-Love.mp3'
    soundpath = Path(soundfile).expanduser()
    # print(soundfile.exists())
    if not soundpath.exists():
        sys.exit('声音文件"{}"不存在'.format(soundfile))

    # 暂停闹钟指定时间
    sleep(duration)

    # 播放音频文件
    if not shutil.which(player):
        sys.exit('请先安装"{}"播放器'.format(player))

    with tempfile.TemporaryFile() as fp:
        subprocess.run([player, str(soundpath)], stdout=fp, stderr=fp)


if __name__ == '__main__':
    import argparse
    import claudio_parse_shell_cmd_sleep_args
    from datetime import datetime

    parse = argparse.ArgumentParser(description='闹钟')
    parse.add_argument('-s', '--soundfile',
                       default='/home/claudio/Music/豆瓣/All-Your-Love.mp3', help='音频文件')
    parse.add_argument('-p', '--player', default='mplayer', help='播放器')
    parse.add_argument('-d', '--duration', default='1',
                       help='时间设定，与Linux系统sleep命令时间指定格式相同')
    args = parse.parse_args()
    # print(args.soundfile)
    # print(args.player)
    # print(args.duration)
    now = datetime.today()
    print('闹钟开启@{}:{}'.format(now.hour, now.minute))
    print('q)退出')
    main(soundfile=args.soundfile, player=args.player, duration=int(
        claudio_parse_shell_cmd_sleep_args.parse(args.duration)))

    sys.exit()
