#!/usr/bin/python3
# Author: Claudio <3261958605@qq.com>
# Created: 2017-06-05 12:55:28
# Code:
'''
文件处理工具
'''


from pathlib import Path

import magic


class ClaudioFileUtils:
    '文件处理工具类'

    def __init__(self, filename):
        self.filename = filename
        self._filepath = Path(filename)
        if self.is_file():
            file_magic = magic.Magic(mime=True, uncompress=True)
            self._filetype = file_magic.from_file(self.filename)
        else:
            self._filetype = None

    def exists(self):
        '文件是否存在。没有访问权限也返回False。'
        try:
            return self._filepath.exists()
        except PermissionError:
            return False

    def is_file(self):
        '是否为普通文件。'
        return self.exists() and self._filepath.is_file()

    def is_dir(self):
        '是否为文件夹。'
        return self.exists() and self._filepath.is_dir()

    def is_text_file(self):
        '是否为文本文件。'
        return self._filetype and 'text' in self._filetype

    def is_excel_file(self):
        '是否为excel文件。'
        return self._filetype and 'excel' in self._filetype

    def is_audio(self):
        '是否为音频文件。'
        return self._filetype and 'audio' in self._filetype

    def is_video(self):
        '是否为视频文件。'
        return self._filetype and 'video' in self._filetype


if __name__ == '__main__':
    filename = '/var/log/apache2/access.log'
    # filename = '/home/claudio/test.txt'
    # filename = '/home/claudio/身份证.xls'
    claudio_file = ClaudioFileUtils(filename)
    print(claudio_file.is_excel_file())
